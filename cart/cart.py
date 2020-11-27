from decimal import Decimal
from django.conf import settings
from account.models import Profile


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        profile_ids = self.cart.keys()
        # get the product objects and add them to the cart
        profiles = Profile.objects.filter(id__in=profile_ids)

        cart = self.cart.copy()
        for profile in profiles:
            cart[str(profile.id)]['profile'] = profile

        for item in cart.values():
            item['price'] = Decimal(2000)
            item['total_price'] = Decimal(2000)
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, profile, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        profile_id = str(profile.id)
        if profile_id not in self.cart:
            self.cart[profile_id] = {'quantity': 0,
                                      'price': 2000}
        if override_quantity:
            self.cart[profile_id]['quantity'] = quantity
        else:
            self.cart[profile_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, profile):
        """
        Remove a product from the cart.
        """
        profile_id = str(profile.id)
        if profile_id in self.cart:
            del self.cart[profile_id]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
            return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())