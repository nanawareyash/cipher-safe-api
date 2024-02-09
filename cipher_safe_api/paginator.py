import math

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CipherSafePagination(PageNumberPagination):
    queryset = None

    def paginate_queryset(self, queryset, request, view=None):
        self.queryset = queryset
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        count = len(data)
        page = self.request.GET.get("page")
        page = int(page) if page is not None else 1
        total_count = self.queryset.count()
        total_pages = math.ceil(total_count / self.page_size)
        return Response(
            {
                "count": count,
                "page": page,
                "total_count": total_count,
                "total_pages": total_pages,
                "data": data,
            }
        )
