# Generated by Django 4.0.5 on 2022-06-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_profile_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='company_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='company_email',
            new_name='email_company',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='company_linkedin',
            new_name='linkedin_company',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='linkedin_profile',
            new_name='linkedin_user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='telephone_number',
        ),
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='employees',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='prefix',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='sectors',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='turnover',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='type_of_code',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
