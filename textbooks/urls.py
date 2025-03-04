from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='COMP346/')),
    path('<str:course_code>/', views.textbook_list, name='textbook_list'),
]