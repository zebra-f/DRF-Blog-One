from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostUserUpdateDeletePermission(BasePermission):
    message = "Editing posts is allowed only by the author."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.author