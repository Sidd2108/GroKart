# Generated by Django 4.1.1 on 2022-11-10 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0007_rename_total_morrisons_basket_total_amazon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='total_amazon',
            new_name='total_morrisons',
        ),
        migrations.RenameField(
            model_name='basket',
            old_name='total_bigbasket',
            new_name='total_sainsburys',
        ),
        migrations.RenameField(
            model_name='basket',
            old_name='total_dmart',
            new_name='total_tesco',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='total_flipkart',
        ),
    ]