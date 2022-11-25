from django.urls import path
from .views import RegisterUserView, DetailedUserProfileView,UpdateUserProfileView,UserEditView, PassWordChangingView,CreateUserProfileView
from django.contrib.auth import views as auth_views


app_name = 'member'
urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('create_new_profile/', CreateUserProfileView.as_view(), name='create_profile'),
    path('password/', PassWordChangingView.as_view(), ),
    path('profile/<int:pk>/', DetailedUserProfileView.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', UpdateUserProfileView.as_view(), name='profile_detail_update'),
]