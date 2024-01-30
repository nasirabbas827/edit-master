from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Your other URL patterns
    path('register/', views.user_register, name='user_register'),
    path('', views.user_login, name='user_login'),
    path('dashboard/', login_required(views.dashboard), name='dashboard'),  # Add this line
    path('update_profile/', login_required(views.update_profile), name='update_profile'),
    path('change_password/', login_required(views.change_password), name='change_password'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', views.voter_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
