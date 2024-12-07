from django.shortcuts import render, redirect
from .models import Paste
from .forms import PasteForm

def paste_create(request):
    if request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paste_list')
    else:
        form = PasteForm()
    return render(request, 'polls/paste_form.html', {'form': form})

def paste_detail(request, slug):
    paste = Paste.objects.get(slug=slug)
    return render(request, 'polls/paste_detail.html', {'paste': paste})

def paste_list(request):
    pastes = Paste.objects.filter(is_public=True)
    return render(request, 'polls/paste_list.html', {'pastes': pastes})
