# Generated by Django 2.2.17 on 2021-01-30 08:35

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import django_jsonfield_backport.models


class Migration(migrations.Migration):

    dependencies = [('dojo', '0074_notifications_close_engagement')]

    operations = [
        migrations.CreateModel(
            name='Test_Import',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('import_settings', django_jsonfield_backport.models.JSONField(null=True)),
                ('version', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(default='unknown', max_length=64, null=False)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Test_Import_Finding_Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('action', models.CharField(blank=True, choices=[('N', 'created'), ('C', 'closed'), ('R', 'reactivated'), ('U', 'updated')], max_length=100, null=True)),
                ('finding', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='dojo.Finding')),
                ('test_import', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='dojo.Test_Import')),
            ],
            options={
                'ordering': ('test_import', 'action', 'finding'),
                'unique_together': {('test_import', 'finding')},
            },
        ),
        migrations.AddField(
            model_name='test_import',
            name='findings_affected',
            field=models.ManyToManyField(through='dojo.Test_Import_Finding_Action', to='dojo.Finding'),
        ),
        migrations.AddField(
            model_name='test_import',
            name='test',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='dojo.Test'),
        ),
        migrations.AddIndex(
            model_name='test_import',
            index=models.Index(fields=['created', 'test', 'type'], name='dojo_test_i_created_951f4e_idx'),
        ),

    ]
