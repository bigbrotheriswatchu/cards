from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cards, Translate
from .forms import TransForm
from django.contrib import messages


def card_list(request):
    cards = Cards.objects.all()
    return render(request, 'card/card_list.html', context={'cards': cards})

def card_detail(request, pk):
    card = get_object_or_404(Cards, pk=pk)
    trans = get_object_or_404(Translate, pk=pk)

    if request.method == 'GET':
        form = TransForm(request.GET)

        if form.is_valid():
            result = form.cleaned_data['title']
            result2 = trans.title

            if result == result2:
                messages.success(request, 'awesome!')
            else:
                messages.error(request, 'try again')
            return redirect('card_detail', pk=pk)
    else:
        form = TransForm()
    return render(request, 'card/card_detail.html', context={
        'card': card, 'form': form,
    })



