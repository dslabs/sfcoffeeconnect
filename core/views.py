from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template('index.html')
    context = Context({
        'test_var': '8=====D', 
    })
    return HttpResponse(template.render(context))


def home(request):
    template = loader.get_template('home.html')
    context = Context({
        'member_count': '3200+',
	'success_rate': '90%',
    })
    return HttpResponse(template.render(context))
