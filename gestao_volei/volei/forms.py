from django.forms import ModelForm
from .models import Time, Jogador

class TimeForm(ModelForm):
    class Meta:
        model = Time
        fields = ['nome', 'cidade']

class JogadorForm(ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'idade', 'time']
