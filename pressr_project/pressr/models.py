from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    # https://stackoverflow.com/questions/22212479/display-date-of-birth-in-django-app
    dob = models.DateField(blank=True, null=True)
    photo_url = models.TextField(null=True)
    provider = models.ForeignKey(
        'self', on_delete=models.PROTECT, blank=True, null=True, )

    def __str__(self):
        return (self.last_name + ", " + self.first_name)


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


class Reading(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='readings')
    systolic = models.IntegerField()
    diastolic = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    reading = models.ForeignKey(
        Reading, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
