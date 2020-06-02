from django.db import models
from PIL import Image
from django.utils import timezone
import datetime
from multiselectfield import MultiSelectField
from ckeditor_uploader.fields import RichTextUploadingField

STATUS = (
    ('Open', 'Open'),
    ('In Progress', 'In Progress'),
    ('Archived', 'Archived'),
    ('Rolling', 'Rolling')
)

class ChallengeTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ChallengeAudience(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Challenges(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150)
    offered_by = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media_pics/%Y/%m/%d', blank=True, default='default-banner.jpg')
    challenge_summary = models.CharField(max_length=250, default='')
    description = RichTextUploadingField()
    external_url = models.CharField(max_length=150)
    targeted_audience = models.ForeignKey(ChallengeAudience, on_delete=models.CASCADE)
    tags = models.ManyToManyField(ChallengeTag)
    rules_of_engagement = RichTextUploadingField()
    judging_criteria = RichTextUploadingField()
    prize = models.CharField(max_length=150)
    how_to_enter = RichTextUploadingField()
    point_of_contact = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    open_until = models.DateField()
    status = models.CharField(choices=STATUS, max_length=200, default='Open')


    class Meta:
        verbose_name = 'challenge'
        verbose_name_plural = 'challenges'

    def get_absolute_url(self):
        return f'detail/{self.id}/{self.slug}/'

    def __str__(self):
        return self.title


class Preapproved_challenge(models.Model):
    goal = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    length = models.CharField(max_length=150)
    short_description = models.TextField()
    steps_to_complete = models.TextField()
    why = models.TextField(blank=True, null=True)
    tips = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(ChallengeTag)

    def __str__(self):
        return self.name
