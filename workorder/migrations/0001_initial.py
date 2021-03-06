# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-28 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('opmanage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host_WorkOrder_info',
            fields=[
                ('host_workorder_id', models.AutoField(primary_key=True, serialize=False)),
                ('submit_time', models.DateField(auto_now_add=True)),
                ('submit_user', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=30)),
                ('git_code', models.CharField(max_length=30)),
                ('describe', models.CharField(max_length=30)),
                ('cloud_type', models.CharField(choices=[('aws', '\u4e9a\u9a6c\u900a\u4e91'), ('qcloud', '\u817e\u8baf\u4e91'), ('aliyun', '\u963f\u91cc\u4e91')], max_length=30)),
                ('apply_type', models.CharField(choices=[('php', 'php'), ('java', 'java')], max_length=30)),
                ('host_type', models.CharField(choices=[('2c4m', '2\u68384G'), ('4c8m', '4\u68388G')], max_length=30)),
                ('host_number', models.PositiveSmallIntegerField()),
                ('pubipaddr', models.CharField(choices=[('t', '\u662f'), ('f', '\u5426')], max_length=30)),
                ('disk', models.CharField(max_length=30)),
                ('monitor_url', models.CharField(max_length=30)),
                ('nginx_log_save', models.CharField(choices=[('t', '\u662f'), ('f', '\u5426')], max_length=30)),
                ('app_log_save_pwd', models.CharField(blank=True, max_length=30, null=True)),
                ('nginx_log_elk', models.CharField(choices=[('t', '\u662f'), ('f', '\u5426')], max_length=30)),
                ('app_log_elk_pwd', models.CharField(blank=True, max_length=30, null=True)),
                ('internal_lb', models.CharField(choices=[('t', '\u662f'), ('f', '\u5426')], max_length=30)),
                ('internal_role', models.CharField(blank=True, max_length=30)),
                ('internet_facing_lb', models.CharField(choices=[('t', '\u662f'), ('f', '\u5426')], max_length=30)),
                ('internet_facing_role', models.CharField(blank=True, max_length=30, null=True)),
                ('internal_domain', models.CharField(choices=[('t', '\u662f'), ('f', '\u5426')], max_length=30)),
                ('internet_facing_domain', models.CharField(choices=[('t', '\u662f'), ('f', '\u5426')], max_length=30)),
                ('domain', models.CharField(blank=True, choices=[('whysdomain.com', 'whysdomain.com'), ('why.com', 'why.com')], max_length=30, null=True)),
                ('serverline_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opmanage.Serverline_info')),
            ],
        ),
        migrations.CreateModel(
            name='Serverline_WorkOrder_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_time', models.DateField(auto_now_add=True)),
                ('submit_user', models.CharField(max_length=20)),
                ('serverline_name', models.CharField(max_length=30)),
                ('describe', models.CharField(max_length=30)),
                ('serverline_leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opmanage.User_info')),
            ],
        ),
        migrations.CreateModel(
            name='Status_WorkOrder_info',
            fields=[
                ('status_workorder_id', models.AutoField(primary_key=True, serialize=False)),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('step_num', models.CharField(max_length=30)),
                ('step_message', models.CharField(max_length=255)),
                ('attribute_workorder', models.ManyToManyField(to='workorder.Host_WorkOrder_info')),
            ],
        ),
    ]
