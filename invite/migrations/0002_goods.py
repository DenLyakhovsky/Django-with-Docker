# Generated by Django 4.2.2 on 2023-06-17 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('image', models.ImageField(upload_to='invite/images', verbose_name='image')),
                ('price', models.IntegerField(blank=True, verbose_name='price')),
            ],
        ),
    ]
