from django.shortcuts import render, redirect
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from .models import QuizDB_Live, Profile
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        currentUserName = request.user
        currentprofile = currentUserName.profile.id
        profile = Profile.objects.all().filter(pk=currentprofile)
        return render(request, "index.html", {'profile': profile})
    else:
        return render(request, "index.html")

    """currentUserName = request.user
    if currentUserName == 'AnonymousUser':
        return render(request, "index.html")
    else:
        currentprofile = currentUserName.profile.id
        profile = Profile.objects.all().filter(pk=currentprofile)
        return render(request, "index.html", {'profile': profile})"""


@login_required
def quiz(request):

    quiz = QuizDB_Live.objects.all()
    return render(request, "quiz.html", {'quiz': quiz})


@login_required
def visual_novel_menu(request):
    total_points = 0
    currentUserName = request.user
    currentprofile = currentUserName.profile.id
    profile = Profile.objects.all().filter(pk=currentprofile)
    for i in profile:
        total_points = i.points
    print("--", total_points)
    if total_points >= 16:
        return render(request, "visualnovel.html")
    else:
        return render(request, "lockvn.html", {'profile': profile})


@login_required
def leaderboard(request):
    return render(request, "leaderboard.html")


@login_required
def contactus(request):
    return render(request, "contact us.html")


@login_required
def quiz_score(request):
    
   #TO GET THE FULL CODE, SEND ME A MAIL AT ayushk0412@gmail.com, WITH THE SUBJECT "CODE REQUIRED"


def about(request):
    return render(request, 'about.html')


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["fname", "lname", "DOB", "ph_no", "desc", "myimg", "child_name"]
