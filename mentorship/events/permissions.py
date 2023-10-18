from rest_framework import permissions

class CustomIsAdmin(permissions.BasePermission):
  def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            (request.user and
            request.user.is_authenticated and
            request.user.is_staff)
        )
  
class IsSuperAdmin(permissions.BasePermission):
  def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            (request.user and
            request.user.is_authenticated and
            request.user.is_superuser and 
            request.user.is_staff)
        )

class IsEventMentor(permissions.BasePermission):
      def has_permission(self, request, view, obj):
        return bool(request.method in permissions.SAFE_METHODS or obj.mentor_id == request.user)
