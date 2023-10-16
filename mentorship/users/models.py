from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=10)
    location = models.CharField(max_length=200)
    cv = models.URLField(max_length=200)
    skills = models.ManyToManyField(
        to='users.Skill',  # use a string in the format `app_name.model_name` to reference models to avoid issues using the model before it was defined
        related_name='user_profiles'  # the name for that relation from the point of view of a skill
    )
    onboarding_status = models.CharField(
        max_length=200,
        choices=[
            ("Applied", "Applied"),
            ("Validated", "Validated"),
            ("Interviewed", "Interviewed"),
            ("Ranked", "Ranked"),
            ("Accepted", "Accepted"),
            ("Onboarded", "Onboarded"),
            ("Ready", "Ready")
        ],
        default="Applied"
    )
    rank = models.CharField(
        max_length=200,
        null=True,
        choices=[
            ("Junior", "Junior"),
            ("Mid-level", "Mid-level"),
            ("Lead", "Lead")
        ],
        default=None
    )
    social_account = models.URLField(max_length=200, null=True)
    linkedin_account = models.URLField(max_length=200,null=True)
    private_notes = models.TextField(null=True)
    
    def __str__(self):
        return self.username
    
class Skill(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)
# Uncomment these to insert the skills into the database. Must have server running for these commands to work.
# Will need to look at a better way of prepopulating the data once when deployed.
# Skill.objects.create(name="Python", abbreviation="Python")
# Skill.objects.create(name="Django", abbreviation="Django")
# Skill.objects.create(name="React", abbreviation="React")
# Skill.objects.create(name="JavaScript", abbreviation="JavaScript")
# Skill.objects.create(name="Frontend", abbreviation="Front-end")
# Skill.objects.create(name="Backend", abbreviation="Back-end")
# Skill.objects.create(name="HTML-CSS", abbreviation="HTML-CSS")