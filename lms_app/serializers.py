from rest_framework import serializers
from .models import BookCategory, BookDetails
from django.contrib.auth.models import User

class StudentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = ('id', 'name', 'author')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }
        
    def create(self, validated_data):
        print(validated_data)
       
        user = User.objects.create(
            username = validated_data['username'],
            email =  validated_data['email'],            
        )
        if validated_data.get('password'):
           user.set_password(validated_data['password'])
           user.save()
           return validated_data
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return validated_data
    
    
class AdminSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }

    def create(self,validatedData):
        user = User.objects.create(
            username = validatedData['username'],
            email = validatedData['email'],
        )
        user.set_password(validatedData['password'])
        user.save() 
        return user 


class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField()


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'
        
        
class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = '__all__'
        depth = 1
