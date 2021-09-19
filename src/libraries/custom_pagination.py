from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(
            {
                'data': data,
                'meta': {
                    'search': self.request.GET.get('search') or '',
                    'ordering': self.request.GET.get(
                        'ordering'
                    ) or '-updated_at',
                    'page': self.page.number,
                    'page_size': self.request.GET.get(
                        'page_size'
                    ) or self.page_size,
                    'page_count': self.page.paginator.num_pages,
                }
            }
        )
