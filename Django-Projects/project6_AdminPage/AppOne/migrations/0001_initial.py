# Generated by Django 4.2.2 on 2023-12-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sid', models.IntegerField()),
                ('Sname', models.CharField(max_length=30)),
                ('Smarks', models.IntegerField()),
                ('Slocation', models.CharField(max_length=30)),
            ],
        ),
    ]
