# Generated by Django 4.2.3 on 2023-07-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstar', '0008_feedback_alter_info_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='district',
            field=models.CharField(default='Maharashatra', max_length=50),
            preserve_default=False,
        ),
    ]
