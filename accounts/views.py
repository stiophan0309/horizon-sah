from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from .forms import (UserLoginForm, UserRegistrationForm, ProfileForm,
                    UserUpdateForm)
from django.template.context_processors import csrf
from django.db import IntegrityError
from .models import Profile
from checkout.models import Order, OrderLineItem


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    try:
        user_id = request.user.pk
        currentprofile = Profile.objects.get(user=user_id)
        return render(request, 'profile.html', {'profile': currentprofile})
    except Profile.DoesNotExist:
        return render(request, 'profile.html')


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'registration.html', args)


@login_required(login_url=reverse_lazy("login"))
def edit_profile(request):
    """
    View to handle the form for a user to enter/edit their profile details
    """
    user_id = request.user.pk
    if request.method == 'POST':
        baseform = UserUpdateForm(request.POST, user=request.user)
        profile_form = ProfileForm(request.POST)
        if baseform.is_valid() and profile_form.is_valid():
            data = baseform.cleaned_data
            if baseform.fields["email"].has_changed(request.user.email,
                                                    data["email"]):
                request.user.email = data["email"]
                request.user.save()
            if (baseform.fields["current_password"].
                has_changed(None, data["current_password"]) or
                baseform.fields["new_password1"].
                has_changed(None, data["new_password1"]) or
                baseform.fields["new_password2"].
                    has_changed(None, data["new_password2"])):
                request.user.set_password(data["new_password1"])
                request.user.save()
                update_session_auth_hash(request, request.user)
            details = profile_form.save(commit=False)
            details.user = request.user
            try:
                details.save()
                return redirect(profile)
            except IntegrityError:
                details.pk = Profile.objects.get(user=user_id).pk
                details.save()
                messages.success(request,
                                 "You successfully updated your profile")
                return redirect(profile)
        else:
            messages.error(request, "Please correct the highlighted errors:")
    else:
        try:
            user_profile = Profile.objects.get(user=user_id)
            profile_form = ProfileForm(instance=user_profile)
        except Profile.DoesNotExist:
            profile_form = ProfileForm()
        baseform = UserUpdateForm(initial={"email": request.user.email})

    args = {"base_form": baseform, "profile_form": profile_form}
    args.update(csrf(request))
    return render(request, "editprofile.html", args)


def delete_profile(request):
    """
    This view renders the deleteprofile page
    where the user must confirm that they wish to delete their user/profile
    """
    user = request.user
    if request.method == "POST":
        user.delete()
        return redirect(reverse('index'))
    context = {
        "object": user
    }
    return render(request, "deleteprofile.html", context)
