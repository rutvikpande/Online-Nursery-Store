# Generated by Django 4.0.2 on 2022-04-05 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart_caritem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarItem',
            new_name='CartItem',
        ),
    ]