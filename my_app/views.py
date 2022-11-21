from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView

from my_app.forms import ImageForm


def start_page(request, *args, **kwargs):
    return render(request, 'my_app/start_page.html', {})


def work(request, *args, **kwargs):
    return render(request, 'works/works.html', {})


def shop(request, *args, **kwargs):
    return render(request, 'shop/shop.html', {})


def about(request, *args, **kwargs):
    return render(request, 'about/about.html', {})


class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)



class ProfilePage(TemplateView) :
    template_name = "registration/profile.html"


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))
        return render(request, self.template_name)



def upload(request, *args, **kwargs):
    return render(request, 'upload/index.html', {})

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})