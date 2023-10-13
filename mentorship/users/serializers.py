from rest_framework import serializers
from .models import CustomUser, Skill

class SkillSerilalizer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ("name",)

class CustomUserSerializerRead(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    skills = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}, 'email' : {'required': True}}


    def get_skills(self, obj):
        skills = Skill.objects.filter(user_profiles=obj.id)
        return SkillSerilalizer(skills, many=True).data


    def get_restricted_data(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'mobile': self.mobile,
            'location': self.location,
            'cv': self.cv,
            'skills': self.skills,
            'social_account': self.social_account,
            'linkedin_account': self.linkedin_account,
            'rank': self.rank,
            'date_joined': self.date_joined
        }

class CustomUserSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'first_name', 'last_name', 'email',
                  'mobile', 'location', 'cv', 'skills', 'social_account', 'linkedin_account','user',)
        extra_kwargs = {'password': {'write_only': True}, 'email' : {'required': True}}


    def validate_username(self, value):
        if CustomUser.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value
    
    def create(self,validated_data):
        user = CustomUser.objects.create_user(username=validated_data.get('username'),
                                              password=validated_data.get('password'),
                                              first_name=validated_data.get('first_name'),
                                              last_name=validated_data.get('last_name'),
                                              email=validated_data.get('email'),
                                              mobile=validated_data.get('mobile'),
                                              location=validated_data.get('location'),
                                              cv=validated_data.get('cv'),
                                              social_account=validated_data.get('social_account'),
                                              linkedin_account=validated_data.get('linkedin_account')
                                              )
        for skillset in validated_data.get('skills'):
            user.skills.add(skillset.id)
        return user


    def update(self,instance,validated_data):


        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile',instance.mobile)
        instance.location = validated_data.get('location',instance.location)
        instance.cv = validated_data.get('cv',instance.cv)
        instance.social_account = validated_data.get('social_account',instance.social_account)
        instance.linkedin_account = validated_data.get('linkedin_account',instance.linkedin_account)

        instance.skills.clear()

        for skillset in validated_data.get('skills'):
            instance.skills.add(skillset.id)

        instance.save()
        return instance

    def get_restricted_data(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'mobile': self.mobile,
            'location': self.location,
            'cv': self.cv,
            'skills': self.skills,
            'social_account': self.social_account,
            'linkedin_account': self.linkedin_account,
            'rank': self.rank,
            'date_joined': self.date_joined
        }


    