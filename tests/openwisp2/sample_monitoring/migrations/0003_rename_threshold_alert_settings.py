# Generated by Django 3.0.3 on 2020-05-30 19:12

from django.core.validators import MaxValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_monitoring', '0002_add_details_field'),
    ]

    operations = [
        migrations.RenameModel('Threshold', 'AlertSettings'),
        migrations.AlterField(
            model_name='alertsettings',
            name='seconds',
            field=models.PositiveIntegerField(
                default=0,
                help_text='for how long should the alert_settings value be crossed before triggering an alert? The maximum allowed is 604800 seconds (7 days)',
                validators=[MaxValueValidator(604800)],
            ),
        ),
        migrations.AlterField(
            model_name='alertsettings',
            name='value',
            field=models.FloatField(help_text='alert settings value'),
        ),
    ]