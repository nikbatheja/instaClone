# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 06:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20170809_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=40)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='is_dirty',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='comment_text',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserModel'),
        ),
        migrations.AlterField(
            model_name='likemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserModel'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.FileField(upload_to=b'instacloneuser_images'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserModel'),
        ),
        migrations.AlterField(
            model_name='sessiontoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserModel'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
