# Generated by Django 4.0.4 on 2022-05-25 06:40

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_house_company_id_alter_user_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'PromoCompany', 'verbose_name_plural': 'PromoCompanies'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'House', 'verbose_name_plural': 'Houses'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RenameField(
            model_name='house',
            old_name='address',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='company',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='house',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='house',
            name='house_id',
        ),
        migrations.AddField(
            model_name='company',
            name='company_description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='house_number',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='street',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_number', models.IntegerField()),
                ('entrance_number', models.IntegerField()),
                ('is_open', models.BooleanField(default=False)),
                ('owners_name', models.CharField(max_length=200)),
                ('owners_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('comment', models.CharField(max_length=200)),
                ('reaction', models.CharField(choices=[('NT', 'neutral'), ('PS', 'positive'), ('NG', 'negative')], max_length=2)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.house')),
            ],
            options={
                'verbose_name': 'Apartment',
                'verbose_name_plural': 'Apartments',
            },
        ),
    ]