# Generated by Django 3.0.4 on 2020-03-11 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200310_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_view', 'Can view book instance'),)},
        ),
    ]