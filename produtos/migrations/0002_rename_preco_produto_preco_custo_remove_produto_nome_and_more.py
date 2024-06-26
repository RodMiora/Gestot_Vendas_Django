# Generated by Django 5.0.6 on 2024-06-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produtos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="produto",
            old_name="preco",
            new_name="preco_custo",
        ),
        migrations.RemoveField(
            model_name="produto",
            name="nome",
        ),
        migrations.AddField(
            model_name="produto",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("eletronicos", "Eletrônicos"),
                    ("roupas", "Roupas"),
                    ("moveis", "Móveis"),
                    ("casa_utensilios", "Casa e Utensílios"),
                    ("variados", "Variados"),
                ],
                default="variados",
                max_length=20,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="produto",
            name="valor_venda",
            field=models.DecimalField(decimal_places=2, default="0.00", max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="produto",
            name="descricao",
            field=models.CharField(max_length=200),
        ),
    ]
