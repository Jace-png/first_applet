# Generated by Django 3.0.3 on 2020-03-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juhe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='coll',
            field=models.CharField(default='test', max_length=64),
        ),
    ]