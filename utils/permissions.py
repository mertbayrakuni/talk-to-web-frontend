from rest_framework import permissions

from utils.constants import SUPER_ADMIN, CALL_CENTER, OPEN, SAHA_PERSONELI, ADVISOR


class PermissionPolicyMixin:

    def check_permissions(self, request):
        try:
            # This line is heavily inspired from `APIView.dispatch`.
            # It returns the method associated with an endpoint.
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None

        if (
                handler
                and self.permission_classes_per_method
                and self.permission_classes_per_method.get(handler.__name__)
        ):
            self.permission_classes = self.permission_classes_per_method.get(handler.__name__)

        super().check_permissions(request)


class IsSuperuser(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        if request.user.is_superuser or request.user.role == SUPER_ADMIN:
            return True

    def has_object_permission(self, request, view, obj):

        if request.user.is_authenticated and (request.user.is_superuser or request.user.role == SUPER_ADMIN or
                                              request.method in permissions.SAFE_METHODS or
                                              (request.user.is_staff and request.method not in self.edit_methods)):
            return True

        return False


class IsCallCenter(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        if request.user.is_superuser or request.user.role in [SUPER_ADMIN, CALL_CENTER]:
            return True

    def has_object_permission(self, request, view, obj):

        if request.user.is_authenticated and (request.user.is_superuser or
                                              request.user.role == SUPER_ADMIN or
                                              request.method in permissions.SAFE_METHODS or
                                              request.user.role == CALL_CENTER):
            return True

        return False


class IsAdvisor(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        if request.user.is_superuser or request.user.role in [SUPER_ADMIN, ADVISOR]:
            return True

    def has_object_permission(self, request, view, obj):

        if request.user.is_authenticated and (request.user.is_superuser or
                                              request.user.role == SUPER_ADMIN or
                                              request.method in permissions.SAFE_METHODS or
                                              request.user.role == ADVISOR):
            return True

        return False

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj and (obj.__class__.__name__ == "User" and obj == request.user) or \
                (hasattr(obj, 'created_by') and obj.created_by == request.user) or \
                (hasattr(obj, 'broker') and obj.broker.user == request.user) or \
                (hasattr(obj, 'owner') and obj.owner == request.user):
            return True
        return False


class IsOpen(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj and obj.__class__.__name__ == "User" and request.user.role == OPEN:
            return True
        return False


class IsBroker(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj and obj.__class__.__name__ == "User" and request.user.role == OPEN:
            return True
        return False