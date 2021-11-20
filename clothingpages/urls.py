from django.urls import path
from .views import indexPageView, closetPageView, editPageView

urlpatterns = [
    path('closet/', closetPageView, name='closet'),
    path('edit/', editPageView, name='edit'),
    path('', indexPageView, name='index'),
]