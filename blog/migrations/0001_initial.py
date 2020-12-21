# Generated by Django 3.1.2 on 2020-12-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='blog')),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('travel', 'Travel'), ('services', 'Services'), ('food', 'Food')], max_length=8)),
            ],
            options={
                'db_table': 'post',
                'managed': False,
            },
        ),
    ]