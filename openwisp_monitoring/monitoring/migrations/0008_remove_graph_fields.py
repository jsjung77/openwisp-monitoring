# Generated by Django 3.0.5 on 2020-04-28 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0007_fill_configuration'),
    ]

    operations = [
        migrations.RemoveField(model_name='graph', name='query',),
        migrations.RemoveField(model_name='graph', name='top_fields',),
        migrations.RemoveField(model_name='graph', name='description',),
        migrations.RemoveField(model_name='graph', name='type',),
    ]