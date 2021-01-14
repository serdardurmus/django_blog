from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    context = {
        "object_list": qs
    }
    return render(request, "blog/post_list.html", context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    # veya şu 3 kod aynı işi yapıyor
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  # author kısmı boş olmasın diye bu ifi yazdık Ya da kullanıcı kimse yazar da o olması gerekiyor
            post = form.save(commit=False)  # Datayı kaydet ama database e işleme demek bu
            post.author = request.user
            post.save()
            return redirect("blog:list")
    context = {
        'form': form
    }
    return render(request, "blog/post_create.html", context)