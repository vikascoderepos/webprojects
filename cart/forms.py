from django import forms


PROFILE_QUANTITY_CHOICES = [(i, str(i)) for i in range(0, 2)]


class CartAddProfileForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=(PROFILE_QUANTITY_CHOICES),
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)