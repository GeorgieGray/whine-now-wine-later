from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm
from django.shortcuts import redirect

class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('root')
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            form.clean()
            user = authenticate(
                request, 
                username=form.cleaned_data["username"], 
                password=form.cleaned_data["password"],
            )
            login(request, user)
            return redirect("root")
        else:
            print(form.errors)
            print(form.cleaned_data)
            
            return redirect("login")

    
class Register(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/register"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('root')
        else:
            return super(Register, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        
        return super(Register, self).form_valid(form)