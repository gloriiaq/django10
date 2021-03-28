from django.shortcuts import render

# Create your views here.


def allblogs(request):
    blogs="my blogs"
    return render(request, "blog/allblogs.html", {"blogs":blogs})

