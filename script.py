from data import workouts

workouts_with_movement = {}
for workout_name in workouts.keys():
  for mvmt in workouts[workout_name].movements:
    if not mvmt in workouts_with_movement.keys():
      workouts_with_movement[mvmt] = [workout_name]
    else:
      workouts_with_movement[mvmt].append(workout_name)

def greet():
    print("""¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11_____1¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1__________1¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_____________¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______________¶11
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1__________________
¶¶¶¶¶¶¶1____1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1________________¶¶
¶¶¶¶¶__________¶¶¶¶¶¶¶¶¶¶¶11____________________¶¶
¶¶¶¶____________¶¶¶¶11_____11___1______________1¶¶
¶¶¶1__________________11¶¶¶¶¶__1¶1_____________¶¶¶
¶¶¶1_______________¶¶¶¶¶¶¶¶¶¶__1¶¶¶__________1¶¶¶¶
¶¶¶______________1¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶11__111¶¶¶¶¶¶
¶¶¶1_____________¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶____________¶¶____1¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶___________________¶¶1___1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶11111¶1__________¶1____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________1¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______________1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶1____________1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶1____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶1___________1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶1___________1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1___________1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    """)
    print("Welcome to workout recommendations!")

def find_movement():
    movement_letters = input("Which movement would you like your workout to include? Write the first letter and enter:\n")
    movements = get_movement_recommendation_from_letters(movement_letters)
    while len(movements) > 1:
        print("\nThese are the available movements: {}".format(movements))
        movement_letters = input("Write the first letters of the movement you'd like to include\n")
        movements = get_movement_recommendation_from_letters(movement_letters)
    if len(movements) == 0:
        start_over_option = input("Sorry, no movement, would you like to start over? (y / n)\n")
        if start_over_option == "y":
            find_movement()
    else:
        print('Okay, {}'.format(movements[0]))
        return movements[0]
        
def find_workout(movement):
    possible_workouts = workouts_with_movement[movement]
    print("Possible workouts:\n")
    for i in range(len(possible_workouts)):
        print("{0} - {1}".format(i+1, workouts[possible_workouts[i]].name))
    user_choice = int(input("Enter the number for the workout you want\n"))
    if user_choice - 1 > len(possible_workouts) or user_choice < 1:
        user_choice = input("Oops, try again.")
    return possible_workouts[user_choice - 1]

def choose_workout():
    movement = find_movement()
    workout = find_workout(movement)
    print("Here's your workout:\n")
    print(workouts[workout].get_workout())
    one_more_time = input('Would you like to choose another workout? (y / n)\n')
    if one_more_time == "y":
        choose_workout()

def get_movement_recommendation_from_letters(letters):
    possible_movements = []
    for movement in workouts_with_movement.keys():
        if movement[0:len(letters)] == letters:
            possible_movements.append(movement)
    return possible_movements

def get_workout_recommendation_from_letters(lst, letters):
    possible_workouts = []
    for workout in lst:
        if workout[0:len(letters)] == letters:
            possible_workouts.append(workout)
    return possible_workouts

def get_workout_recommendation(movement):
    if movement in workouts_with_movement.keys():
        print("These workouts include {}:".format(movement))
        for workout in workouts_with_movement[movement]:
            print("- " + workouts[workout].name)

def goodbye():
    print("Thanks for using the workout recommendator")

def program():
    greet()
    choose_workout()
    goodbye()

program()