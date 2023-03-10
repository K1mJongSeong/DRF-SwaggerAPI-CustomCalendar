# Generated by Django 4.1.6 on 2023-03-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_aprilback_aprilfront_augback_augfront_cover_decback_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='aprilback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='aprilfront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='augback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='augfront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='calendar',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='cover',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='decback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='decfront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='febback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='febfront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='janback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='janfront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='julyback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='julyfront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='juneback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='junefront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='marback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='marfront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='mayback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='mayfront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='nansu',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='novback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='novfront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='octback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='octfront',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='prolog',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='sepback',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='sepfront',
            options={'managed': True},
        ),
    ]
