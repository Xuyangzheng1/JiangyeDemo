# Generated by Django 4.0.4 on 2022-07-29 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiangyeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='uesrImg',
            field=models.ImageField(default=0, upload_to='userImg/', verbose_name='img'),
        ),
    ]
