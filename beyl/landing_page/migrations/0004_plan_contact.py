# Generated by Django 3.1.2 on 2020-10-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0003_plan_planfeature_planinclude'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='contact',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
