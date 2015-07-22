import json
from django.shortcuts import render_to_response, redirect, render
from django.views.generic import View
from django.contrib.auth.models import User


class HomePageView(View):

    def get(self, request):
        if request.user.is_anonymous():
            return redirect('/logout')
    	social_obj = request.user.social_auth.filter(provider='linkedin', user=request.user).first()
    	if social_obj:
            print social_obj.extra_data
            context = {"profile_details": social_obj.extra_data}
            return render(request, 'mylogins/profile.html', context)
        return redirect('/logout')