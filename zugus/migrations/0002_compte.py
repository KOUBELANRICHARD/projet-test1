# Generated by Django 4.2.5 on 2023-10-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zugus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=128)),
                ('dateCreation', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
