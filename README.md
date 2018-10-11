# Optimization Based Cartesian Controller for Robots

This node was developed during my master thesis project at [ISR](http://welcome.isr.tecnico.ulisboa.pt/)/[IST](https://tecnico.ulisboa.pt/pt/).

It offers a cartesian controller in x degrees of freedom (x = 10 for our use case, 7 arm joints + base).

It moves base and arm in a combined way to achive 3D poses with the end effector.

A nice video showing some results can be seen [here](https://www.youtube.com/watch?v=_-M7cxlhyYY&t=38s).

# Credits

Brought to you by:
- [Instituto Superior Tecnico, Lisboa](http://welcome.isr.tecnico.ulisboa.pt/)
- [Institute for Systems and Robotics (ISR)](http://welcome.isr.tecnico.ulisboa.pt/)
- [Laboratory of Robotics and Engineering Systems (LARSyS)](http://larsys.pt/)
- [SocRob RoboCup team](http://socrob.isr.tecnico.ulisboa.pt)

This code was tested on Ubuntu 16.04 and ROS kinetic.

The code is generic and takes input from URDF model, so any robot can use it.

It requires for your arm to have a velocity control interface.

# Usage

run your robot driver (bringup):

        this depends on your robot!

switch your arm driver to velocity control mode:

        this dependy on your robot! (keep in mind typically controllers are launched by default in trajectory ctrl mode)

run the controller:

        roslaunch optimisation_cartesian_controller optimization_cart_ctrler.launch target_pose:=/my_goal_pose

publish pose stamped message as goal pose:

        rostopic pub /my_goal_pose std_msgs/PoseStamped ... (base_link frame!)

trigger node to start controller:

        rostopic pub /optimization_cart_ctrler_node/event_in std_msgs/String e_start

cancel controller execution (if needed):

        rostopic pub /optimization_cart_ctrler_node/event_in std_msgs/String e_stop

Listen to controller output:

        rostopic echo /optimization_cart_ctrler_node/event_out
        
if controller execution was succesfull you should get: e_success
