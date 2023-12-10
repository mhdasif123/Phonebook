from django.urls import path
from.import views
from.views import update

urlpatterns=[
    path("",views.fun1),
    path("newcontact.html",views.fun2),
    path("display.html",views.fun3),
    path("update.html",views.fun4),
    path("delete.html",views.fun5),
    path("insert",views.insert),
    path("disply",views.display),
    path("updt",views.update),
    path("updtnb",views.updatenumber),
    path("dlt",views.delete),
]