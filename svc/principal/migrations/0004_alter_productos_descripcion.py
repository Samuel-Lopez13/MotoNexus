# Generated by Django 5.0.4 on 2024-05-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_alter_marcas_table_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='descripcion',
            field=models.TextField(),
        ),
    ]