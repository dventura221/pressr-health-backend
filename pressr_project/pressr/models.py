from django.db import models
from datetime import date

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
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
