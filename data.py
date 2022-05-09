class Workout:
  def __init__(self, name, measurement, rounds_or_time, movements, reps, weights, same_varying_reps=False):
    #Measurement is AMRAP or For time
    self.name = name
    self.measurement = measurement
    #Number of rounds
    self.rounds_or_time = rounds_or_time
    self.movements = movements
    self.reps = reps
    self.weights = weights
    self.same_varying_reps = same_varying_reps

  def get_workout(self):
    workout_as_string = ""
    workout_as_string += "Workout name: {0}\n".format(self.name)

    #AMRAP
    if self.measurement.lower() == 'amrap':
      workout_as_string += "As many rounds or reps as possible in {0} minutes of:\n".format(self.rounds_or_time)
      for i in range(len(self.movements)):
        weight = ""
        if self.weights[i]:
          weight += ", {0} kg".format(self.weights[i])
        workout_as_string += "{reps} {movement}{weight}\n".format(reps = self.reps[i], movement = self.movements[i], weight = weight)

    #For time  
    elif self.measurement.lower() == 'for time':
      workout_as_string += "For time"

      if self.same_varying_reps:
        same_reps_string = " "
        for i in range(len(self.reps)):
          if i > 0:
            same_reps_string += "/"
          same_reps_string += "{0}".format(self.reps[i])
        workout_as_string += "{0} reps of:\n".format(same_reps_string)
        for i in range(len(self.movements)):
          weight = ""
          if self.weights[i]:
            weight += ", {0} kg".format(self.weights[i])
          workout_as_string += "{movement}{weight}\n".format(reps = self.reps[i], movement = self.movements[i].capitalize(), weight = weight)

      else:
        if self.rounds_or_time > 1:
          workout_as_string += ", {0} rounds of".format(self.rounds_or_time)
        workout_as_string += ":\n"
        for i in range(len(self.movements)):
          weight = ""
          if self.weights[i]:
            weight += ", {0} kg".format(self.weights[i])
          workout_as_string += "{reps} {movement}{weight}\n".format(reps = self.reps[i], movement = self.movements[i], weight = weight)

    return workout_as_string


workouts = {}

workouts['Cindy'] = Workout('Cindy', 'AMRAP', 20, ['pull-ups', 'push-ups', 'air squats'], [5, 10, 15], [None, None, None])
workouts['Fran'] = Workout('Fran', 'For time', 3, ['pull-ups', 'thrusters'], [21,15,9], [None, 43], True)
workouts['Diane'] = Workout('Diane', 'For time', 3, ['deadlifts', 'handstand push-ups'], [21,15,9], [102, None], True)
workouts['Karen'] = Workout('Karen', 'For time', 1, ['wall balls'], [150], [9])
workouts['Elizabeth'] = Workout('Elizabeth', 'For time', 3, ['cleans', 'ring dips'], [21,15,9], [60,None], True)
workouts['DT'] = Workout('DT', 'For time', 5, ['deadlifts', 'hang power cleans', 'push jerks'], [12,9,6], [70, 70, 70])
workouts['Jackie'] = Workout('Jackie', 'For time', 1, ['row', 'thrusters', 'pull-ups'], ['1000 m', 50, 30], [None, 20 ,None])
workouts['Grace'] = Workout('Grace', 'For time', 1, ['clean & jerks'], [30], [60])
workouts['Isabel'] = Workout('Isabel', 'For time', 1, ['snatches'], [30], [60])
workouts['Helen'] = Workout('Helen', 'For time', 3, ['run', 'kettlebell swings', 'pull-ups'], ['400 m', 21, 12], [None, 24 ,None])
workouts['Annie'] = Workout('Annie', 'For time', 5, ['double unders', 'sit-ups'], [50,40,30,20,10], [None, None], True)
workouts['Nancy'] = Workout('Nancy', 'For time', 5, ['run', 'overhead squats'], ['400 m', 15], [None, 43])
workouts['Kelly'] = Workout('Kelly', 'For time', 5, ['run', 'box jumps', 'wall balls'], ['400 m', 30, 30], [None, None, 9])
workouts['Christine'] = Workout('Christine', 'For time', 3, ['row', 'deadlifts', 'box jumps'], ['500 m', 12, 21], [None, 'bodyweight', None])
workouts['Filthy Fifty'] = Workout('Filthy Fifty', 'For time', 1, ['box jumps', 'jumping pull-ups', 'kettlebell swings', 'walking lunges', 'knees-to-elbows', 'push press', 'back extensions', 'wall balls', 'burpees', 'double unders'], [50, 50, 50, 50, 50, 50, 50, 50, 50, 50], [None, None, 16, None, None, 20, None, 9, None, None])
workouts['Open 11.1'] = Workout('Open 11.1', 'AMRAP', 10, ['double unders', 'power snatches'], [30, 15], [None, 30])
workouts['Open 14.5'] = Workout('Open 14.5', 'For time', 7, ['thrusters', 'bar facing burpees'], [21, 18, 15, 12, 9, 6, 3], [43, None], True)
workouts['Open 18.2'] = Workout('Open 18.2', 'For time', 10, ['dumbbell squats', 'bar facing burpees'], [1,2,3,4,5,6,7,8,9,10], [22.5, None], True)
workouts['Amanda'] = Workout('Amanda', 'For time', 3, ['ring muscle-ups', 'squat snatches'], [9,7,5], [None, 60], True)
  

