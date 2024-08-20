from django.urls import path
from . import views
urlpatterns=[
path("",views.index,name="home"),
path("post/<int:id>",views.post,name="post"),
path("create",views.create,name="create"),
path("edit/<int:id>",views.edit,name="edit"),
path("delete/<int:id>",views.delete,name="delete"),
path("registration",views.registration,name="registration"),
path("logout",views.logout,name="logout")
]