# Generated by Django 4.1.2 on 2022-10-27 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_type', '0001_initial'),
        ('supers', '0003_alter_supers_super_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supers',
            name='super_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='super_type.super_type'),
        ),
    ]
