# Generated by Django 4.2.2 on 2023-07-12 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='color',
            field=models.CharField(choices=[('black', 'BLACK'), ('white', 'WHITE'), ('grey', 'GREY'), ('blue', 'BLUE'), ('pink', 'PINK')], max_length=15),
        ),
    ]
