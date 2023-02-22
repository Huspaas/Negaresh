# Generated by Django 4.1.6 on 2023-02-22 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0005_contract_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='منتشرکننده'),
        ),
    ]