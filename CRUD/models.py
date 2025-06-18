from django.db import models

# Create your models here.
class Resume(models.Model):
    full_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='media/profile_pictures')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    summary = models.TextField()
    
    # Education
    degree = models.CharField(max_length=255)
    institute_name = models.CharField(max_length=255)
    year_of_graduation = models.PositiveIntegerField()
    
    # Work Experience
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    years_of_experience = models.DecimalField(max_digits=4, decimal_places=1)
    
    # Other Info
    skills = models.TextField(help_text="Comma-separated skills")
    hobbies = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name