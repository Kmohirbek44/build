# Generated by Django 4.1 on 2022-08-31 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_description_ru_product_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_ru',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
