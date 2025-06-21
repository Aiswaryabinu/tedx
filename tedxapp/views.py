from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
#from django.contrib.auth.models import User

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import CustomUser

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']   # Include 'role' field in the form


def home(request):
    return render(request, 'index.html')  # Render a simple home page template



def register(request):
    if request.method == 'POST':
        form =CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()        # Since we are using UserCreationForm, it will handle the password hashing and user creation.
            login(request, user)
            return redirect('login')  
    else:
        initial_data = {'username':'','email':'', 'password1':'', 'password2':'', 'role':''}
        form = CustomUserCreationForm(initial=initial_data)
    return render(request, 'register.html', {'form': form})    
        
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # with password hashing 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)  
    return render(request, 'login.html', {'form': form})    


@login_required
def dashboard_view(request):
    if request.user.role == 'admin':
        return redirect('admin_dashboard')
    elif request.user.role == 'user':
        return redirect('user_dashboard')
    else:
        return HttpResponse("Unauthorized", status=401)


@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login') 

""" views for user registration, login, and dashboard access using Django REST Framework."""
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

"""with token refresh functionality for user login."""    

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer =   UserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

"""class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({'user': user_serializer.data,
                          'message': 'Welcome to the dashboard!'})"""