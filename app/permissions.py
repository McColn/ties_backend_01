# yourapp/permissions.py
from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow superusers (admin) to perform any action
        if request.user and request.user.is_superuser:
            return True

        # Allow users to perform actions on their own profile
        return obj == request.user
