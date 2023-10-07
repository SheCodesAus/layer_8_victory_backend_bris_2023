from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):
  def has_object_permission (self,request,view,obj):
    return bool(request.user.is_superuser and request.user.is_staff)