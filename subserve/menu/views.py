from django.shortcuts import render, redirect
from .forms import MenuForm

# Create your views here.
def detail(request):
    menus=Menu.objects.all()
    menu=Menu()
    menu.menu_name = request.POST.get('menu_name')
    return render(request, 'detail.html', {'menus':menus})

def create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('/')
    else:
        form = MenuForm()
    return render(request, 'menu_form.html', {'form': form})
