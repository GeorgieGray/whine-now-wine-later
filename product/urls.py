from django.urls import path
from product.views import Buy, Workouts, CreateWorkout, EditWorkout, DeleteWorkout
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Buy.as_view(), name="root"),
    path('workouts', login_required(Workouts.as_view()), name="workout_list"),
    path('workouts/new', login_required(CreateWorkout.as_view()), name="create_workout"),
    path('workouts/<pk>/delete', login_required(DeleteWorkout.as_view()), name="delete_workout"),
    path('workouts/<pk>', login_required(EditWorkout.as_view()), name="edit_workout")
]
