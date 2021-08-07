# Generated by Django 3.1.6 on 2021-08-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dpt_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('faculties', models.CharField(max_length=225)),
            ],
            options={
                'db_table': 'table_1',
            },
        ),
    ]