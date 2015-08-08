from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime



from .models import Urls,UrlsForm

def index(request):
	tabla_urls=[]
	tabla_urls=Urls.objects.all().order_by('-date');
	
	msj=''
	if request.method == 'POST':
		form=UrlsForm(request.POST)
		if form.is_valid():
			url = form.cleaned_data['url']
			user = form.cleaned_data['user']
			now = datetime.datetime.now()
			if (url !='' and user !=''):
				urlObject = Urls(url=url, user=user, date=now)
				urlObject.save()
				msj='Foto agregada exitosamente'
			else:
				msj='Información Incompleta'
		else:
			msj='Por favor completar la información'
		
	else:
		form=UrlsForm()
	
	return render_to_response('index.html',{'form':form,'msj':msj,'galerias':tabla_urls,'request':request},context_instance=RequestContext(request))

