# Generated by Django 5.0 on 2023-12-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anomaly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mill_type', models.CharField(max_length=20)),
                ('mill_operation', models.CharField(max_length=100)),
                ('anomaly_description', models.TextField()),
            ],
        ),
    ]