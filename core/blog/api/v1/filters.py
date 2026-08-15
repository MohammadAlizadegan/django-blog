from rest_framework import filters


class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    add IsOwnerFilterBackend to filter_backends / Now is disabled.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(author__user=request.user)

    #We can add and create longrange of filters easily with GPT !