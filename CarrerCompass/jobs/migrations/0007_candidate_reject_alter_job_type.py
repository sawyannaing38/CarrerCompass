# Generated by Django 5.1 on 2024-09-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_job_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='reject',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(default='open', max_length=5),
        ),
    ]
