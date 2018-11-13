from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class main(TemplateView):
    template_name = "main.html"
