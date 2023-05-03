# Generated by Django 3.1.7 on 2023-02-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=30)),
                ('pub_date', models.DateField(verbose_name='date_published')),
            ],
        ),
    ]