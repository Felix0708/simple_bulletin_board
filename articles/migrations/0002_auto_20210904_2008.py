# Generated by Django 3.2.7 on 2021-09-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
