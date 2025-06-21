from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import redirect

"""
Custom account adapter to redirect users based on their role after login."""

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        user = request.user
        if user.role == 'admin':
            return '/tedxapp/admin/dashboard/'
        else:
            return '/tedxapp/user/dashboard/'
