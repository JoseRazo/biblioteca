from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(max_length=1000, help_text="Ingrese una breve descripción del libro")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn" target="_blank">Numero ISBN</a>')
    

    def __str__(self):
        return self.titulo
