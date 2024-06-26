# Generated by Django 5.0.4 on 2024-05-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ('id',), 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='services',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='Скидка в %'),
        ),
    ]
