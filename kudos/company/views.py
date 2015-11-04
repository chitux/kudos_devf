from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from company.forms import Signup
import hashlib
from hashids import Hashids



def signup(request):
    hashids = Hashids()

    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():
            company = form.save(commit=False)
            password = request.POST['password']
            company.password = hashlib.sha1(password.encode('utf8'))
            company.save()

            # update company, add invitation code
            company.invitation_code = hashids.encode(company.id)
            company.save()
            return redirect(reverse('company:home'))

    form = Signup()
    return render(request, 'company/signup.html', {'form': form})



def home (request):
    return HttpResponse('Welcome')