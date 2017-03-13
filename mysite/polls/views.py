from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Post


def index(request):
    latest_text_list = Post.objects.order_by('date_of_publication')[:3]
    template = loader.get_template('polls/index.html')
    #output = ' '.join(p.text for p in latest_text_list)
    context = RequestContext(request, {
        'latest_text_list': latest_text_list,
    })
    return HttpResponse(template.render(context))