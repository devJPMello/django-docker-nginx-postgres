from django import forms
from django.core.exceptions import ValidationError
from .models import UploadedFile
import os

class UploadForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Descrição opcional do arquivo...',
            'class': 'form-control'
        }),
        required=False,
        max_length=500,
        help_text='Máximo 500 caracteres'
    )
    
    class Meta:
        model = UploadedFile
        fields = ['file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.txt,.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.jpg,.jpeg,.png,.gif,.bmp,.zip,.rar,.7z'
            })
        }
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if file.size > 100 * 1024 * 1024:
                raise ValidationError('O arquivo não pode ser maior que 100MB.')
            
            allowed_extensions = UploadedFile.ALLOWED_EXTENSIONS
            file_extension = os.path.splitext(file.name)[1][1:].lower()
            
            if file_extension not in allowed_extensions:
                raise ValidationError(
                    f'Extensão de arquivo não permitida. '
                    f'Extensões permitidas: {", ".join(allowed_extensions).upper()}'
                )

            if file.size == 0:
                raise ValidationError('O arquivo não pode estar vazio.')
        
        return file
    
    def clean(self):
        cleaned_data = super().clean()
        file = cleaned_data.get('file')
        description = cleaned_data.get('description')
        
        if not file:
            raise ValidationError('É necessário selecionar um arquivo para upload.')
        
        return cleaned_data
