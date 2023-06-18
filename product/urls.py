from django.urls import path
from product.views import Buy, Workouts, CreateWorkout, EditWorkout

urlpatterns = [
    path('', Buy.as_view(), name="root"),
    path('workouts', Workouts.as_view(), name="workout_list"),
    path('workouts/new', CreateWorkout.as_view(), name="create_workout"),
    path('workouts/<pk>', EditWorkout.as_view(), name="edit_workout")
]
