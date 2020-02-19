# Generated by Django 3.0.3 on 2020-02-19 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kennywoodapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attractions', to='kennywoodapi.ParkArea'),
        ),
    ]