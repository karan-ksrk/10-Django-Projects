from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductModelForm
# Create your views here.


# def bad_view(request, *args, **kwargs):
#     # print(dict(request.GET))
#     my_request_data = dict(request.GET)
#     new_product = my_request_data.get("new_product")
#     print(my_request_data, new_product)
#     if new_product[0].lower() == "true":
#         print("new product")
#         Product.objects.create(title=my_request_data.get('title')[0], content=my_request_data.get("content")[0])
#     return HttpResponse("Dont do this")





def search_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello KSRK!</h1>")
    query = request.GET.get('q')

    context = {"name": "Karan Singh", "query": query}
    qs = Product.objects.filter(title__icontains=query[0])
    print(query, qs)
    return render(request, 'home.html', context)
    
# def product_create_view(request, *args, **kwargs):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             # print(my_form.is_valid())
#             if my_form.is_valid():
#                 print(my_form.cleaned_data.get("title"))
#                 Product.objects.create(title=my_form.cleaned_data.get('title'))
#                 # print("post_data", post_data)
#     return render(request, 'form.html', {})

def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()

        # print(form.cleaned_data)
        # data = form.cleaned_data
        # Product.objects.create(**data)
        form = ProductModelForm()
        # return HttpResponseRedirect('/success')
        # return redirect('/success ')
    return render(request, 'form.html', {"form":form})

def product_detail_view(request, pk, **kwargs):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404 # render html page, witj HTTP status code
    # return HttpResponse(f"Product id  {obj.id}")
    return render(request, 'products/detail.html', {"Object": obj })



def product_list_view(request, *args, **kwargs):
    obj = Product.objects.all()
    context = {
        'object_list': obj
    }
    return render(request, 'products/list.html', context)

def product_api_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not Found"}) # render html page, witj HTTP status code
    return JsonResponse({"id":  obj.id})



