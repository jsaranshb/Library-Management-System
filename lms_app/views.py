from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BookCategory, BookDetails
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import BookDetailsSerializer, BookCategorySerializer, StudentViewSerializer, AdminSignupSerializer

# Create your views here.

class StudentView(APIView):
    serializer_class = StudentViewSerializer
    def get(self, request):
        try:
            queryset = BookDetails.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({'details' : 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        

class AdminSignupView(viewsets.ModelViewSet):
    serializer_class = AdminSignupSerializer
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    
    
class AdminLoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class BookCategoryView(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = BookCategorySerializer
    queryset = BookCategory.objects.filter(status=True)
    
    
class AdminBooksView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]
    serializer_class = BookDetailsSerializer
    queryset = BookDetails.objects.all()
    
    
