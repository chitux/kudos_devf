from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from company.forms import Signup, Login
from django.views.generic import View
from django.http import HttpResponse
from hashids import Hashids
import hashlib



class CompanySignup(View):
    def get(self, request):
        form = Signup()
        return render(request, 'company/signup.html', {'form': form})


    def post(self, request):
        hashids = Hashids()
        form = Signup(request.POST)

        if form.is_valid():
            company = form.save(commit=False)
            password = request.POST['password']
            company.password = hashlib.sha1(password.encode('utf8'))
            company.save()

            # update company, add invitation code
            company.invitation_code = hashids.encode(company.id)
            company.save()
            return redirect(reverse('company_home'))
        else:
            return render(request, 'company/signup.html', {'form': form})



class CompanyHome(View):
    def get(self, request):
        return HttpResponse("Company Home")
