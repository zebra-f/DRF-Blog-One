from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CustomUserSerializer


class CustomUserCreate(APIView):
    
    permission_classes = [AllowAny]

    
    def post(self, request):
        
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            if user:
                json = serializer.data

                return Response(json, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenView(APIView):

    permission_classes = [AllowAny]


    def post(self, request):

        try:
            refresh_token = request.data['refresh']
            refresh_token = RefreshToken(refresh_token)
            refresh_token.blacklist()

            return Response(status=status.HTTP_200_OK) 

        except:

            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    



