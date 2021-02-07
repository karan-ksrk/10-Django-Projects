from django.shortcuts import render
from .models import Post
from marketing.models import Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q

def home(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by("-timestamp")[0:5]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    context= {
        'object_list': featured,
        'latest': latest
    }
    return render(request, 'Home/index.html', context)

def blog(request):
    post_list = Post.objects.order_by("-timestamp")
    paginator = Paginator(post_list, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginator_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginator_queryset = paginator.page(1)
    except EmptyPage:
        paginator_queryset = paginator.page(paginator.num_pages)


    context = {
        'queryset':paginator_queryset,
        'page_request_var' : page_request_var
    }
    return render(request, 'Home/news.html', context)


def post(request, id):
    return render(request, 'Home/post.html', {})


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'Home/search_result.html', context)