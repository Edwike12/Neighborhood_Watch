# Generated by Django 2.2.24 on 2022-02-20 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0005_business_location_neighborhood_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.NeighborHood'),
        ),
    ]
