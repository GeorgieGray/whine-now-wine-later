from django.views.generic import CreateView, DeleteView, TemplateView, FormView
from .models import Subscriber
from django.shortcuts import redirect
from .forms import SubscriberForm

# Create your views here.
class Join(CreateView):
    template_name="newsletter_create.html"
    model = Subscriber
    fields = ["email"]
    success_url="/mail/thanks"

    def get_form(self, form_class=None):
        form = super(Join, self).get_form(form_class)
        form.fields['email'].widget.attrs['class'] = 'form-control'

        return form

def get_subscriber_or_none(email):
    try:
        return Subscriber.objects.get(pk=email)
    except Subscriber.DoesNotExist:
        return None

class Unsubscribe(FormView):
    template_name="newsletter_unsub.html"
    fields = ["email"]
    form_class = SubscriberForm

    def get_form(self, form_class=None):
        form = super(Unsubscribe, self).get_form(form_class)
        form.fields['email'].widget.attrs['class'] = 'form-control'

        return form

    def form_valid(self, form):
        sub = get_subscriber_or_none(form.cleaned_data['email'])
        
        if sub != None:
            sub.delete()

        return redirect("bye_news")

class Bye(TemplateView):
    template_name="newsletter_bye.html"

class Thanks(TemplateView):
    template_name="newsletter_welcome.html"