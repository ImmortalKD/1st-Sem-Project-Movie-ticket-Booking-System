# Generated by Django 3.0

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_customer_gen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]