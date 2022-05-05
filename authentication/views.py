from django.shortcuts import render, redirect
from django.conf import settings
from authentication.forms import SignupForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View

def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

""" class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request,
        self.template_name,
        {'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        return render(request,
        self.template_name,
        {'form': form, 'message': message}) """
