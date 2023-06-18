from django.views.generic import ListView, CreateView, UpdateView
from .models import Product, Workout

class Buy(ListView):
    template_name = "buy.html"
    model = Product

class Workouts(ListView):
    template_name = "workouts.html"
    model = Workout

class CreateWorkout(CreateView):
    model = Workout
    fields = ["type", "time", "date"]

class EditWorkout(UpdateView):
    model = Workout
    fields = ["type", "time", "date"]