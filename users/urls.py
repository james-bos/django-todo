from django.conf.urls import url, include
from django.urls import path
from users.views import dashboard, register, user_info, listing, add_blog, edit_blog, view_blog, private_place, staff_place, add_messages

urlpatterns = [
    url('dashboard/', dashboard, name="dashboard"),
    url('accounts/', include("django.contrib.auth.urls")),
    url('register/', register, name="register"),
    url('oauth/', include("social_django.urls")),
    url('listing/', listing, name="listing"),
    url('add_blog/', add_blog, name="add_blog"),
    path('edit_blog/<int:blog_id>/', edit_blog, name="edit_blog"),
    path('view_blog/<int:blog_id>/', view_blog, name="view_blog"),
    path('user_info/', user_info),
    path("private_place/", private_place),
    path("staff_place/", staff_place),
    path("add_messages/", add_messages),
]