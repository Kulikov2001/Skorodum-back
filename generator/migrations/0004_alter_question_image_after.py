# Generated by Django 5.0.2 on 2024-06-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_alter_question_image_after'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image_after',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
