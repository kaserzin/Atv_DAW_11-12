from django.shortcuts import render, redirect, get_object_or_404
from .models import Time, Jogador
from .forms import TimeForm, JogadorForm

# Time Views
def time_list(request):
    times = Time.objects.all()
    return render(request, 'time_list.html', {'times': times})

def time_create(request):
    form = TimeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('time_list')
    return render(request, 'time_form.html', {'form': form})

def time_update(request, id):
    time = get_object_or_404(Time, id=id)
    form = TimeForm(request.POST or None, instance=time)
    if form.is_valid():
        form.save()
        return redirect('time_list')
    return render(request, 'time_form.html', {'form': form})

def time_delete(request, id):
    time = get_object_or_404(Time, id=id)
    if request.method == 'POST':
        time.delete()
        return redirect('time_list')
    return render(request, 'time_confirm_delete.html', {'time': time})

# Jogador Views
def jogador_list(request):
    jogadores = Jogador.objects.all()
    return render(request, 'jogador_list.html', {'jogadores': jogadores})

def jogador_create(request):
    form = JogadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('jogador_list')
    return render(request, 'jogador_form.html', {'form': form})

def jogador_update(request, id):
    jogador = get_object_or_404(Jogador, id=id)
    form = JogadorForm(request.POST or None, instance=jogador)
    if form.is_valid():
        form.save()
        return redirect('jogador_list')
    return render(request, 'jogador_form.html', {'form': form})

def jogador_delete(request, id):
    jogador = get_object_or_404(Jogador, id=id)
    if request.method == 'POST':
        jogador.delete()
        return redirect('jogador_list')
    return render(request, 'jogador_confirm_delete.html', {'jogador': jogador})
