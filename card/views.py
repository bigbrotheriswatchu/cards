from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cards, Category
from .forms import TransForm, CardForm
from django.contrib import messages


def list_of_cards_by_category(request, category_slug):
    categories = Category.objects.all()
    card = Cards.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug__iexact=category_slug)
        card = card.filter(category=category)
        count = Cards.objects.filter(category=category).count()
        counts = str(count)

    template = 'card/list_by_category.html'
    context = {"categories": categories, "card": card, "category": category, 'counts': counts, }
    return render(request, template, context,)


def card_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        cards = Cards.objects.filter(text__icontains=search_query)

        result = search_query

        return render(request, 'card/search_result.html', context={'cards': cards, 'result': result })
    else:
        cards = Cards.objects.all()

    return render(request, 'card/card_list.html', context={
        'cards': cards,
    })


def category_list(request):
    categories = Category.objects.all()

    card = Cards.objects.count()
    count = str(card)

    return render(request, 'card/category_list.html', context={'categories': categories, "count": count, })


def card_detail(request, slug):
    card = get_object_or_404(Cards, slug=slug)

    if request.method == 'GET':
        form = TransForm(request.GET)

        if form.is_valid():
            result = form.cleaned_data['title']
            result2 = card.translate

            if result == result2:
                messages.success(request, 'awesome!')
            else:
                messages.error(request, 'try again')
            return redirect('card_detail', slug=slug)
    else:
        form = TransForm()
    return render(request, 'card/card_detail.html', context={
        'card': card, 'form': form,
    })


def new_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)

        if form.is_valid():
            card = form.save(commit=False)
            card.text = card.slug
            card.save()

        return redirect('card_detail', slug=card.slug)

    else:
        form = CardForm()

    return render(request, 'card/card_new.html', context={"form": form, })


def card_edit(request, slug):
    card = get_object_or_404(Cards, slug=slug)

    if request.method == 'POST':

        form = CardForm(request.POST, instance=card)

        if form.is_valid():
           card = form.save(commit=False)
           card.user = request.user
           card.save()

        return redirect('card_detail', slug=card.slug)
    else:
        form = CardForm(instance=card)
    return render(request, 'card/card_edit.html', context={'form': form, })


def card_delete(request, slug):
    try:
        card = get_object_or_404(Cards, slug=slug)
        card.delete()

        return redirect('card_delete_list')
    except card.DoesNotExist:
        return HttpResponseNotFound("<h2>Card not found</h2>")


def card_delete_list(request,):
    cards = Cards.objects.all()

    return render(request, 'card/card_delete.html', context={'cards': cards,})