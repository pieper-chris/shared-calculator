# Generated by Django 3.0.8 on 2020-08-06 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_auto_20200806_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computation',
            name='comp',
            field=models.TextField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
