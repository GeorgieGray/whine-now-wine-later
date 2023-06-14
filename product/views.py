from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate
from .forms import RegisterForm
import logging

log = logging.getLogger()

class Buy(TemplateView):
    template_name = "buy.html"

class Register(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/register"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return super(Register, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=self.request.POST['username'],password=self.request.POST['password1'])
        self.request.session['_auth_user_id'] = user.pk
        self.request.session['_auth_user_backend'] = user.backend
        return super(Register, self).form_valid(form)
