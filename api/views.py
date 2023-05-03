from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import rest_framework.status as status

def index(request):
    data = {
        "message": "Hello, world. You're at the api index.",
        "status": 200
    }
    return JsonResponse(data, safe=False, status=status.HTTP_200_OK)