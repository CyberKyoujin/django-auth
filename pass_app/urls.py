from django.urls import path
from . import views
app_name = 'pass_app'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]
