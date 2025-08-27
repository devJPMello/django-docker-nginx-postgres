from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import UploadForm
from .models import UploadedFile

def upload_view(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                uploaded_file = form.save()
                messages.success(
                    request, 
                    f'Arquivo "{uploaded_file.original_filename}" enviado com sucesso!'
                )
                return redirect("upload")
            except Exception as e:
                messages.error(
                    request, 
                    f'Erro ao enviar arquivo: {str(e)}'
                )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UploadForm()
    
    # Busca e paginação
    search_query = request.GET.get('search', '')
    if search_query:
        files = UploadedFile.objects.filter(
            Q(original_filename__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(file_type__icontains=search_query)
        ).order_by('-uploaded_at')
    else:
        files = UploadedFile.objects.all().order_by('-uploaded_at')
    
    # Paginação - 10 arquivos por página
    paginator = Paginator(files, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'form': form,
        'files': page_obj,
        'search_query': search_query,
        'total_files': files.count(),
        'total_size_mb': sum(f.file_size_mb for f in files),
    }
    
    return render(request, "upload.html", context)
