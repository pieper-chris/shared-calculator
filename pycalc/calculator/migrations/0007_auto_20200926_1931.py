# Generated by Django 3.1.1 on 2020-09-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0006_auto_20200806_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computation',
            name='entered_at',
            field=models.TextField(blank=True, default=None, max_length=30, null=True),
        ),
    ]