# Generated by Django 4.1.2 on 2023-02-07 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_article_like_comment_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='webapp.article', verbose_name='Статья'),
        ),
    ]
