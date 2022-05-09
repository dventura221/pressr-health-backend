# Generated by Django 4.0.4 on 2022-05-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pressr', '0004_alter_user_dob_alter_user_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='provider_type',
            field=models.CharField(choices=[('Physician', 'Physician'), ('PA', 'PA'), ('NP', 'NP')], max_length=101, null=True),
        ),
    ]