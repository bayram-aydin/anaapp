# Generated by Django 4.1.3 on 2023-05-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_course_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]