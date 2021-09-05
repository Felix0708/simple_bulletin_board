from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('main/signup/', views.signup, name="signup"),
    # path('signup2/', views.signup2, name="signup2"),
    path('main/login/', views.login, name="login"),
    path('main/logout/', views.logout, name="logout"),
    # path('main/', views.main, name="main"),
]
