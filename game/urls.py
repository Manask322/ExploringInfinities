from django.urls import path

# from .views import HomePageView
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('game/',views.game,name='game'),
    path('login/',views.login,name='login'),
    path('start_game',views.start_game,name='start_game')
    # path('', views.HomePageView.as_view(), name='home'),
]