# Generated by Django 4.1.6 on 2023-03-08 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_delete_imagetest_remove_calendar_nansu_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='nansu_data',
        ),
        migrations.RemoveField(
            model_name='nansu',
            name='related_nansu',
        ),
        migrations.AddField(
            model_name='aprilback',
            name='april_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='aprilback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aprilfront',
            name='april_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='aprilfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='augback',
            name='aug_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='augback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='augfront',
            name='aug_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='augfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cover',
            name='cover_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='cover',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='decback',
            name='dec_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='decback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='decfront',
            name='dec_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='decfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='febback',
            name='feb_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='febback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='febfront',
            name='feb_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='febfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='janback',
            name='jan_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='janback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='janfront',
            name='jan_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='janfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='julyback',
            name='july_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='julyback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='julyfront',
            name='july_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='julyfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='juneback',
            name='june_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='juneback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='junefront',
            name='june_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='junefront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marback',
            name='mar_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='marback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marfront',
            name='mar_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='marfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mayback',
            name='may_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='mayback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mayfront',
            name='may_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='mayfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='novback',
            name='nov_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='novback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='novfront',
            name='nov_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='novfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='octback',
            name='oct_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='octback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='octfront',
            name='oct_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='octfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prolog',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prolog',
            name='prolog_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='sepback',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sepback',
            name='sep_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='sepfront',
            name='page_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sepfront',
            name='sep_idx',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='aprilback',
            name='april_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='aprilback',
            name='april_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='aprilfront',
            name='april_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='aprilfront',
            name='april_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='augback',
            name='aug_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='augback',
            name='aug_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='augfront',
            name='aug_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='augfront',
            name='aug_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cover',
            name='cover_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cover',
            name='cover_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='decback',
            name='dec_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='decback',
            name='dec_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='decfront',
            name='dec_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='decfront',
            name='dec_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='febback',
            name='feb_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='febback',
            name='feb_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='febfront',
            name='feb_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='febfront',
            name='feb_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='janback',
            name='jan_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='janback',
            name='jan_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='janfront',
            name='jan_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='janfront',
            name='jan_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='julyback',
            name='july_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='julyback',
            name='july_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='julyfront',
            name='july_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='julyfront',
            name='july_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='juneback',
            name='june_picl',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='juneback',
            name='june_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='junefront',
            name='june_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='junefront',
            name='june_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='marback',
            name='mar_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='marback',
            name='mar_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='marfront',
            name='mar_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='marfront',
            name='mar_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mayback',
            name='may_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mayback',
            name='may_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mayfront',
            name='may_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mayfront',
            name='may_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='novback',
            name='nov_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='novback',
            name='nov_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='novfront',
            name='nov_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='novfront',
            name='nov_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='octback',
            name='oct_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='octback',
            name='oct_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='octfront',
            name='oct_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='octfront',
            name='oct_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prolog',
            name='prolog_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='prolog',
            name='prolog_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sepback',
            name='sep_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sepback',
            name='sep_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sepfront',
            name='sep_pic',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sepfront',
            name='sep_seq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
