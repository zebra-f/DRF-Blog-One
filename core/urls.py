"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    
    # api
    path('api/', include('blog_api.urls', namespace='blog_api')),

    # api DRF GUI auth (api-auth/login/, api-auth/logout)
    path('api-auth/', include('rest_framework.urls', namespace='blog_api_auth')),
    # api JWT auth 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/user/', include('users.urls', namespace='users')),
    
    # OpenAPI/CoreAPI documentation/schema
    path('openapi-schema', get_schema_view(
        title='Django-Blog-One',
        description='Django-Blog-One API',
        version='0.0.1',
    ), name='openapi-schema'),
    path('docs/', include_docs_urls(title='Django-Blog-One'))
]
