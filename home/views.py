from django.shortcuts import render
# Create your views here.

def home(request):
    context = {
            'texto':'equivalente ao compact',
            'title': 'teste de dados',
        }
    return render(
        request,
        'home/index.html',
        context,
    )