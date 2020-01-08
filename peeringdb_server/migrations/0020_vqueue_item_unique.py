# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-04 08:38


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("peeringdb_server", "0019_auto_20190819_1133"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="verificationqueueitem",
            unique_together=set([("content_type", "object_id")]),
        ),
    ]