# Generated by Django 4.0.4 on 2022-04-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0005_alter_track_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='city',
            field=models.CharField(default='benin', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='state',
            field=models.CharField(default='Edo', max_length=50),
            preserve_default=False,
        ),
    ]
