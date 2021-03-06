from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class BoardModel(models.Model):
    user_id = models.IntegerField(null=True, blank=True, default=0)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    good = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.TextField(null=True, blank=True, default='initial')
    pub_date = models.DateTimeField(default=timezone.now)
    star_rate = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    article_urls = models.TextField()

    def __str__(self):
        return self.title

class ProfileModel(models.Model):
    user_id = models.IntegerField(null=True, blank=True, default=0)
    author = models.CharField(max_length=50)
    one_thing = models.TextField(null=True, blank=True, default='initial')
    header_image = models.ImageField(upload_to='', null=True, blank=True, default=0)
    follow_number = models.IntegerField(null=True, blank=True, default=0)
    follow_text = models.TextField(null=True, blank=True, default='initial')
    befollowed_number = models.IntegerField(null=True, blank=True, default=0)
    befollowed_text = models.TextField(null=True, blank=True, default='initial')

    def __str__(self):
        return self.author
