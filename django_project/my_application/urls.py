from . import views
from django.urls import path

urlpatterns = [
    path("",views.home,name='home'),
    path("blist/<int:id>",views.book_list,name='book_list'),
    path("bdata/",views.book_data,name='book_data'),
    path("badd/",views.bookadd,name='bookadd'),
    path("sadd/",views.shopadd,name='shopadd'),
    path("sview/",views.sview,name='sview'),
    path("update/<int:id>",views.update,name='update'),
    path("delete/<int:id>",views.deletee,name='delete'),
    

]
