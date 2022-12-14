# Generated by Django 4.1 on 2022-08-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=16)),
                ('lname', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=244)),
                ('phone', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=32)),
                ('created', models.DateField()),
            ],
        ),
    ]
