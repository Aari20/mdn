# Generated by Django 3.0.4 on 2020-03-11 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20200311_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_view_instance', 'Librarienii pot vedea cine a luat cartile'), ('can_mark_returned', 'Librarienii pot schimba data de returnare a cartilor'))},
        ),
    ]
