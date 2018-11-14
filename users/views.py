from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		#UserCreationForm is a built in form from django
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error