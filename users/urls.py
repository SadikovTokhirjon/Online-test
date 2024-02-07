from django.urls import path
from users.views import Registertion,LoginView,ProfileView,LogoutView,UserUpadeView
from django.contrib.auth import views as auth_views
app_name='users'
urlpatterns=[
    path('singup/',Registertion.as_view(),name='singup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/edit',UserUpadeView.as_view(),name='profile-edit'),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='passport_set'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name = 'password_reset_complete'),

]