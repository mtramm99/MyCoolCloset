from django.urls import path
from .views import indexPageView, closetPageView, editPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('closet/', closetPageView, name='closet'),
    path('edit/', editPageView, name='edit'),
]