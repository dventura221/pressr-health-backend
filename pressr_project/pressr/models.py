from django.db import models
from datetime import date

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    # https://stackoverflow.com/questions/22212479/display-date-of-birth-in-django-app
    dob = models.DateField()
    photo_url = models.TextField()
    is_provider = False
    provider_type = models.CharField(max_length=100)
    provider_choices = [
        ('Physician', 'Physician'),
        ('PA', 'PA'),
        ('NP', 'NP')
    ]
    # https://books.agiliq.com/projects/django-orm-cookbook/en/latest/self_fk.html
    provider = models.ForeignKey('self', on_delete=models.CASCADE)

    def calculate_age(self):
        today = date.today()

        try:
            birthday = self.dob.replace(year=today.year)
        # raised when birth date is February 29 and the current year is not a leap year
        except ValueError:
            birthday = self.dob.replace(year=today.year, day=born.day-1)

        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year

    def __str__(self):
        return self.name


class Reading(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='readings')
    systolic = models.IntegerField(max_length=3)
    diastolic = models.IntegerField(max_length=3)

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
