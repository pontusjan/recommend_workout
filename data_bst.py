from bst import BinarySearchTree
from data import workouts
import random

#Dict with every unique movement as keys to all the workouts that include the movement
workouts_with_movement = {}
for workout_name in workouts.keys():
  for mvmt in workouts[workout_name].movements:
    if not mvmt in workouts_with_movement.keys():
      workouts_with_movement[mvmt] = [workout_name]
    elif workout_name not in workouts_with_movement[mvmt]:
      workouts_with_movement[mvmt].append(workout_name)

#List of the movement names
movements = list(workouts_with_movement.keys())

#Initiate a BST of movement names with a random movement from the movement list as root
movements_bst = BinarySearchTree(movements.pop(random.randint(0, len(movements) - 1)))
for movement in movements:
  movements_bst.insert(movement)

