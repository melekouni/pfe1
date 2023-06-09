# Generated by Django 4.1.7 on 2023-04-25 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_rename_fermier_superviseur"),
    ]

    operations = [
        migrations.CreateModel(
            name="client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100, null=True)),
                ("e_mail", models.EmailField(max_length=100, null=True)),
                ("client_id", models.CharField(max_length=100, null=True, unique=True)),
                ("image", models.ImageField(null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="supervisor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100, null=True)),
                ("e_mail", models.EmailField(max_length=100, null=True)),
                (
                    "supervisor_id",
                    models.CharField(max_length=100, null=True, unique=True),
                ),
                ("image", models.ImageField(null=True, upload_to="")),
            ],
        ),
        migrations.DeleteModel(
            name="superviseur",
        ),
        migrations.AddField(
            model_name="client",
            name="supervisor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.supervisor",
            ),
        ),
    ]
