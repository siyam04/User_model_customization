from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404, reverse

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# def custom_login(request):
#     if request.method == 'POST':
#
#         phone_number = request.POST.get('phone_number')
#         password = request.POST.get('password2')
#
#         user = authenticate(phone_number=phone_number, password2=password)
#
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#             else:
#                 return HttpResponse("Your account was inactive.")
#         else:
#             return render(request, 'registration/login.html', {})
#     else:
#         return render(request, 'registration/login.html', {})

