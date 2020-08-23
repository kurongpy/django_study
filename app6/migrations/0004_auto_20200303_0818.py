# Generated by Django 3.0.3 on 2020-03-03 00:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app6', '0003_auto_20200303_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('image', models.ImageField(upload_to='app6/image')),
            ],
            options={
                'db_table': 'app6_image',
            },
        ),
        migrations.AlterField(
            model_name='upfiles',
            name='file',
            field=models.FileField(upload_to='app6/files', validators=[django.core.validators.FileExtensionValidator(['pdf'], message='文件必须为pdf')]),
        ),
    ]
