# Generated by Django 5.0.2 on 2024-03-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_document_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='videotitle',
            field=models.CharField(default=None, max_length=800),
        ),
    ]