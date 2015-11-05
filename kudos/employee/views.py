from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from employee.forms import Signup
from employee.models import Employee
from company.models import Company
from hashids import Hashids
import hashlib


# Create your views here.
class EmployeeSignup(View):
    def get(self, request, *args, **kwargs):
        form = Signup()

        return render(request, 'employee/signup.html', {
            'form': form,
            'company_id': kwargs['company_id'],
            'invitation_code': kwargs['invitation_code']
        })


    def post(self, request, *args, **kwargs):
        hashids = Hashids()
        company = Company.objects.get(invitation_code=request.POST['invitation_code'])
        form = Signup(request.POST, request.FILES)

        if company:
            if form.is_valid():
                form_commit = form.save(commit=False)
                form_commit.company_id = company
                form_commit.kudollars = 0.0
                password = request.POST['password']
                form_commit.password = hashlib.sha1(password.encode('utf8'))
                form_commit.save()
                return redirect(reverse('employee_home'))

        return render(request, 'employee/signup.html', {
            'form': form,
            'company_id': kwargs['company_id'],
            'invitation_code': kwargs['invitation_code']
        })


class EmployeeHome(View):
    def get(self, request):
        return render(request, 'employee/home.html')

