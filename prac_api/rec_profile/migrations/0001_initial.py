# Generated by Django 3.0.8 on 2020-09-06 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FactorsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_factors', models.CharField(default='SOME STRING', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_name', models.CharField(default='SOME STRING', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RecruitSkillsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('skill', models.CharField(default='SOME STRING', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RecruitSkillsTypeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('skill_name', models.CharField(default='SOME STRING', max_length=20)),
                ('skill_number', models.PositiveIntegerField()),
                ('skill_t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_type', to='rec_profile.RecruitSkillsModel')),
            ],
        ),
        migrations.CreateModel(
            name='RecruitOverviewModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rank', models.CharField(default='SOME STRING', max_length=10)),
                ('percentile', models.PositiveIntegerField()),
                ('average_rank', models.CharField(default='SOME STRING', max_length=10)),
                ('rank_evaluation', models.CharField(default='SOME STRING', max_length=10)),
                ('r_overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='overview', to='rec_profile.ProfileModel')),
            ],
        ),
    ]
