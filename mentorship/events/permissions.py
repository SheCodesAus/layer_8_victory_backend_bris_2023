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
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_superuser and 
            request.user.is_staff
        )

class IsValidMentor(permissions.BasePermission):
    def has_permission(self, request, view):
        mentor_id = request.data['mentor_id']
        user = CustomUser.objects.get(id=mentor_id)
        return bool(
            request.user.is_authenticated and
            user.onboarding_status == "Ready"
        )