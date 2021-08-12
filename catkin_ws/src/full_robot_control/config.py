import numpy as np
import math as m

# State description parameters
NUM_OBJS = 10         # Number of dynamic objects in the scene (incl. goal obj.)
N_GRIPPER_JOINTS = 6 # Number of gripper joints (=1 DOF)
BASE_DOF = 3
ARM_DOF = 6
DOF = BASE_DOF + ARM_DOF            # Robot's degrees of freedom
GRIPPER_DOF = 1      # Gripper's degree of freedom
N_QPOS = DOF + NUM_OBJS*7 + N_GRIPPER_JOINTS
N_QVEL = DOF + NUM_OBJS*6 + N_GRIPPER_JOINTS

# Inverse Kinematics parameters
SITE_NAME = "ee_point" # Point of interest at the end effector for IK
JOINTS = [ "shoulder_pan_joint",
          "shoulder_lift_joint", "elbow_joint", "wrist_1_joint",
          "wrist_2_joint", "wrist_3_joint"] # Joints to consider during IK

# JOINTS = ["robot_x", "robot_y", "robot_z", "shoulder_pan_joint",
#           "shoulder_lift_joint", "elbow_joint", "wrist_1_joint",
#           "wrist_2_joint", "wrist_3_joint"] # Joints to consider during IK
TOL = 1e-14
MAX_STEPS = 100

# Cost weights for grasping in clutter
W_DISTURBANCE = 1e-6      # State deviation/disturbance cost
W_ACCELERATION = 1e-6     # Acceleration cost
W_CLUTTER_GOAL = 1e4   # Clutter grasping final cost
W_GRIPPER_OPEN = 1e2   # Cost to ensure open gripper at final state

# Fixed trajectory optimization costs
TABLE_ROBOT_COLLISION_COST = 1e5 # Fixed cost for table-robot collision
TABLE_Z = 0.45         # Height threshold to define fallen objects
EDGE_PENALTY = 1e5     # Edge penalty to penalize fallen objects
TOPPLING_COST = 1e5     # Cost to penalize toppled objects
MARKER_COLLISION_CHECK = True

COST_THRESH = 20      # Cost threshold to define a successful trajectory
OFFSET_DISTANCE = 0.01 # Desired relative gripper-object distance
GOAL_HALF_H = 0.04  # Half height of the goal object
GOAL_Z_POSITION = 0.47 # Bisto
# Sampling parameters
EXPLORATION_VARIANCE = 7e-4 # Exploration variance for robot joints
STD_DEV_ARR = np.sqrt(EXPLORATION_VARIANCE*np.ones(DOF + GRIPPER_DOF))
# STD_DEV_ARR[-1] += 0.2 # Explore more in the gripper joint
# STD_DEV_ARR[-2] += 0.1 # Explore more in the robot's angular vel.
# STD_DEV_ARR[-3] += 0.2 # Explore more in the robot's pependiular dir.

STD_DEV_ARR[0] = 0.05 # Base x
STD_DEV_ARR[1] = 0.05 # Base y
STD_DEV_ARR[2] = 0.05 # Base thetha
STD_DEV_ARR[3] = 0.05 # Shoulder pan
STD_DEV_ARR[4] = 0.05 # Shoulder lift
STD_DEV_ARR[5] = 0.05 # Elbow
STD_DEV_ARR[6] = 0.05 # Wrist 1
STD_DEV_ARR[7] = 0.05 # Wrist 2
STD_DEV_ARR[8] = 0.05 # Wrist 3


NUM_TRAJ_ROLLOUTS = 4  # Number of rollouts per iteration of traj. optimization
ARM_HOME_QPOS =  np.array([91.98,-74.0,148.17,-73.99,90.52,1.41])*m.pi/180.0
ARM_TEST_QPOS = ARM_HOME_QPOS.copy()
ARM_TEST_QPOS[-1] += m.pi/2
ARM_TEST_QPOS[2] -= 10*m.pi/180.


# Simulation parameters
CTRL_DUR = 0.2           # Control duration
SIM_TIMESTEP = 2e-4      # Simulation time step
LAG_CONSTANT = 1e-1      # Multiple of the number of substeps for extra sim
STOCH_SLOPE = 1e-1 # Std. dev. for noise added on velocities at each time step.
TEST_STOCHASTICITY = False # Boolean to test stochasticity in the viewer

# Parallel processing parameters
NUM_POOL_PROCESSES = 4

# Online re-planning parameters
MANY_CTRLS = 5  # Number of control steps during oprn-loop planning
FEW_CTRLS = 3    # Number of control steps during re-planning
MANY_ITER = 6   # Number of iterations during open-loop planning
FEW_ITER = 3     # Number of iterations during re-planning
MAX_MPC_ACTIONS = 20 # Maximum number of actions to execute under MPC
MIN_TRAJ_COST = COST_THRESH   # Trajectory cost indicating grasp success
MIN_STATE_DEVIATION = 2 # State deviation threshold to re-plan
MIN_CTRL_STEPS = 1      # Mininim number of actions to re-plan
CAPTURE_FRAMES = False
COLLECT_DATA = True
