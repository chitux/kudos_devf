from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from employee.forms import Signup, KudoForm
from employee.models import Employee, Kudo
from company.models import Company
from hashids import Hashids
from django.db.models import Count
import hashlib


# Employee views
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
        form = KudoForm()

        # get lasts kudos
        last_kudos = Kudo.objects.all().order_by('-id')[0:10]
        top_employees = Employee.objects.annotate(kudos=Count('kudo')).order_by('-kudos')[:3]

        return render(request, 'employee/home.html', {
            'form': form,
            'last_kudos': last_kudos,
            'top_employees': top_employees
        })


    def post(self, request):
        form = KudoForm(request.POST)

        # get lasts kudos
        last_kudos = Kudo.objects.all().order_by('-id')[0:10]
        top_employees = Employee.objects.annotate(kudos=Count('kudo')).order_by('-kudos')[:3]

        if form.is_valid():
            form.save()
            form = KudoForm()
        
        return render(request, 'employee/home.html', {
            'form': form,
            'last_kudos': last_kudos,
            'top_employees': top_employees
        })





















































