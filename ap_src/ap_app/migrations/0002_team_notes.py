# Generated by Django 3.2.9 on 2022-10-24 11:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ap_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='notes',
            field=models.CharField(default=django.utils.timezone.now, max_length=512),
            preserve_default=False,
        ),
    ]
