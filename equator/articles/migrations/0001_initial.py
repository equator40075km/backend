# Generated by Django 4.2.2 on 2023-10-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('preview', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('img', models.URLField()),
                ('rating', models.IntegerField(default=0)),
                ('cat', models.CharField(max_length=150)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
