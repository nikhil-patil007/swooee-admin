# Generated by Django 3.0 on 2022-01-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swooee', '0006_auto_20220110_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='v_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
