# Generated by Django 3.0.3 on 2020-03-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('juhe', '0008_auto_20200310_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='menu',
            field=models.ManyToManyField(to='api.App'),
        ),
    ]
