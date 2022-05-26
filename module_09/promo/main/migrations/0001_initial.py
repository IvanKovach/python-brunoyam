# Generated by Django 4.0.4 on 2022-05-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('company_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_id', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('numbers_entrance', models.IntegerField()),
                ('numbers_apartment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]