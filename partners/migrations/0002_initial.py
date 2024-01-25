# Generated by Django 5.0.1 on 2024-01-25 13:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поставщика'),
        ),
        migrations.AddField(
            model_name='partners',
            name='part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='partners.partners', verbose_name='Поставщик'),
        ),
        migrations.AddField(
            model_name='partners',
            name='product',
            field=models.ManyToManyField(to='products.product', verbose_name='Продукт'),
        ),
    ]
