from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# views.py
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')   
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to your dashboard or desired URL
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadPDFForm
from .models import UploadedPDF

@login_required
def dashboard(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            UploadedPDF.objects.create(user=request.user, pdf_file=pdf_file)
            # Redirect to avoid form resubmission on page refresh
            return redirect('dashboard')
    else:
        form = UploadPDFForm()

    # Fetch all uploaded PDFs for the current user
    uploaded_pdfs = UploadedPDF.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {'form': form, 'uploaded_pdfs': uploaded_pdfs})






from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

@login_required
def update_profile(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # Create a profile if it doesn't exist
        profile = Profile(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Save profile data
            form.save()

            # Update user information
            user.first_name = form.cleaned_data['full_name'].split(' ')[0]
            user.last_name = form.cleaned_data['full_name'].split(' ')[-1]
            user.email = form.cleaned_data['email']
            user.save()

            # Redirect to the profile update success page or dashboard
            return redirect('dashboard')  # Replace 'dashboard' with your dashboard URL name
    else:
        # Populate the form with existing data
        form = ProfileForm(instance=profile, initial={
            'full_name': f'{user.first_name} {user.last_name}',
            'email': user.email,
        })

    return render(request, 'update_profile.html', {'form': form})



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def view_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'view_profile.html', {'user_profile': user_profile})


from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')  # Replace 'dashboard' with your dashboard URL name
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def voter_logout(request):
    logout(request)
    return redirect('user_login')  # You can specify the URL to redirect to after logout

