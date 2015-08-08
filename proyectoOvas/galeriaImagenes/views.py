from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Imagen

def home(request):
	
	list = Imagen.objects.all()
	template = loader.get_template('galeriaImagenes/home.html')
	context = RequestContext(request, {
        'list': list,
    })
	return HttpResponse(template.render(context))
