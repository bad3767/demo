from django.shortcuts import render,redirect,get_object_or_404
from.models import Book,Shops
from .forms import bookform

# Create your views here.
def home(request):
    return render (request,'home.html')



def book_list(request,id):
    hh=Book.objects.get(pk=id)
    return render (request,'book_list.html',{'aa':hh})

def book_data(request):
    kk=Book.objects.all()
    return render(request,'book_data.html',locals())

def bookadd(request):
    ss = Book()
    if request.method=='POST':
        if True:
            ss.b_name=request.POST.get('bname')
            ss.pub_date=request.POST.get('pubdate')
            ss.save()
            return redirect('/bdata/')
    return render(request,'bookadd.html')



def shopadd(request):
    zz={}
    dd = bookform(request.POST or None, request.FILES)
    if dd.is_valid():
        dd.save()
        return redirect('/sview')
    zz['qq']=dd
    return render(request,'shopadd.html',zz)

def sview(request):
    aa={}
    aa["data"] =Shops.objects.all()
    return render(request,"sview.html",aa)

def update(request,id):
    dd={}
    obj=get_object_or_404(Shops,pk=id)
    ss=bookform(request.POST , instance=obj)
    if ss.is_valid():
        ss.save()
        return redirect('/sview/')
    dd['o']=ss
    return render(request,'update.html',dd)

def deletee(request,id):
    
    obj=get_object_or_404(Shops,pk=id)
    if request.method=='POST':
        obj.delete()
        return redirect('/sview/')
    return render (request,'deletee.html')