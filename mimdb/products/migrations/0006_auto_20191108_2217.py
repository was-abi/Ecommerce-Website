# Generated by Django 2.2.7 on 2019-11-08 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productimage_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title', 'slug')},
        ),
    ]