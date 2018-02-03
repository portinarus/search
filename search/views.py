# -*- coding: utf-8 -*-
"""
This module contains all endpoints for dealing with search
"""

from rest_framework.response import Response
from rest_framework.views import APIView


class SearchView(APIView):
    """
    This class deals with search
    """

    def get(self, request):
        """
        Searches elastic.

        :param request: the request object.
        :type request: :py:class:`rest_framework.request.Request`
        """

        return Response({'test': 'test'})
