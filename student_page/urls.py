from django.urls import path
from HttpRequest import request

from . import views

app_name = 'student_page'
if request.user.is_authenticated:
    urlpatterns = [
        path('<int::student_id>/swipe/', views.swiping, name='swipe'),
        path('', )
    ]
else:
    pass