from rest_framework.views import APIView
from rest_framework.response import Response


class Auth(APIView):

    def post(self, request):
        return Response("hello rest framework")
