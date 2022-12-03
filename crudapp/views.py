from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    stud = Stduent.objects.all()
    return render(request,"home.html",{'stud':stud})


@csrf_exempt
def add(request):
    if request.method=="POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        btn = request.POST.get('btn')
        img = request.FILES.get("img")
        if btn=="save":
            student = Stduent.objects.create(name=name,mobile=mobile,img=img)
            student.save()
            stu = list(Stduent.objects.all().values())
            return JsonResponse({'status':1,'msg':"Data Saved Successfully","stu":stu})
        else:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            id = request.POST.get('btn')
            img = request.FILES.get("img")
            st = Stduent.objects.get(id=id)
            st.name = name
            st.mobile = mobile
            st.img=img
            st.save()
            std = list(Stduent.objects.all().values())
            return JsonResponse({"status":3,"msg":"Data Updated Successfully","std":std})


@csrf_exempt
def edit(request):
    id = request.POST.get('id')
    stud = Stduent.objects.filter(id=id).values()
    st = list(stud)
    return JsonResponse({"status":4,"msg":"Data Updated","st":st})


@csrf_exempt
def delete(request):
    id = request.POST.get('id')
    st = Stduent.objects.get(id=id)
    st.delete()
    s =list(Stduent.objects.all().values())
    return JsonResponse({"status":5,"msg":"Data Deleted!","s":s})