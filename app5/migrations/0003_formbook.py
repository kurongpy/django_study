# Generated by Django 3.0.3 on 2020-03-02 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0002_auto_20200302_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('page', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'form_book',
            },
        ),
    ]
