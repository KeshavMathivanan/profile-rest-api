from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Keshav is a Programmer as well as Developer',
            'Is similar to traditional django View',
            'Gives you the most control over application logic',
            'Is mapped manaually to URLs',
        ]

        return  Response({'message': 'Hello!', 'an_apiview': an_apiview})