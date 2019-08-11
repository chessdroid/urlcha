
from django.urls import path, include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   
    path('', MainView.as_view()),
    path('<small_url>/', Redirector.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
