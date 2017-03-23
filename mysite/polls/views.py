from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from .models import Post


def index(request):
    latest_text_list = Post.objects.order_by('date_of_publication')[:3]
    template = loader.get_template('polls/index.html')
    #output = ' '.join(p.text for p in latest_text_list)
    context = RequestContext(request, {
        'latest_text_list': latest_text_list,
    })
    return HttpResponse(template.render(context))

def detail(request, text_id):
    post = get_object_or_404(Post, pk=text_id)
    return render(request, 'polls/detail.html',{'post':post})

def edit(request, text_id):
    post = get_object_or_404(Post, pk=text_id)
    return render(request, 'polls/edit.html', {'post': post})
