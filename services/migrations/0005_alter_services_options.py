# Generated by Django 5.0.4 on 2024-05-24 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_services_options_alter_services_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ('id',), 'verbose_name': 'Услугу', 'verbose_name_plural': 'Услуги'},
        ),
    ]
