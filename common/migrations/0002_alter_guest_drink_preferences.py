# Generated by Django 4.2.2 on 2023-06-22 13:15

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='drink_preferences',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('shamp', 'Шампанское'), ('white_wine', 'Белое вино'), ('red_wine', 'Красное вино'), ('samogon', 'Папин самогон'), ('vodka', 'Водка'), ('kon', 'Коньяк'), ('no', 'А я и не пью')], max_length=20, null=True, verbose_name='Предпочтения по напиткам'),
        ),
    ]