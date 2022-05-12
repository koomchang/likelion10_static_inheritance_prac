from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .form import BlogForm

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    # 1. 데이터가 입력된 후 제출 버튼을 누르고 데이터 저장 -> POST
    # 2. 정보가 입력되지 않은 빈칸을 되어있는 페이지 보여주기 -> GET
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid(): #유효성검사
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form':form})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.contents = request.POST['contents']
    new_blog.image = request.FILES['image']
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = get_object_or_404(Blog, pk = id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = get_object_or_404(Blog, pk = id)
    update_blog.title = request.POST['title']
    update_blog.contents = request.POST['contents']
    update_blog.image = request.FILES['image']
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = get_object_or_404(Blog, pk = id)
    delete_blog.delete()
    return redirect('home')

def report(request, id):
    report_blog = get_object_or_404(Blog, pk = id)
    report_blog.report += 1
    if report_blog.report == 3:
        report_blog.delete()
        return render(request, 'report.html', {'blog':report_blog})
    report_blog.save()
    return render(request, 'report.html', {'blog':report_blog})
