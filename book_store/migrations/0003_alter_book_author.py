# Generated by Django 5.1.4 on 2025-01-29 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0002_alter_book_created_at_alter_book_published_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.OneToOneField(limit_choices_to={'user_type': 'author'}, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
