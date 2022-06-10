# Generated by Django 4.0.5 on 2022-06-09 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_rename_codeb_customer_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone_number', models.IntegerField()),
                ('linkedin_profile', models.URLField()),
                ('company', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('code', models.IntegerField()),
                ('company_address', models.CharField(max_length=255)),
                ('products', models.CharField(max_length=255)),
                ('BOM_position', models.CharField(max_length=255)),
                ('company_linkedin', models.URLField()),
                ('company_email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
