# Generated by Django 5.1.2 on 2024-11-15 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=50)),
                ('descriptoin', models.CharField(max_length=300)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('car_img', models.ImageField(upload_to='car/media/uploads/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.carbrandmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('commented_on', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.carmodle')),
            ],
        ),
    ]
