# Generated by Django 4.1.5 on 2023-01-10 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_birth', models.DateField()),
                ('addres', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('mobile_phone', models.IntegerField()),
            ],
        ),
    ]
