# Generated by Django 4.0.5 on 2022-06-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_remove_prefixmodel_id_prefixmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefixmodel',
            name='image',
            field=models.ImageField(unique=True, upload_to=''),
        ),
    ]
