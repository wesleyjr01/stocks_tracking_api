from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    https://www.django-rest-framework.org/api-guide/permissions/#isadminuser
    """

    def has_permission(self, request, view):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # # Write permissions are only allowed to users which user.is_staff is True
        return request.user.is_staff == True