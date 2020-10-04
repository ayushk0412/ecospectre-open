from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.quiz, name="quiz"),
    path('kids-zone/', views.kids, name="kids-zone"),
    path('quiz_video/', views.quiz_video, name="quiz_video"),
    path('quiz_result/', views.quiz_score, name="quiz_score"),
    path('visual_novel-story/', views.visual_novel_story,
         name="visual_novel_story"),
    path('visual_novel-quiz1/', views.visual_novel_quiz1,
         name="visual_novel_quiz1"),
    path('visual_novel-quiz2/', views.visual_novel_quiz2,
         name="visual_novel_quiz2"),
    path('visual_novel-menu/', views.visual_novel_menu, name="visual_novel_menu"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('contact-us/', views.contactus, name="contactus"),
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/")),
]
