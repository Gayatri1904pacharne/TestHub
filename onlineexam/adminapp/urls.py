from django.urls import path
from . import views
 

urlpatterns=[

    path("addquestion/",views.addquestion),
    path("updatequestion/",views.updatequestion),
    path("getquestion/",views.getquestion),
    path("deletequestion/",views.deletequestion),
    path("marks_analysis/",views.marks_analysis),
    # path("get/",views.get)
    
]