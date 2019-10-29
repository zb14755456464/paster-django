# Copyright 2019-present Lenovo
# Confidential and Proprietary

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
