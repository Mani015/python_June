# Generated by Django 4.2.2 on 2023-12-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('img_url', models.CharField(max_length=900)),
            ],
        ),
    ]
