# Generated by Django 4.2.13 on 2024-05-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_empleado_trabajo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
