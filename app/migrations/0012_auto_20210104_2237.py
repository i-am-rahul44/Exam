# Generated by Django 3.1.3 on 2021-01-04 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201228_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Type',
        ),
        migrations.AddField(
            model_name='course',
            name='materials',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='materials',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer_sheet',
            name='Attempted_option',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]