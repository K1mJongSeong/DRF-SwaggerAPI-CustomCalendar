# Generated by Django 4.1.6 on 2023-03-03 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_image_image_file_alter_image_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppImage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image_file', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'app_image',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_file',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]