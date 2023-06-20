# Generated by Django 3.2.19 on 2023-06-20 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkSelection',
            fields=[
                ('drink_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_drink', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200, unique=True)),
                ('price', models.FloatField()),
                ('drink_choice', models.IntegerField(choices=[(0, 'White Wine'), (1, 'Red Wine'), (2, 'Rose Wine'), (3, 'Prosecco'), (4, 'Beers'), (5, 'Cocktails'), (6, 'Spirits'), (7, 'New')], default=7)),
                ('available', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-available'],
            },
        ),
        migrations.CreateModel(
            name='FoodSelection',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_food', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('food_choice', models.IntegerField(choices=[(0, 'Starters'), (1, 'Mains'), (2, 'Steaks'), (3, 'Desserts'), (4, 'New')], default=4)),
                ('available', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-food_choice'],
            },
        ),
    ]