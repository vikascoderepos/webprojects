from django.db import models
from django.conf import settings
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import  USStateField
from django.urls import reverse



class Profile(models.Model):
    BOOL_CHOICES = ((True, 'Yes'),(False, 'No'))
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'))
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.TextField(max_length=500, blank=True)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = USStateField(choices = STATE_CHOICES)
    zip_code=models.CharField(max_length=32, db_index=True, blank=False)
    phone_number = PhoneNumberField(null=False, blank=False)
    created_date = models.DateTimeField(default=now, editable=False)
    is_parent = models.BooleanField(choices=BOOL_CHOICES, default=True)
    is_teacher = models.BooleanField(choices=BOOL_CHOICES, default=False)
    class Meta:
        ordering = ('zip_code',)
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'


    def __str__(self):
        return f'Profile for user {self.user.username}'

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])