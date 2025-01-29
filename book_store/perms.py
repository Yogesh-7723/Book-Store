from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method == "GET" :
            return True
        elif request.user.is_authenticated:
            if request.user.user_type == "author" and request.method in ["POST","PUT","DELETE"]:
                return True
        else:
            return False