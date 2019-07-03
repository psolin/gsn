# Generated by Django 2.2.1 on 2019-06-26 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gsndb', '0008_merge_20190624_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='behavior',
            name='behavior_SISID',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HistoricalStudentID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_SISID', models.BigIntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gsndb.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gsndb.Student')),
            ],
        ),
    ]