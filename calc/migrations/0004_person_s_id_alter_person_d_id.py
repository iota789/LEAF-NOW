# Generated by Django 4.0.4 on 2022-06-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_remove_person_s_id_alter_person_d_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='s_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='d_id',
            field=models.BooleanField(default=False),
        ),
    ]
