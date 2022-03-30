from ast import Is
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(views.APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {"message": "Hello World"}
        return Response(content)
