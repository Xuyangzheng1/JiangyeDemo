from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse

from jiangyeapp.models import userinformation


def book(request):
    return HttpResponse('这是jiangyetest')

def book_detail(request,book_id):
    text = '图书id是 %s'% book_id
    return HttpResponse(text)

def test(request):
    return HttpResponse('testjaingyebook')

def test730(request):
    name="giao"
    datetime=datetime.now()
    return render(request,'index')


def register(request):
    if request.method == 'POST':
        username1 = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        age = request.POST.get('age')
        date = request.POST.get('date')
        time1 = request.POST.get('time')
        print(allow)
        # if allow !='on':
        #   return render(request,'register.html',{'errmsg':'huoyigeiwoligiaogiao'})
        uuu = userinformation.objects.create(
            name=username1, password=pwd, email=email, age=age, date=date, create_time=time1)
    # userinformationv.is_active()=0
        uuu.save()
        # 发送邮件
        subject = 'youjian'
        message = "huanying <br> <a href=''dianjijihuo"
        # res=send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[email,])
        # print(res)

        return redirect('http://localhost:8000/testjs/')
    return render(request, 'register.html')