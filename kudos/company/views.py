from django.shortcuts import render
from django.http import HttpResponse
from django.template import  RequestContext, loader


def signup(request):
	template = loader.get_template('company/signup.html')
	context = RequestContext(request, {
		'name': 'signup'
	})

	return HttpResponse(template.render(context))