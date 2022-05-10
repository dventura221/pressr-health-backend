from django.db import models
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes import fields

# Create your models here.


class Provider(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    photo_url = models.TextField(null=True)
    provider_choices = [
        ('Physician', 'Physician'),
        ('PA', 'PA'),
        ('NP', 'NP')
    ]
    provider_type = models.CharField(
        max_length=101, choices=provider_choices, blank=True, null=True)

    def __str__(self):
        return (self.last_name + ", " + self.first_name + ", " + self.provider_type)


class User(models.Model):
    first_name = models.CharField(max_length=101, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    # https://stackoverflow.com/questions/22212479/display-date-of-birth-in-django-app
    dob = models.DateField(blank=True, null=True)
    photo_url = models.TextField(null=True)
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, blank=True, null=True, related_name='users')

    def __str__(self):
        return (self.last_name + ", " + self.first_name)


class Reading(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='readings')
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (str(self.systolic) + " / " + str(self.diastolic))


comment_choices = (
    ('User', 'User'),
    ('Provider', 'Provider')
)


class Comment(models.Model):
    author_of_comment = models.CharField(
        max_length=8, choices=comment_choices, default=None)
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, blank=True, null=True, related_name='comments', default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='comments', default=0)
    reading = models.ForeignKey(
        Reading, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.content)
