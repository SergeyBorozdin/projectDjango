# Generated by Django 5.0.6 on 2024-06-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_equipment_options_alter_equipment_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='title',
            field=models.CharField(default='', max_length=250, verbose_name='title'),
            preserve_default=False,
        ),
    ]
