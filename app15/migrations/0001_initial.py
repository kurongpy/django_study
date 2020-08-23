# Generated by Django 3.0.3 on 2020-03-08 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App15Articls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.fields.CharField, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'app15_article',
                'permissions': [('view_article', '查看文章的权限')],
            },
        ),
    ]
