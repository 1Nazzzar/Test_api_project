from django.urls import path
from .views import    *

urlpatterns = [
    path('test/', ProductView.as_view(), name='test')
]