# Generated by Django 4.1.10 on 2023-10-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_alter_chapter_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter',
            field=models.FileField(default='', upload_to='chapters/'),
            preserve_default=False,
        ),
    ]
