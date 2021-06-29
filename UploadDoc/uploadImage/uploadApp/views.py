from django.shortcuts import render,HttpResponse
from .models import User


# Create your views here.
def index(request):
    users=User.objects.all()
    img_path=users[len(users)-1].pic
    # print("without url",img_path)
    # print("with url",img_path.url)
    # return HttpResponse(users)
    # pic_name=users[0].pic
    # print(pic_name)
    return render(request,'index.html',{'pic':users})

def uploadImage(request):
    print("Successful....!")
    # print(request.FILES)
    pic_data=request.FILES['image']
    user=User(pic=pic_data)
    user.save()
    return render(request,'index.html')