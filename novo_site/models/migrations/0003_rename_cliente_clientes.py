# Generated by Django 4.1 on 2024-06-19 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_cliente_bairro_cli'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cliente',
            new_name='Clientes',
        ),
    ]
