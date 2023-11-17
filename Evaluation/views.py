from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Evaluation
from rest_framework import status
from .serializers import EvaluationSerializer
from django.utils import timezone
from Client.models import ClientUser
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

class GetClientEvaluations(ListAPIView):
    serializer_class = EvaluationSerializer


    def get_queryset(self):
        # Fetch evaluations for the authenticated client based on the provided token
        token = self.request.query_params.get('token', None)

        if token:
            print(f'Token: {token}')

            user = ClientUser.objects.get(token=token)
            print(f'User Role: {user.role}')

            if user.role == 'client':
                return Evaluation.objects.filter(client_id=user)
            elif user.role == 'admin':
                return Evaluation.objects.all()
            else:
                return Evaluation.objects.filter(evaluator_id=user)

        # If the token is not provided, return an empty queryset or handle it as per your needs
        return Evaluation.objects.none()


class AddEvaluations(generics.CreateAPIView):
    serializer_class = EvaluationSerializer

    def create(self, request, *args, **kwargs):
        # Extract token from query parameters
        data = request.data
        token = data.get('token')

        if not token:
            return Response({'error': 'Token is required in query parameters'}, status=status.HTTP_400_BAD_REQUEST)

        # Assuming you have the token in the request, get the user
        try:
            user = ClientUser.objects.get(token=token)
            evaluator_id = user.id
        except ClientUser.DoesNotExist:
            return Response({'error': 'User not found for the given token'}, status=status.HTTP_404_NOT_FOUND)

        # Add evaluator_id and etat to data
        mutable_data = dict(data)
        mutable_data['evaluator_id'] = evaluator_id
        mutable_data['etat'] = '0'
        
        if 'title' not in mutable_data or not mutable_data['title']:
            return Response({'error': 'Title is required.'}, status=status.HTTP_400_BAD_REQUEST)

        if 'post' not in mutable_data or not mutable_data['post']:
            return Response({'error': 'Post is required.'}, status=status.HTTP_400_BAD_REQUEST)

        if 'notes' not in mutable_data or not mutable_data['notes']:
            return Response({'error': 'Notes are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize the modified data
        serializer = EvaluationSerializer(data=mutable_data)

        if serializer.is_valid():
            # Save the evaluation
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
