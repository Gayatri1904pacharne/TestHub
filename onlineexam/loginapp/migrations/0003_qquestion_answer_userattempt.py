# Generated by Django 5.1.3 on 2024-12-25 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_result_alter_question_answer_alter_question_op1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qquestion',
            fields=[
                ('qno', models.IntegerField(primary_key=True, serialize=False)),
                ('qtext', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='loginapp.question')),
            ],
        ),
        migrations.CreateModel(
            name='UserAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_answer', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginapp.question')),
            ],
        ),
    ]
