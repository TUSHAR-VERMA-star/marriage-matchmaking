from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from django.db.models import Q

class UserListCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def get(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserMatchAPIView(APIView):
    # def get(self, request, pk):
    #     user = User.objects.get(pk=pk)
    #     if not user:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     matches = User.objects.filter(
    #         gender=user.gender,
    #         city=user.city,
    #         interests=user.interests
    #     ).exclude(pk=pk)
    #     serializer = UserSerializer(matches, many=True)
    #     return Response(serializer.data)
    
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Extract query parameters
        city = request.query_params.get('city', user.city)
        interests = request.query_params.get('interests', user.interests)
        gender = request.query_params.get('gender', user.gender)
        min_age = request.query_params.get('min_age', user.age - 5)
        max_age = request.query_params.get('max_age', user.age + 5)

        # Filter users based on query parameters
        matches = User.objects.filter(
            Q(city=city) &
            Q(interests__icontains=interests) &
            Q(gender=gender) &
            Q(age__gte=min_age) &
            Q(age__lte=max_age)
        ).exclude(pk=pk)

        serializer = UserSerializer(matches, many=True)
        return Response(serializer.data)
