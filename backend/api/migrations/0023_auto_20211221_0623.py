# Generated by Django 3.2.8 on 2021-12-21 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20211220_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='label_new',
        ),
        migrations.RemoveField(
            model_name='span',
            name='label_new',
        ),
        migrations.AlterField(
            model_name='category',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.doctype'),
        ),
        migrations.AlterField(
            model_name='span',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.spantype'),
        ),
    ]
