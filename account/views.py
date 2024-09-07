from django.shortcuts import render
# from django.http import HttpResponse ,HttpResponseRedirect
# from .forms import LoginForm
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # process the data in form.cleaned_data
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
            
            
#             # TODO: authenticate user and redirect to appropriate page
#             user = authenticate(username=username, password=password)

#             if user is not None:
                
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Successful Login')
#                 else:
#                     return HttpResponse("Invalid login credentials")
#             else:
#                 return HttpResponse("Invalid login")
#     else:
#         form = LoginForm()
    
    
#     return render(request,'account/login.html',{
#         'form': form,
#     })


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html',{
        'section': 'dashboard',
    })