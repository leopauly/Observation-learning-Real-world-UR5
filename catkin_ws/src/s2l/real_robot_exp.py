
import numpy as np
import IPython
from std_msgs.msg import Float32MultiArray
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import rospy
import control_sequences
import time
import timeit
import matplotlib.pyplot as plt

REWARD_THRESH = 100
MAX_ITERATIONS = 10
K = 8 # Number of random control sequence variations per iteration
#STD_DEV_ARR = np.array([5e-2, 1e-8, 1e-8, 1e-8, 6e-2, 1e-8]) # std_dev for exploration

# std_dev for exploration for pushing task (joints0 (more) and 4 (less))
STD_DEV_ARR = np.array([5e-2, 1e-4, 1e-4, 1e-4, 2e-2, 1e-4])
# std_dev for exploration for hammering task (joints0 (less) and 4 (more))
#STD_DEV_ARR = np.array([2e-2, 1e-4, 1e-4, 1e-4, 3e-2, 1e-4])

TIMEOUT = 20000
MIN_ROLLOUT = 2
#robot_record_pub = rospy.Publisher("/robot_record", numpy_msg(Floats), queue_size=1)

class real_robot_trajopt():

    def __init__(self):


        self.K = K
        self.cand_ctrl_seq = control_sequences.sequence_1

        rospy.init_node("real_robot_exp", anonymous=True, disable_signals=True)

        self.rate=rospy.Rate(50) # Loop rate of 10 hertz

        """
        rospy.Subscriber("/robot_done", numpy_msg(Floats),
                                        self.robot_done_callback,
                                        queue_size=1)

        rospy.Subscriber("/robot_reward", numpy_msg(Floats),
                                          self.reward_callback,
                                          queue_size=1)
        """

        self.robot_record_pub = rospy.Publisher("/robot_record",
                                               numpy_msg(Floats),
                                               queue_size=1)
        self.record_command = np.zeros(2)

        self.sequence_done_pub = rospy.Publisher('/sequence_done',
                                                numpy_msg(Floats),
                                                queue_size=1)
        self.seq_done_command = np.array([0.0])

        self.robot_pub = rospy.Publisher('/robot_command', Float32MultiArray,
                                                           queue_size=10)

    def reset_robot(self):
        print ("Resetting robot")

        # 100 or any number > 0 for reset
        dum = self.cand_ctrl_seq[0]
        robot_msg = Float32MultiArray(data=[dum[0], dum[1], dum[2],
                                            dum[3], dum[4], dum[5], 100.])
        #robot_msg = Float32MultiArray(data=[self.cand_ctrl_seq, 100])
        time.sleep(2)
        self.robot_pub.publish(robot_msg)
        print ("Published action")
        robot_done = rospy.wait_for_message('/robot_done', numpy_msg(Floats), timeout=TIMEOUT)

        print ("Done resetting robot")

    def reset_object(self):
        print ("Resetting object")

        while True:
            n = raw_input("\n\nEnter 'p' if object reset is complete:\n\n")
            if n == "p":
                break
            else:
                print ("Invalid input")

        print ("Done resetting")

    def gen_rand_seqs(self, cand_ctrl_seq):
        num_ctrls = cand_ctrl_seq.shape[0]
        size_ctrls = cand_ctrl_seq.shape[1]

        print (size_ctrls)
        rand_ctrl_seqs = np.zeros((self.K, num_ctrls, size_ctrls))

        variation = np.zeros((self.K, num_ctrls, size_ctrls))
        for k in range(self.K):
            variation[k] = np.random.normal(0, STD_DEV_ARR, (num_ctrls,
                                                             int(size_ctrls)))
            rand_ctrl_seqs[k] = cand_ctrl_seq + variation[k]

        return rand_ctrl_seqs

    def execute_cand_seq(self, ctrl_seq):
        time.sleep(2)
        self.robot_record_pub.publish(self.record_command)
        #robot_record_pub.publish(self.record_command)
        print (ctrl_seq.shape[0])
        for k in range(ctrl_seq.shape[0]):
            #print ("yes")
            dum = ctrl_seq[k]
            robot_msg = Float32MultiArray(data=[dum[0], dum[1], dum[2],
                                                dum[3], dum[4], dum[5], 0.])
            #rospy.loginfo(robot_msg)
            self.robot_pub.publish(robot_msg)
            robot_done = rospy.wait_for_message('/robot_done', numpy_msg(Floats), timeout=TIMEOUT)
            #self.rate.sleep()
        # Declare that sequence execution is done
        self.sequence_done_pub.publish(self.seq_done_command)
        print ("Done executing")

    def get_reward(self):
	print('Waiting for reward')
        robot_reward = rospy.wait_for_message('/robot_reward', numpy_msg(Floats))
        #robot_reward = 10.
        print (robot_reward)

        return robot_reward.data[0]

    def traj_opt(self):
        """ Stochastic Trajectory Optimization """
        self.reset_robot()
        self.reset_object()
        sequences = np.zeros((MAX_ITERATIONS+1, self.cand_ctrl_seq.shape[0],
                            self.cand_ctrl_seq.shape[1]))
        print ("Executing the initial candidate control sequence")
        cand_ctrl_seq = self.cand_ctrl_seq.copy()
	sequences[0]=cand_ctrl_seq.copy()
        self.execute_cand_seq(cand_ctrl_seq)
        cand_reward = self.get_reward()

        print ("Initial reward is", cand_reward)
        max_iter=0
        reward_array = np.zeros(self.K)

        # Visualize rewards
        plt_reward_arr = np.zeros(MAX_ITERATIONS+1)
        plt_reward_arr[0] = cand_reward
        plt.ion()
	print('sequences:',sequences)
	print('plt_reward_arr:',plt_reward_arr)
        while ((cand_reward <= REWARD_THRESH) and (max_iter<MAX_ITERATIONS)):
	    print(max_iter, '<' ,MAX_ITERATIONS)
            reward_array = np.zeros(self.K)
            print ("Current iteration is {}".format(max_iter))

            self.reset_robot()
            self.reset_object()

            rand_ctrl_seqs = self.gen_rand_seqs(cand_ctrl_seq)

            for k in range(self.K):
		print(self.K,'iteration:',max_iter,'rollout:',k)
                print ("This is rollout number", k)
                start_time = timeit.default_timer()
                self.execute_cand_seq(rand_ctrl_seqs[k])
                end_time = start_time - timeit.default_timer()
                print ("This sequence took {} seconds".format(end_time))
                reward_array[k] = self.get_reward()
                self.reset_robot()
                self.reset_object()

            print ("The maximum reward for this iteration is",np.max(reward_array) )


            max_reward_index = np.argmax(reward_array)

            if cand_reward < reward_array[max_reward_index]:
                cand_reward = reward_array[max_reward_index]
                cand_ctrl_seq = rand_ctrl_seqs[max_reward_index]

            max_iter+=1

            if self.K > MIN_ROLLOUT:
                self.K -= 2


            plt_reward_arr[max_iter] = cand_reward
	    print('Max_iter value:',max_iter)
            sequences[max_iter] = cand_ctrl_seq.copy()
	    print('sequences:',sequences)
	    print('plt_reward_arr:',plt_reward_arr)
            np.save("reward_list",plt_reward_arr)
            np.save("optimal_sequence",cand_ctrl_seq)
            np.save("sequences",sequences)
            plt.plot(plt_reward_arr[0:max_iter+1])
            plt.xlim([0,MAX_ITERATIONS+1])
            plt.show()
            plt.pause(1)

	    

        return cand_ctrl_seq, cand_reward

    def replay(self):
        self.reset_robot()
        self.reset_object()
        print ("Executing the optimal control sequence")
        path = "./Thesis/Exp4_sweeping/V2/trial12"
        cand_ctrl_seq = np.load("{}/optimal_sequence.npy".format(path))
        #sequences = np.load("{}/sequences.npy".format(path))
        #cand_ctrl_seq = sequences[-1]

        self.execute_cand_seq(cand_ctrl_seq)
        #sequences =  np.load("{}/sequences.npy".format(path))
        v = np.load("{}/reward_list.npy".format(path))
        plt.plot(v)
        plt.show()
        #cand_reward = self.get_reward()

if __name__ == "__main__":
    opt = real_robot_trajopt()
    #optimized_sequence, optimal_reward = opt.traj_opt()
    opt.replay()
    IPython.embed()
