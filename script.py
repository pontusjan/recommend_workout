from data import workouts
from data_bst import workouts_with_movement, movements_bst
from print_functions import *

#Function to find the movement of choice
def find_movement():
    movement_letters = input("Which movement would you like your workout to include? Enter the first letters to search:\n")
    movements = movements_bst.autocomplete_depth_first(movement_letters)

    #If there are multiple movements matching the input letters, search again
    while len(movements) > 1:
        message = "These are the available movements for '{0}': {1}".format(movement_letters, movements)
        print_message(message)
        movement_letters = input("Enter the first letters of the movement you'd like your workout to include:\n")
        movements = movements_bst.autocomplete_depth_first(movement_letters)

    #If there's no movements matching the input, give the user a chance to start over
    if len(movements) == 0:
        start_over_option = input("Sorry, no movement for '{}', would you like to search for some other movement? (y / n)\n".format(movement_letters))
        if start_over_option == "y":
            find_movement()
    
    #If there's only one matching movement, print and return it
    else:
        user_input = input("\nFor '{0}', the only movement is {1}. Is that correct? (y / n)\n".format(movement_letters, movements[0]))
        if user_input == "y":
            return movements[0]
        else:
            find_movement()
        
#Choose a workout including the chosen movement
def find_workout(movement):
    possible_workouts = workouts_with_movement[movement]
    message = ""
    message += "Possible workouts:\n"

    #Print the possible workouts, with a corresponding index
    for i in range(len(possible_workouts)):
        message += "{0} - {1}\n".format(i+1, workouts[possible_workouts[i]].name)
    print_message(message)

    #Let the user make a choice, until the choice is valid
    while True:
      user_choice = input("Enter the number for the workout you want\n")
      try:
        user_choice = int(user_choice)
        break
      except ValueError:
        print("Oops, '{0}' is not a number.".format(user_choice))
    while not (user_choice > 0 and user_choice <= len(possible_workouts)):
      print("Oops, '{0}' is not a number of a workout.".format(user_choice))
      while True:
        try:
          user_choice = int(input("Enter the number for the workout you want\n"))
          break
        except ValueError:
          print("Oops, '{0}' is not a number.".format(user_choice))

    #Return the workout name
    return possible_workouts[user_choice - 1]       
    
#The workout recommendation functionality, looping for as long as the user wants to continue
def choose_workout():
    #Find the workout
    movement = find_movement()
    workout = find_workout(movement)

    #Print the workout
    message = "Here's your workout:\n\n{0}".format(workouts[workout].get_workout())
    print_message(message)

    #Wanna go again?
    one_more_time = input('Would you like to search for another workout? (y / n)\n')
    if one_more_time == "y":
        choose_workout()

def program():
  greet()
  choose_workout()
  goodbye()

#Let's go! =]]---]]=
program()