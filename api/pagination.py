from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomNumberPagination(PageNumberPagination):
    page_size = 10
    
    def get_paginated_response(self, data):
        return Response({
            'links': 
                {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
            'total_objects_count': self.page.paginator.count,
            'total_pages_count': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'results': data
        })