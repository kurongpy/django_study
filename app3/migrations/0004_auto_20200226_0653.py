# Generated by Django 3.0.3 on 2020-02-25 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0003_ormfrontuser_userextension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ext', to='app3.ORMFrontUser'),
        ),
        migrations.CreateModel(
            name='ORMTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('articles', models.ManyToManyField(to='app3.ORMArticle')),
            ],
            options={
                'db_table': 'orm_tag',
            },
        ),
    ]
