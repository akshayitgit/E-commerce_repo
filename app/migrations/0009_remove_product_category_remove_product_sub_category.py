# Generated by Django 4.0.2 on 2022-02-21 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
    ]