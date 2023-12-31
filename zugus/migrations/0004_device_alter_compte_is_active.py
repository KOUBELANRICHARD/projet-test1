# Generated by Django 4.2.5 on 2023-10-16 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zugus', '0003_alter_compte_email_alter_compte_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=25)),
                ('localisation', models.CharField(max_length=50)),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='compte',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
