# Generated by Django 5.0.1 on 2024-01-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0005_remove_query_u_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='u_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
