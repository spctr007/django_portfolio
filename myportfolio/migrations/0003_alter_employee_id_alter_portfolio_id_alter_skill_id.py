# Generated by Django 4.1 on 2023-01-30 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_auto_20230130_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
