# Generated by Django 4.2 on 2025-01-18 21:48

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField()),
                ('date_embauche', models.DateField()),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.IntegerField()),
                ('annee', models.IntegerField()),
                ('salaire_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('primes', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('avance_salaire', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_net', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement', models.DateField(auto_now_add=True)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('type_contrat', models.CharField(choices=[('CDI', 'Contrat à Durée Indéterminée'), ('CDD', 'Contrat à Durée Déterminée'), ('STAGE', 'Stage')], max_length=10)),
                ('date_publication', models.DateField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('PUBLIE', 'Publié'), ('EN_COURS', 'En Cours'), ('TERMINE', 'Terminé')], max_length=10)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.service')),
            ],
        ),
        migrations.CreateModel(
            name='Pointage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_pointage', models.DateField()),
                ('present', models.BooleanField(default=True)),
                ('conge', models.BooleanField(default=False)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_conge', models.CharField(choices=[('ANNUEL', 'Congé Annuel'), ('MALADIE', 'Congé Maladie'), ('MATERNITE', 'Congé Maternité'), ('PATERNITE', 'Congé Paternité'), ('SANS_SOLDE', 'Congé Sans Solde')], max_length=20)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('nb_jours', models.IntegerField()),
                ('justification', models.TextField(blank=True)),
                ('statut', models.CharField(choices=[('DEMANDE', 'Demandé'), ('APPROUVE', 'Approuvé'), ('REFUSE', 'Refusé')], max_length=10)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.service'),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_contrat', models.CharField(choices=[('CDI', 'Contrat à Durée Indéterminée'), ('CDD', 'Contrat à Durée Déterminée'), ('STAGE', 'Stage')], max_length=10)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('salaire_mensuel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salaire_journalier', models.DecimalField(decimal_places=2, max_digits=10)),
                ('archive', models.BooleanField(default=False)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_hr', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('verification_token', models.CharField(blank=True, max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
