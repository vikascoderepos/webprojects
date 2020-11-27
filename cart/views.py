from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from account.models import Profile
from .cart import Cart
from .forms import CartAddProfileForm


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    profile = get_object_or_404(Profile, id=pk)
    form = CartAddProfileForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(profile=profile,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, profile_id):
    cart = Cart(request)
    profile = get_object_or_404(Profile, id=profile_id)
    cart.remove(profile)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProfileForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})