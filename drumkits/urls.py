from django.urls import path
from .views import DrumkitListView

urlpatterns = [
    path('', DrumkitListView.as_view(), name='home'),
]