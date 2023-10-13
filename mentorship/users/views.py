from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Skill
from .serializers import CustomUserSerializer, CustomUserSerializerRead
from .permissions import UserDetailPermission

class UserList(APIView):

    def get_queryset(self):
        skills = self.request.data['skills']
        skill_ids = []
        for skill in skills:
            skill_ob = Skill.objects.get(name=skill)
            skill_ids.append((skill_ob.id))
        return skill_ids

    def get(self,request):
        if request.user.is_staff:
            users = CustomUser.objects.all()
            serializer = CustomUserSerializer(users, many=True)
            return Response(serializer.data)
        elif request.user.is_authenticated:
            users = CustomUser.objects.all().get(pk=self.request.user.id)
            data = CustomUserSerializer.get_restricted_data(users)
            serializer = CustomUserSerializer(users, data=data,many=True)
            return Response(serializer.initial_data)
        else:
            return Response(
                { "detail": "You do not have permission to perform this action." }, 
                status=status.HTTP_401_UNAUTHORIZED
            )

    def post(self, request):
        request.data['skills'] = self.get_queryset()
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UserDetail(APIView):
    permission_classes = [UserDetailPermission]
    
    def get_queryset(self):
        skills = self.request.data['skills']
        skill_ids = []
        for skill in skills:
            skill_ob = Skill.objects.get(name=skill)
            skill_ids.append((skill_ob.id))
        return skill_ids

    def get_object(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request,user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        user = self.get_object(pk)
        self.check_object_permissions(self.request,user)
        if request.user.is_staff:
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        else:
            data = CustomUserSerializer.get_restricted_data(user)
            serializer = CustomUserSerializer(user,data=data)
            return Response(serializer.initial_data)
    
    def put(self,request,pk):
        user = self.get_object(pk)
        request.data['skills'] = self.get_queryset()
        serializer = CustomUserSerializer(
            instance=user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )