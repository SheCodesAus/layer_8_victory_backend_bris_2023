from rest_framework import permissions
from users.models import CustomUser

class CustomIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )

class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or (
                request.user
                and request.user.is_authenticated
                and request.user.is_superuser
                and request.user.is_staff
            )
        )

class EventMentorUpdate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(obj.mentor_id == request.user or request.user.is_staff)

class IsValidMentor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            mentor_id_switch = CustomUser.objects.get(id=request.data['mentor_id'])
        else:
            mentor_id_switch = request.user
        user = CustomUser.objects.get(id=mentor_id_switch.id)
        if request.user.is_authenticated and user.onboarding_status == "Ready":
            return True
        return False