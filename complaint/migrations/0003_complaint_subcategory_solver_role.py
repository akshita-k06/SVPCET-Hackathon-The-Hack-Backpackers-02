# Generated by Django 3.1.3 on 2020-11-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0002_complaint_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint_subcategory',
            name='solver_role',
            field=models.SmallIntegerField(blank=True, default=1, null=True),
        ),
    ]
