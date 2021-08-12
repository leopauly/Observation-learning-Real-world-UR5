# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "controller_manager_msgs: 4 messages, 6 services")

set(MSG_I_FLAGS "-Icontroller_manager_msgs:/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(controller_manager_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg" NAME_WE)
add_custom_target(_controller_manager_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "controller_manager_msgs" "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg" ""
)

get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllers.srv" NAME_WE)
add_custom_target(_controller_manager_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "controller_manager_msgs" "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllers.srv" "controller_manager_msgs/ControllerState:controller_manager_msgs/HardwareInterfaceResources"
)

get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg" NAME_WE)
add_custom_target(_controller_manager_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "controller_manager_msgs" "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg" "controller_manager_msgs/HardwareInterfaceResources"
)

get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/LoadController.srv" NAME_WE)
add_custom_target(_controller_manager_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "controller_manager_msgs" "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/LoadController.srv" ""
)

get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg" NAME_WE)
add_custom_target(_controller_manager_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "controller_manager_msgs" "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg" ""
)

get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/UnloadController.srv" NAME_WE)
add_custom_target(_controller_manager_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "controller_manager_msgs" "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/UnloadController.srv" ""
)

get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllersStatistics.msg" NAME_WE)
add_custom_target(_controller_manager_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "controller_manager_msgs" "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllersStatistics.msg" "controller_manager_msgs/ControllerStatistics:std_msgs/Header"
)

get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/SwitchController.srv" NAME_WE)
add_custom_target(_controller_manager_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "controller_manager_msgs" "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/SwitchController.srv" ""
)

get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllerTypes.srv" NAME_WE)
add_custom_target(_controller_manager_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "controller_manager_msgs" "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllerTypes.srv" ""
)

get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ReloadControllerLibraries.srv" NAME_WE)
add_custom_target(_controller_manager_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "controller_manager_msgs" "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ReloadControllerLibraries.srv" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
)
_generate_msg_cpp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
)
_generate_msg_cpp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg"
  "${MSG_I_FLAGS}"
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
)
_generate_msg_cpp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllersStatistics.msg"
  "${MSG_I_FLAGS}"
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
)

### Generating Services
_generate_srv_cpp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllers.srv"
  "${MSG_I_FLAGS}"
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg;/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_cpp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/LoadController.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_cpp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllerTypes.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_cpp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/UnloadController.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_cpp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/SwitchController.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_cpp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ReloadControllerLibraries.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
)

### Generating Module File
_generate_module_cpp(controller_manager_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(controller_manager_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(controller_manager_msgs_generate_messages controller_manager_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_cpp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllers.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_cpp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_cpp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/LoadController.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_cpp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_cpp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/UnloadController.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_cpp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllersStatistics.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_cpp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/SwitchController.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_cpp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllerTypes.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_cpp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ReloadControllerLibraries.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_cpp _controller_manager_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(controller_manager_msgs_gencpp)
add_dependencies(controller_manager_msgs_gencpp controller_manager_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS controller_manager_msgs_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
)
_generate_msg_lisp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
)
_generate_msg_lisp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg"
  "${MSG_I_FLAGS}"
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
)
_generate_msg_lisp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllersStatistics.msg"
  "${MSG_I_FLAGS}"
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
)

### Generating Services
_generate_srv_lisp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllers.srv"
  "${MSG_I_FLAGS}"
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg;/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_lisp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/LoadController.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_lisp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllerTypes.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_lisp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/UnloadController.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_lisp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/SwitchController.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_lisp(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ReloadControllerLibraries.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
)

### Generating Module File
_generate_module_lisp(controller_manager_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(controller_manager_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(controller_manager_msgs_generate_messages controller_manager_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_lisp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllers.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_lisp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_lisp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/LoadController.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_lisp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_lisp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/UnloadController.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_lisp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllersStatistics.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_lisp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/SwitchController.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_lisp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllerTypes.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_lisp _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ReloadControllerLibraries.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_lisp _controller_manager_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(controller_manager_msgs_genlisp)
add_dependencies(controller_manager_msgs_genlisp controller_manager_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS controller_manager_msgs_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
)
_generate_msg_py(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
)
_generate_msg_py(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg"
  "${MSG_I_FLAGS}"
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
)
_generate_msg_py(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllersStatistics.msg"
  "${MSG_I_FLAGS}"
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
)

### Generating Services
_generate_srv_py(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllers.srv"
  "${MSG_I_FLAGS}"
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg;/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_py(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/LoadController.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_py(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllerTypes.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_py(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/UnloadController.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_py(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/SwitchController.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
)
_generate_srv_py(controller_manager_msgs
  "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ReloadControllerLibraries.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
)

### Generating Module File
_generate_module_py(controller_manager_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(controller_manager_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(controller_manager_msgs_generate_messages controller_manager_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerStatistics.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_py _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllers.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_py _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllerState.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_py _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/LoadController.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_py _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/HardwareInterfaceResources.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_py _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/UnloadController.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_py _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/msg/ControllersStatistics.msg" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_py _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/SwitchController.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_py _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ListControllerTypes.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_py _controller_manager_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wisdom/catkin_ws/src/ridgeback/ros_control/controller_manager_msgs/srv/ReloadControllerLibraries.srv" NAME_WE)
add_dependencies(controller_manager_msgs_generate_messages_py _controller_manager_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(controller_manager_msgs_genpy)
add_dependencies(controller_manager_msgs_genpy controller_manager_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS controller_manager_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/controller_manager_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(controller_manager_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/controller_manager_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(controller_manager_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/controller_manager_msgs/.+/__init__.pyc?$"
  )
endif()
add_dependencies(controller_manager_msgs_generate_messages_py std_msgs_generate_messages_py)
