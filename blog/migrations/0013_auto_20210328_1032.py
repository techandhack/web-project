# Generated by Django 3.1.7 on 2021-03-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210328_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('g', 'Government Jobs'), ('F', 'fee courses online'), ('ge', 'government exams'), ('er', 'government exams result'), ('ee', 'Entrance exam'), ('jn', 'Job Notification'), ('i', 'Internship'), ('wf', 'work form home')], default='random', max_length=50),
        ),
    ]
