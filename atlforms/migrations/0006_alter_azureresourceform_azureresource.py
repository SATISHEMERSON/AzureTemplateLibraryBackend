# Generated by Django 5.1.7 on 2025-03-28 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlforms', '0005_update_field_type_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='azureresourceform',
            name='azureresource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atlforms.azureresources'),
        ),
    ]
