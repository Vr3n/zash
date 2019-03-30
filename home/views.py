from django.shortcuts import render
from django.contrib.auth import authenticate
from django.forms import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.shortcuts import render_to_response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes, api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home/home.html', context)


# PROFILE API.
@never_cache
@csrf_exempt
@api_view(['GET'])
def userprofile(request):

    profile = {
        "firstname": "VIREN", "lastname": "PATEL"
    }

    if request.method == 'GET':

        return JsonResponse(profile, status=status.HTTP_200_OK)

    return JsonResponse({"msg": "Please access with GET request"}, status=status.HTTP_400_BAD_REQUEST)
