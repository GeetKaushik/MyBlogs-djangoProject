# Generated by Django 5.0.1 on 2024-01-16 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0003_alter_blog_category_blog_cat_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=100)),
                ('u_email', models.EmailField(max_length=254)),
                ('u_query', models.CharField(max_length=200)),
            ],
        ),
    ]