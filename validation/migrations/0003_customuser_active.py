# Generated by Django 4.0.3 on 2023-02-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0002_customuser_is_sponsor_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='active',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive', max_length=20),
        ),
    ]
