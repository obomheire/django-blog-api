from rest_framework.permissions import BasePermission, SAFE_METHODS


# Custom permission that allows only read-only access (GET, HEAD, OPTIONS)
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Grant permission if the HTTP method is safe (e.g., GET, HEAD, OPTIONS)
        return request.method in SAFE_METHODS


# Custom permission that allows read access to everyone, but write access only to the author of the object
class AuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow safe methods for any user
        if request.method in SAFE_METHODS:
            return True

        # Allow write permissions only to the object's author
        return request.user == obj.author
