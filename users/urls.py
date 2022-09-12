from django.urls import path

from .views import CustomUserCreate, BlacklistTokenView

app_name = 'users'

# api/user/
urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='user_register'),
    path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist'),
]
