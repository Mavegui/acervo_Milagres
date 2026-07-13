from django.db import models
from django.utils.text import slugify


def renomear_arquivo(instance, filename):
    extensao = filename.split('.')[-1]
    novo_nome = f"{slugify(instance.titulo)}.{extensao}"
    return novo_nome

class Foto(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Título"
    )
    descricao = models.TextField(
        max_length=400,
        verbose_name="Descrição/História"
    )

    CATEGORIAS_CHOICES = [
        ('REL', 'Religiosidade'),
        ('ARQ', 'Arquitetura e Urbanismo'),
        ('CUL', 'Cultura e Eventos'),
        ('PES', 'Personalidades'),
        ('PAI', 'Paisagens Naturais'),
        ('COT', 'Cotidiano'),
        ('SIM', 'Símbolos'),
        ('MON', 'Monumentos'),
    ]

    categoria = models.CharField(
        max_length=3,
        choices=CATEGORIAS_CHOICES,
        verbose_name="Categoria"
    )

    data_estimada = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de fundação (Estimada)"
    )
    credito = models.CharField(
        max_length=150,
        verbose_name="Cedido por / Fonte",
        help_text="Nome da pessoa ou orgão que disponibilizou a imagem."
    )

    imagem = models.ImageField(
        upload_to=renomear_arquivo,
        verbose_name="Arquivo da foto",
        max_length=500
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} [{self.get_categoria_display()}]"

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
