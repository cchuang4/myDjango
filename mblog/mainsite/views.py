from datetime import datetime
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Post

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
"""    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<hr>")
        post_lists.append("<small>" + post.body + "</small><br><br>") #str(post.body.encode('utf-8'))
    return HttpResponse(post_lists)
"""

def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')