# Generated by Django 2.2.5 on 2019-09-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0004_auto_20190910_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
