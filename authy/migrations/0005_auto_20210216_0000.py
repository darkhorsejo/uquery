# Generated by Django 3.0.8 on 2021-02-15 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0004_auto_20200814_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='high_school',
            field=models.CharField(blank=True, default='Name of High school', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='position_at_work',
            field=models.CharField(blank=True, default='Position at work', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='previous_work',
            field=models.CharField(blank=True, default='Previous place worked', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='read',
            field=models.CharField(blank=True, default='Course of study', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='schooled_at',
            field=models.CharField(blank=True, default='Name of Tertiary Inst', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_at',
            field=models.CharField(blank=True, default='Workplace', max_length=100, null=True),
        ),
    ]
