# Generated by Django 4.2 on 2023-04-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_bmpimage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmpimage',
            name='match_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bmpimage',
            name='patient_finger',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bmpimage',
            name='patient_gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bmpimage',
            name='patient_hand',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bmpimage',
            name='patient_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bmpimage',
            name='patient_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bmpimage',
            name='patient_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bmpimage',
            name='patient_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
