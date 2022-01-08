# Generated by Django 4.0.1 on 2022-01-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Guest name')),
                ('email', models.EmailField(max_length=254, verbose_name='Contact information')),
                ('text', models.TextField(max_length=2000, verbose_name='Content')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('edition_date', models.DateTimeField(auto_now=True, verbose_name='Date of edition')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=200, verbose_name='process')),
            ],
            options={
                'verbose_name': 'guests list',
                'verbose_name_plural': 'guest book list',
                'db_table': 'guests',
            },
        ),
    ]
