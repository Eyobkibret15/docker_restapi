from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from .models import country, city, hotel
from .serializer import countryserializer, cityserializer, hotelserializer
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework import status
from rest_framework.response import Response

#
# @api_view(['GET'])
# # @authentication_classes([SessionAuthentication, BasicAuthentication])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def example_view(request, format=None):
#     content = {
#         'user': str(request.user),  # `django.contrib.auth.User` instance.
#         'auth': str(request.auth),  # None
#     }
#     return Response(content)
#

from django.views.decorators.csrf import csrf_exempt


@api_view(["GET","POST"])
@csrf_exempt
def home(request):
    if request.method == "GET":
        data = country.objects.all()
        serializer = countryserializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = countryserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# @api_view(["GET","POST"])
# def values(request):
#     if request.method == "GET":
#         data = value.objects.all()
#         serializer = valueserializers(data, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif  request.method == "POST":
#         serializer = valueserializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

@api_view(["GET","PUT","POST"])
def edit(request,pk):
    if request.method == "POST":
        serializer = countryserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        pro = country.objects.get(id=pk)
        serializer = countryserializer(pro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data , status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        pro = country.objects.get(id=pk)
        serializer = countryserializer(pro)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(["GET"])
def test(request):
    if request.method == "GET":
        data = country.objects.all()
        serializer = countryserializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#
# @api_view(['GET', 'PUT', 'DELETE',"POST"])
# def apply(request, pk):
#
#     """
#     Retrieve, update or delete a code snippet.
#     """
#
#     try:
#         pro = product.objects.get(pk=pk)
#     except product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = productserializers(pro)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = productserializers(pro, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         pro.delete()
#         return JsonResponse(status=status.HTTP_204_NO_CONTENT)
#