# models.py dentro de 'core'

from django.db import models
from django.core.validators import FileExtensionValidator
import os

class UploadedFile(models.Model):
    # Validações de arquivo
    ALLOWED_EXTENSIONS = ['txt', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 
                          'jpg', 'jpeg', 'png', 'gif', 'bmp', 'zip', 'rar', '7z']
    
    file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)],
        help_text='Arquivos permitidos: ' + ', '.join(ALLOWED_EXTENSIONS)
    )
    original_filename = models.CharField(max_length=255)
    file_size = models.BigIntegerField(help_text='Tamanho do arquivo em bytes')
    file_type = models.CharField(max_length=50, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, help_text='Descrição opcional do arquivo')
    
    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Arquivo Enviado'
        verbose_name_plural = 'Arquivos Enviados'
    
    def __str__(self):
        return self.original_filename
    
    def save(self, *args, **kwargs):
        if not self.original_filename and self.file:
            self.original_filename = os.path.basename(self.file.name)
        if not self.file_size and self.file:
            self.file_size = self.file.size
        if not self.file_type and self.file:
            self.file_type = os.path.splitext(self.file.name)[1][1:].upper()
        super().save(*args, **kwargs)
    
    @property
    def file_size_mb(self):
        """Retorna o tamanho do arquivo em MB"""
        return round(self.file_size / (1024 * 1024), 2)
    
    @property
    def file_extension(self):
        """Retorna a extensão do arquivo"""
        return os.path.splitext(self.original_filename)[1][1:].upper()
    
    def get_file_url(self):
        """Retorna a URL do arquivo"""
        if self.file:
            return self.file.url
        return None
