# Generated by Django 4.0.5 on 2022-06-05 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='', null='True', on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
