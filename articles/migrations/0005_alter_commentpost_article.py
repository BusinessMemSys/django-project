# Generated by Django 3.2.8 on 2021-10-29 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20211029_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpost',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.article'),
        ),
    ]
