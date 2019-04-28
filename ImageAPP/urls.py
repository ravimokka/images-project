from django.urls import path
from . import views

urlpatterns = [
    path('',views.LoginPage, name='LoginPage'),
    path('signup',views.Signup_page, name='Signup_page'),
    path('homepage',views.HomePage, name='Homepage'),
    path('learn_more',views.Learnmore, name='Homepage'),

]