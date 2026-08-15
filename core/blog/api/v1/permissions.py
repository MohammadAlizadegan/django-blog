from rest_framework import permissions


class IsAuthorEditObjectOrReadOnly(permissions.BasePermission):
    '''Object-level permission to only allow authors to edit an object.'''
    def has_object_permission(self, request, view, obj):
        #Read permissions are allowed for list and retrieve methods.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author.user == request.user