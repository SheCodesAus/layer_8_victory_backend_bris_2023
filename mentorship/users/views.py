from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Skill
from .serializers import CustomUserSerializer, CustomUserSerializerRead

class UserList(APIView):

    def get_queryset(self):
        skills = self.request.data['skills']
        skill_ids = []
        for skill in skills:
            skill_ob = Skill.objects.get(name=skill)
            skill_ids.append((skill_ob.id))
        return skill_ids

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializerRead(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['skills'] = self.get_queryset()
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UserDetail(APIView):
    def get_queryset(self):
        skills = self.request.data['skills']
        skill_ids = []
        for skill in skills:
            skill_ob = Skill.objects.get(name=skill)
            skill_ids.append((skill_ob.id))
        return skill_ids

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializerRead(user)
        return Response(serializer.data)
    
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