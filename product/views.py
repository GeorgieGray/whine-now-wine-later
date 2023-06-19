from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product, Workout
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import ChoiceWidget
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import IntegrityError
from django.forms.forms import NON_FIELD_ERRORS 

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
        form.fields['type'].widget.attrs['class'] = 'form-control'
        form.fields['time'].widget.attrs['class'] = 'form-control mb-3'
        form.fields['day'].widget = AdminDateWidget(attrs={'type': 'date', 'class': 'form-control mb-3' })

        return form

    def form_valid(self, form):
        workout = form.save(commit=False)
        workout.user = self.request.user
        try:
            return super(CreateWorkout, self).form_valid(form)
        except IntegrityError:
            form.add_error(NON_FIELD_ERRORS, "You've already got plans at this time/day combination")
            return self.form_invalid(form)

class EditWorkout(UserPassesTestMixin, UpdateView):
    template_name="workout_form.html"
    model = Workout
    fields = ["type", "time", "day"]
    success_url="/workouts"

    def form_valid(self, form):
        try:
            return super(EditWorkout, self).form_valid(form)
        except IntegrityError:
            form.add_error(NON_FIELD_ERRORS, "You've already got plans at this time/day combination")
            return self.form_invalid(form)

    def test_func(self):
        workout = Workout.objects.get(pk=self.kwargs['pk'])
        return self.request.user.id == workout.user.id

    def get_form(self, form_class=None):
        form = super(EditWorkout, self).get_form(form_class)
        form.fields['type'].widget.attrs['class'] = 'form-control'
        form.fields['time'].widget.attrs['class'] = 'form-control'
        form.fields['day'].widget = AdminDateWidget(attrs={'type': 'date', 'class': 'form-control' })

        return form

class DeleteWorkout(UserPassesTestMixin, DeleteView):
    def test_func(self):
        workout = Workout.objects.get(pk=self.kwargs['pk'])
        return self.request.user.id == workout.user.id
    template_name="workout_delete.html"
    model = Workout
    success_url="/workouts"