from rest_framework import permissions


class IsRoleAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.
                user.is_admin or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated and request.
                user.is_admin or request.user.is_superuser)


class IsRoleModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_moderator)

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated and request.user.is_moderator)


class IsRoleUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.
                user.is_user or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.
                SAFE_METHODS or request.user == obj.author)


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

        # return obj.author == request.user
