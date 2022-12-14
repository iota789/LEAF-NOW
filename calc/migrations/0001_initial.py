# Generated by Django 4.0.4 on 2022-06-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=20)),
                ('phone_no', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('pdet', models.CharField(max_length=50)),
                ('payment', models.CharField(max_length=15)),
                ('d_id', models.BooleanField(default=False)),
                ('s_id', models.BooleanField(default=False)),
            ],
        ),
    ]
