# Generated by Django 2.1 on 2018-08-08 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SearchPage', '0002_auto_20180727_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='AAlopecia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.TextField()),
                ('sinlair', models.IntegerField(max_length=10)),
                ('menstrual', models.BooleanField(default=None)),
                ('hirsutism', models.BooleanField(default=None)),
                ('acne', models.BooleanField(default=None)),
                ('familyH', models.BooleanField(default=None)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SearchPage.Patients')),
            ],
        ),
        migrations.CreateModel(
            name='AAreata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('S', 'Single patch'), ('M', 'Multiple patches'), ('AT', 'Alopecia Totalis'), ('AU', 'Alopecia Universalis'), ('D', 'Diffuse')], max_length=30)),
                ('sites', models.CharField(choices=[('Scalp', 'Scalp'), ('Beard', 'Beard'), ('EB', 'Eyebrows'), ('EL', 'Eyelashes'), ('Body', 'Body')], max_length=30)),
                ('AA', models.CharField(choices=[('None', 'None'), ('T', 'Thyroid'), ('LE', 'Lupus Erythromatosis'), ('DM', 'Diabetes Melitus'), ('V', 'Vitiligo'), ('IBD', 'Inflamatory Bowel Disease'), ('ITP', 'Idiopathic Thrombocytopenia'), ('RA', 'Rheumatoid Arthritis'), ('PA', 'Pernicious Anemia')], max_length=30)),
                ('nails', models.CharField(choices=[('None', 'None'), ('Pitting', 'Pitting'), ('Brittle', 'Brittle'), ('LR', 'Longitudinal ridging'), ('Oncholysis', 'Onycholysis'), ('Onchomadesis', 'Onychomadesis')], max_length=30)),
                ('atopy', models.CharField(choices=[('None', 'None'), ('AD', 'Atopic dermatitis'), ('AR', 'Allergic rhinitis'), ('HF', 'Hay fever')], max_length=30)),
                ('familyH', models.BooleanField(default=None)),
                ('familyAA', models.CharField(choices=[('None', 'None'), ('T', 'Thyroid'), ('LE', 'Lupus Erythromatosis'), ('DM', 'Diabetes Melitus'), ('V', 'Vitiligo'), ('IBD', 'Inflamatory Bowel Disease'), ('ITP', 'Idiopathic Thrombocytopenia'), ('RA', 'Rheumatoid Arthritis'), ('PA', 'Pernicious Anemia')], max_length=30)),
                ('salt', models.IntegerField(max_length=10)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SearchPage.Patients')),
            ],
        ),
    ]