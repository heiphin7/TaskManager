# Generated by Django 4.2.8 on 2023-12-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190329_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='team_files/'),
        ),
    ]
