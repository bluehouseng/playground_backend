from django.shortcuts import render
from django.http.response import JsonResponse 
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from rest_framework.decorators import api_view

from .models import User 
from .serializers import UserSerializer

@api_view(['GET', 'POST', 'DELETE'])
def get_user_list(request):
    if request.method == 'GET':
        users = User.objects.all()

        fullname = request.query_params.get('fullname', None)
        if fullname is not None:
            users = users.filter(fullname__icontains=fullname)
        
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user_count = User.objects.all().delete()
        return JsonResponse({'message': 'f"{} Users were deleted successfully!!!" user_count[0]'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def get_user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message':'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user, many=False)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'user was deleted successfully!!!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def active_users(request):
    users = User.objects.filter(active=True)

    if request.method == 'GET':
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)