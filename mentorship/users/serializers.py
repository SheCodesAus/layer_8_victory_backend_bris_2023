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

class CustomUserSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = CustomUser
        fields = (
            'username', 
            'password', 
            'first_name', 
            'last_name', 
            'email', 
            'mobile', 
            'location', 
            'github_profile', 
            'skills', 
            'social_account', 
            'linkedin_account',
            'user'
        )
        extra_kwargs = {'password': {'write_only': True}, 'email' : {'required': True}}


    def validate_username(self, value):
        if CustomUser.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value
    
    def create(self,validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            mobile=validated_data.get('mobile'),
            location=validated_data.get('location'),
            github_profile=validated_data.get('github_profile'),
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
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.location = validated_data.get('location', instance.location)
        instance.github_profile = validated_data.get('github_profile', instance.github_profile)
        instance.social_account = validated_data.get('social_account', instance.social_account)
        instance.linkedin_account = validated_data.get('linkedin_account', instance.linkedin_account)
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
            'github_profile': self.github_profile,
            'skills': SkillSerilalizer(Skill.objects.filter(user_profiles=self.id), many=True).data,
            'social_account': self.social_account,
            'linkedin_account': self.linkedin_account,
            'rank': self.rank,
            'date_joined': self.date_joined
        }


class CustomStaffSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}, 'email' : {'required': True}}

    def create(self,validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            mobile=validated_data.get('mobile'),
            location=validated_data.get('location'),
            github_profile=validated_data.get('github_profile'),
            social_account=validated_data.get('social_account'),
            linkedin_account=validated_data.get('linkedin_account'),
            onboarding_status=validated_data.get('onboarding_status'),
            rank=validated_data.get('rank'),
            private_notes=validated_data.get('private_notes')
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
        instance.location = validated_data.get('location', instance.location)
        instance.github_profile = validated_data.get('github_profile', instance.github_profile)
        instance.social_account = validated_data.get('social_account', instance.social_account)
        instance.linkedin_account = validated_data.get('linkedin_account', instance.linkedin_account)
        instance.is_superuser = validated_data.get('is_superuser',instance.is_superuser)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.rank = validated_data.get('rank', instance.rank)
        instance.private_notes = validated_data.get('private_notes', instance.private_notes)
        instance.onboarding_status = validated_data.get('onboarding_status', instance.onboarding_status)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.skills.clear()

        for skillset in validated_data.get('skills'):
            instance.skills.add(skillset.id)

        instance.save()
        return instance