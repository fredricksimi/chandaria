from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required #added
from .forms import UserUpdateForm, ProfileUpdateForm
from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
    'u_form':u_form,
    'p_form':p_form,
    "account_page":"active"
    }
    return render(request, 'users/profile.html', context)
