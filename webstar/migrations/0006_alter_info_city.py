# Generated by Django 4.2.3 on 2023-07-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstar', '0005_alter_info_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
    ]
