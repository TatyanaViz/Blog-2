import datetime
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Post
from .forms import PostForm


def index(request):
    latest_text_list = Post.objects.order_by('date_of_publication')[:10]
    template = loader.get_template('polls/index.html')
    #output = ' '.join(p.text for p in latest_text_list)
    context = RequestContext(request, {
        'latest_text_list': latest_text_list,
    })
    return HttpResponse(template.render(context))

def detail(request, text_id):
    post = get_object_or_404(Post, pk=text_id)
    return render(request, 'polls/detail.html',{'post':post})



def edit(request, obj_id=None):
    post = None
    if obj_id:
        post = get_object_or_404(Post, pk=obj_id)

    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.date_of_publication = datetime.datetime.now()
        post.save()
        return redirect(reverse('polls:detail', args=(post.id, )))

    context = {
       'form': form
    }
    return render(request, 'polls/edit.html', context)


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/polls/')
