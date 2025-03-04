from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='textbooks/')),
    path('textbooks/', include('textbooks.urls')),
]