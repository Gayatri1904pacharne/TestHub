from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('signup/',views.signup),
    path('login/',views.login),
    path('dashboard/',views.dashboard),
    path('logout/',views.logout),
    path('search/',views.search),
    path('nextQuestion/',views.nextQuestion),
    path('previousQuestion/',views.previousQuestion),
    path('indexfortest/',views.indexfortest),
    path('endexam/',views.endexam),
    path('viewscore/',views.viewscore),
    path("question/",views.question)
    
]