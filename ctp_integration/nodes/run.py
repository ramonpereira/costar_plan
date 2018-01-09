#!/usr/bin/env python

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import argparse
import rospy

from costar_task_plan.mcts import PlanExecutionManager, DefaultExecute
from costar_task_plan.robotics.core import RosTaskParser
from costar_task_plan.robotics.tom import *
from sensor_msgs.msg import JointState

from ctp_integration import MakeStackTask
from ctp_integration.util import GetDetectObjectsService

def getArgs():
    '''
    Get argument parser and call it to get information from the command line.

    Parameters:
    -----------
    none

    Returns:
    --------
    args: command-line arguments
    '''
    parser = argparse.ArgumentParser(add_help=True, description="Parse rosbag into graph.")
    parser.add_argument("--fake",
                        action="store_true",
                        help="create some fake options for stuff")
    parser.add_argument("--show",
                        action="store_true",
                        help="show a graph of the compiled task")
    parser.add_argument("--plan",
                        action="store_true",
                        help="set if you want the robot to generate a task plan")
    parser.add_argument("--execute",
                        type=int,
                        help="execute this many loops")
    parser.add_argument("--iter","-i",
                        default=0,
                        type=int,
                        help="number of samples to draw")

    return parser.parse_args()

def fakeTaskArgs():
  '''
  Set up a simplified set of arguments. These are for the optimization loop, 
  where we expect to only have one object to grasp at a time.
  '''
  args = {
    'block': ['block_1', 'block_2'],
    'endpoint': ['r_ee_link'],
    'high_table': ['ar_marker_2'],
    'Cube_blue': ['blue1'],
    'Cube_red': ['red1'],
    'Cube_green': ['green1'],
    'Cube_yellow': ['yellow1'],
  }
  return args

def main():
    # Read options from command line
    args = getArgs()

    # Create the task model
    task = MakeStackTask()

    # create fake data or listen for a detected object information message
    if args.fake:
        world.addObjects(fakeTaskArgs())
        filled_args = task.compile(fakeTaskArgs())
    else:
        objects = GetDetectObjectsService()
        raise NotImplementedError('wait for object detection information')

    # print out task info
    if args.verbose:
        print(task.nodeSummary())
        print(task.children['ROOT()'])

    if args.show:
        from costar_task_plan.tools import showTask
        showTask(task)

    for i in range(args.execute):
        print("Executing trial %d..."(i))

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException as e:
        pass
