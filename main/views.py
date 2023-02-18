from django.shortcuts import render

def mp_view(request):
    return render(request, 'main/mainpage.html', context={"title" : 'Главная страница'})
