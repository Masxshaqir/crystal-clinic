# Generated by Django 4.2.13 on 2024-07-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
            ],
        ),
    ]
