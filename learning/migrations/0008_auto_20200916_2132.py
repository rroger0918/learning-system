# Generated by Django 2.2 on 2020-09-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_auto_20200916_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='IMG',
        ),
    ]
