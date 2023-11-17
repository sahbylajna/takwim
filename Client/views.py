# client_api/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import ClientUser
from .serializers import ClientUserSerializer
from django.core.exceptions import ObjectDoesNotExist
import secrets
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from django.core.files.storage import default_storage

import base64
from django.core.files.base import ContentFile
class ClientUserLogin(generics.CreateAPIView):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserSerializer

    def create(self, request, *args, **kwargs):
        phone = request.data.get('phone', None)
        password = request.data.get('password', None)

        # if not phone:
        #     return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
        # if not password:
        #     return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            client_user = ClientUser.objects.get(phone=phone,password=password)
        # return Response({'token': client_user.id}, status=status.HTTP_200_OK)

            token = secrets.token_hex(16)
            client_user.token = token
            client_user.save()
            data = {'token': token, 'id': str(client_user.id),'role':client_user.role}

            # return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            data = {'token': '', 'id': '','role':''}

        return Response(data, status=status.HTTP_200_OK)
class regesterClient(generics.CreateAPIView):
    serializer_class = ClientUserSerializer

    def create(self, request, *args, **kwargs):
        # Extract token from query parameters
        data = JSONParser().parse(request)
        base64_string = data.get('singater', '')
        uid = data.get('uid', '')
        # print(f'{data}')
        # Decode base64 image data

        # Decode the base64 string
        image_data = base64.b64decode(base64_string)
        print(f'{image_data}')
        # Create a ContentFile from the binary image data
        # image_file = ContentFile(image_data, name="your_image.png")
        # image_binary = base64.b64decode(image_data)
        #
        # # Save the image with a specific name
        image_name = 'images/'+uid+'.png'
        image_path = default_storage.save(image_name, ContentFile(image_data))

        print(f'{data}')
        mutable_data = dict(data)
        mutable_data['singater'] = image_name
        print(f'{mutable_data}')
        print(f'{image_name}')
        serializer = ClientUserSerializer(data=mutable_data)

        if serializer.is_valid():
            # Save the evaluation
            serializer.save()
            data = {'message': 'ok', 'errors': ''}
            return Response(data, status=status.HTTP_200_OK)




            # return Response(data, status=status.HTTP_200_OK)

        data = {'message': '', 'errors': 'ok'}
        return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getClient(generics.CreateAPIView):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserSerializer

    def create(self, request, *args, **kwargs):
        token = request.data.get('token', None)

        # if not phone:
        #     return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
        # if not password:
        #     return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            client_user = ClientUser.objects.get(token=token)
        # return Response({'token': client_user.id}, status=status.HTTP_200_OK)
            serializer = ClientUserSerializer(client_user)
              # Assuming you have a serializer defined for ClientUser
            return Response(serializer.data, status=status.HTTP_200_OK)



            # return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return Response({}, status=status.HTTP_200_OK)

class GetClientList(ListAPIView):
    serializer_class = ClientUserSerializer
    def get_queryset(self):
        # Fetch evaluations for the authenticated client based on the provided token
        token = self.request.query_params.get('token', None)
        try:
            client_user = ClientUser.objects.get(token=token)
            if client_user.role == 'admin':
                return ClientUser.objects.all().exclude(id=client_user.id)


            else:
                return ClientUser.objects.filter(supvaser_id=user).exclude(id__in=client_user.id)# Assuming you have a serializer defined for ClientUser


        except ObjectDoesNotExist as e:
            return Response({}, status=status.HTTP_200_OK)
