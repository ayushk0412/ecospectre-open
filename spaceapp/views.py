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
    quiz = QuizDB_Live.objects.all()
    score = 0
    choice = [request.POST.get('1', ""),
              request.POST.get('2', ""),
              request.POST.get('3', ""),
              request.POST.get('4', ""),
              request.POST.get('5', ""),
              request.POST.get('6', ""),
              request.POST.get('7', ""),
              request.POST.get('8', ""),
              request.POST.get('9', ""),
              request.POST.get('10', ""),
              ]
    answer = []
    for i in quiz:
        answer.append(i.answer)
    for i in range(len(choice)):
        if i >= 8:
            if answer[i] == choice[i]:
                score += 6
            else:
                score += 0
        else:
            if answer[i] == choice[i]:
                score += 2
            else:
                score += 0
    print(choice)
    print(score)
    for i in range(len(choice)):
        print(choice[i])
    """current = request.user
    currentprofile = current.profile.id
    b = Profile.objects.get(pk=currentprofile)
    current_points = b.points
    print('current points', current_points)
    a = Profile.objects.filter(pk=currentprofile).update(
        points=current_points+2)"""
    currentUserName = request.user
    currentprofile = currentUserName.profile.id
    profile_obj = Profile.objects.get(pk=currentprofile)
    UpdatedScore = Profile.objects.filter(pk=currentprofile).update(
        points=(profile_obj.points)+score)
    print('score:', profile_obj.points)
    return render(request, 'quiz_result.html', {'score': score, 'choice': choice, 'quiz': quiz})


@login_required
def kids(request):
    return render(request, 'kidszone.html')


@login_required
def quiz_video(request):
    return render(request, 'quiz_video.html')


@login_required
def visual_novel_story(request):
    return render(request, 'VN/story/index.html')


@login_required
def visual_novel_quiz1(request):
    return render(request, 'VN/quiz1/index.html')


@login_required
def visual_novel_quiz2(request):
    return render(request, 'VN/quiz2/index.html')


def about(request):
    return render(request, 'about.html')


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["fname", "lname", "DOB", "ph_no", "desc", "myimg", "child_name"]
