from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):
    # read permissions everyone
    if request.method in permissions.SAFE_METHODS:
      return True

    # write permissions are only allowed to author of post
    return obj.author == request.user
