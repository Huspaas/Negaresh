# Generated by Django 4.1.6 on 2023-02-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=25, verbose_name='نام مشتری')),
                ('dealer', models.CharField(max_length=25, verbose_name='نام کارشناس')),
                ('clientNumber', models.CharField(max_length=11, verbose_name='شماره مشتری')),
            ],
            options={
                'verbose_name': 'قرارداد',
                'verbose_name_plural': 'قرارداد ها',
            },
        ),
    ]
