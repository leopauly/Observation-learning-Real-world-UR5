# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/wisdom/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/wisdom/catkin_ws/build

# Utility rule file for clean_test_results_combined_robot_hw_tests.

# Include the progress variables for this target.
include ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests.dir/progress.make

ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests:
	cd /home/wisdom/catkin_ws/build/ridgeback/ros_control/combined_robot_hw_tests && /usr/bin/python /opt/ros/indigo/share/catkin/cmake/test/remove_test_results.py /home/wisdom/catkin_ws/build/test_results/combined_robot_hw_tests

clean_test_results_combined_robot_hw_tests: ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests
clean_test_results_combined_robot_hw_tests: ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests.dir/build.make
.PHONY : clean_test_results_combined_robot_hw_tests

# Rule to build all files generated by this target.
ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests.dir/build: clean_test_results_combined_robot_hw_tests
.PHONY : ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests.dir/build

ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests.dir/clean:
	cd /home/wisdom/catkin_ws/build/ridgeback/ros_control/combined_robot_hw_tests && $(CMAKE_COMMAND) -P CMakeFiles/clean_test_results_combined_robot_hw_tests.dir/cmake_clean.cmake
.PHONY : ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests.dir/clean

ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests.dir/depend:
	cd /home/wisdom/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wisdom/catkin_ws/src /home/wisdom/catkin_ws/src/ridgeback/ros_control/combined_robot_hw_tests /home/wisdom/catkin_ws/build /home/wisdom/catkin_ws/build/ridgeback/ros_control/combined_robot_hw_tests /home/wisdom/catkin_ws/build/ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : ridgeback/ros_control/combined_robot_hw_tests/CMakeFiles/clean_test_results_combined_robot_hw_tests.dir/depend

