# Generated by Django 4.0.4 on 2022-04-21 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_track_date_created_alter_track_pickup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]