# Generated by Django 4.1.1 on 2022-09-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0006_remove_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank='True'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.SlugField(max_length=200),
        ),
    ]
