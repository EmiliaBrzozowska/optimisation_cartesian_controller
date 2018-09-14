#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# for your packages to be recognized by python
d = generate_distutils_setup(
 packages=['mbot_optimization_cartesian_controller_ros'],
 package_dir={'mbot_optimization_cartesian_controller_ros': 'ros/src/mbot_optimization_cartesian_controller_ros'}
)

setup(**d)
