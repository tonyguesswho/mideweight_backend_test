# Generated by Django 2.2.18 on 2021-02-20 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_sources', '0002_auto_20210220_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatewaystatus',
            name='gateway',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_sources.Gateway'),
        ),
    ]