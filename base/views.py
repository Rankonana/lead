from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
import random
import string
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Max


def home(request):
    return render(request, 'base/home.html')