from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product, Workout
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin

class Buy(ListView):
    template_name = "buy.html"
    model = Product

class Workouts(ListView):
    template_name = "workouts.html"
    model = Workout

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

class CreateWorkout(CreateView):
    template_name="workout_form.html"
    model = Workout
    fields = ["type", "time", "day"]
    success_url="/workouts"

    def get_form(self, form_class=None):
        form = super(CreateWorkout, self).get_form(form_class)
        form.fields['day'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        workout = form.save(commit=False)
        workout.user = self.request.user
        return super(CreateWorkout, self).form_valid(form)

class EditWorkout(UserPassesTestMixin, UpdateView):
    def test_func(self):
        workout = Workout.objects.get(pk=self.kwargs['pk'])
        return self.request.user.id == workout.user.id
    template_name="workout_form.html"
    model = Workout
    fields = ["type", "time", "day"]
    success_url="/workouts"

class DeleteWorkout(UserPassesTestMixin, DeleteView):
    def test_func(self):
        workout = Workout.objects.get(pk=self.kwargs['pk'])
        return self.request.user.id == workout.user.id
    template_name="workout_delete.html"
    model = Workout
    success_url="/workouts"