# Generated by Django 4.2.4 on 2024-02-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedIQ_Advisor_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mental_Health_Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('self_employed', models.CharField(max_length=5)),
                ('family_history', models.CharField(max_length=5)),
                ('mental_health_interference', models.CharField(max_length=10)),
                ('company_size', models.CharField(max_length=20)),
                ('remote_work', models.CharField(max_length=5)),
                ('tech_company', models.CharField(max_length=5)),
                ('mental_health_benefits', models.CharField(max_length=5)),
                ('know_mental_health_care', models.CharField(max_length=10)),
                ('discussed_mental_health', models.CharField(max_length=10)),
                ('resources_learn_mental_health', models.CharField(max_length=10)),
                ('anonymity_protected', models.CharField(max_length=10)),
                ('medical_leave', models.CharField(max_length=20)),
                ('negative_consequences_mental_health', models.CharField(max_length=10)),
                ('negative_consequences_physical_health', models.CharField(max_length=10)),
                ('discuss_with_coworkers', models.CharField(max_length=10)),
                ('discuss_with_supervisors', models.CharField(max_length=10)),
                ('bring_up_in_interview_mental_health', models.CharField(max_length=10)),
                ('bring_up_in_interview_physical_health', models.CharField(max_length=10)),
                ('employer_takes_mental_health_seriously', models.CharField(max_length=10)),
                ('observed_negative_consequences', models.CharField(max_length=5)),
            ],
        ),
    ]