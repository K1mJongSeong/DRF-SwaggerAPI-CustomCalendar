# Generated by Django 4.1.6 on 2023-03-02 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_calendar_nansu'),
    ]

    operations = [
        migrations.AddField(
            model_name='nansu',
            name='related_nansu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calendars', to='app.nansu'),
        ),
    ]
