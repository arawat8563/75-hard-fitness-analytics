from fitness_analytics.models import Exercise

exercise = Exercise(
    exercise_name="Bench Press",
    muscle_group="Chest"
)

print(exercise.exercise_name)
print(exercise.muscle_group)