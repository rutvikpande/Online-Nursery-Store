# Generated by Django 4.0.3 on 2022-04-06 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_caritem_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=250)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='RS Order Total')),
                ('emailAddress', models.EmailField(blank=True, max_length=250, verbose_name='Email Address')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('billingName', models.CharField(blank=True, max_length=250)),
                ('billingAddress1', models.CharField(blank=True, max_length=250)),
                ('billingCity', models.CharField(blank=True, max_length=250)),
                ('billingPostcode', models.CharField(blank=True, max_length=250)),
                ('billingCountry', models.CharField(blank=True, max_length=250)),
                ('shippingName', models.CharField(blank=True, max_length=250)),
                ('shippingAddress1', models.CharField(blank=True, max_length=250)),
                ('shippingCity', models.CharField(blank=True, max_length=250)),
                ('shippingPostcode', models.CharField(blank=True, max_length=250)),
                ('shippingCountry', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='RS Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]
