from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from users.forms import CustomUserCreationForm
from users.models import Blog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from users.forms import BlogForm
from django.db.models.functions import Lower, Coalesce

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))

def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")

def listing(request):
    data = {
        "blogs": Blog.objects.all().order_by(Coalesce('title', 'id').asc()),
    }

    return render(request, "blog/listing.html", data)

@login_required
@user_passes_test(lambda user: user.is_staff)
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("listing")
            except:
                pass
    else:
        form = BlogForm()

    return render(request, "blog/add_blog.html", {'form':form})

def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    data = {
        "blog": blog,
    }

    return render(request, "blog/view_blog.html", data)

@user_passes_test(lambda user: user.is_staff)
def edit_blog(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    form = BlogForm(request.POST, instance = blog)
    if form.is_valid():
        try:
            form.save()
            return redirect("listing")
        except:
            pass

    return render(request, "blog/edit_blog.html", {"blog": blog})

@login_required
def private_place(request):
    return HttpResponse("Shhh, members only!", content_type="text/plain")

@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("Employees must wash hands", content_type="text/plain")

@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello {username}")
    messages.add_message(request, messages.WARNING, "DANGER WILL ROBINSON")

    return HttpResponse("Messages added", content_type="text/plain")
