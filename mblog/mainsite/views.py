from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Post, Product

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

def about(request):
    html = '''
<!DOCTYPE html>
<html>
<head><title>About Myself</title></head>
<body>
<h2>Cho-Chun Huang</h2>
<hr>
<p> Hi, I am Cho-Chun Huang Ho. Nice to meet you!</p>
</body>
</html>
'''
    return HttpResponse(html)

def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    return render(request, 'disp.html', locals())
