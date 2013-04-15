from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template('index.html')
    context = Context({
        'test_var': '8=====D', 
    })
    return HttpResponse(template.render(context))
