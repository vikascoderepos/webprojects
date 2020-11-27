from cart.forms import CartAddProfileForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm


from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Profile
from django.contrib.auth.models import User
from .serializers import ProfileSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        profile_serializer = ProfileSerializer(user.profile)
        return Response(profile_serializer.data)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


# @login_required
# def dashboard(request):
#     return render(request,
#                   'account/dashboard.html',
#                   {'section': 'dashboard'})

@login_required
def dashboard(request):
    profiles = Profile.objects.filter(is_teacher=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(profiles, 10)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        profiles = paginator.page(1)
    except EmptyPage:
        profiles = paginator.page(paginator.num_pages)
    context = {
        'profiles': profiles
    }
    return render(request,
                  'account/dashboard.html',context
                  )

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})




@login_required
def profile_detail(request, pk):
    profile = Profile.objects.get(id=pk)
    cart_profile_form = CartAddProfileForm()
    context = {
        'profile': profile
    }
    # return render(request, 'account/profile_detail.html', context, 
    #             'cart_profile_form': cart_profile_form)


    return render(request,
                  'account/profile_detail.html',
                  {'profile': profile,
                   'cart_profile_form': cart_profile_form})


@login_required
def about_view(request):
    return render(request, 'account/about.html')


@login_required
def contact_view(request):
    return render(request, 'account/contact.html')