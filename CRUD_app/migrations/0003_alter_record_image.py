# Generated by Django 5.2.3 on 2025-06-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_app', '0002_record_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
