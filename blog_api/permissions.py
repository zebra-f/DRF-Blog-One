from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import AnonymousUser


class PostUserUpdateDeleteCreatePermission(BasePermission):
    '''Same as DRF's IsAuthenticatedOrReadOnly permission (?).'''
    message = "Editing posts is allowed only by the author."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.author

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        if request.method == 'POST':
            if request.user == AnonymousUser():
                return False
            
            return True

    

    