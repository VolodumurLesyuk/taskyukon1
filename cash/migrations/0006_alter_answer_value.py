# Generated by Django 4.1.5 on 2023-01-28 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0005_alter_answer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='value',
            field=models.FloatField(max_length=10),
        ),
    ]
