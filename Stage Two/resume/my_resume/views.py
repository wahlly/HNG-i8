from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def index(request):
    # return render(request, 'index.html', {})
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'index.html', context)