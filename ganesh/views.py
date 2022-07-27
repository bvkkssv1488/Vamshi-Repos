from django.shortcuts import render
from django.db import connection
from django.http.response import StreamingHttpResponse
from ganesh.models import Donation,Poojaevents
from django.contrib import messages
from ganesh.camera import VideoCamera,IPWebCam,LiveWebCam

def helloworld(request):
	return render(request,'Jai Ganesh 2022/home.html')

def function(request):
	return render(request,'Jai Ganesh 2022/donation.html')

def function1(request):
	return render(request,'Jai Ganesh 2022/poojaevents.html')

def cultural(request):
	return render(request,'Jai Ganesh 2022/cultural.html')
	
def live(request):
	return render(request,'Jai Ganesh 2022/live.html')
def list1(request):
    list1=Donation.objects.all()
    return render(request,'Jai Ganesh 2022/gotramlist.html',{'list':list1})
def list2(request):
	list2=Poojaevents.objects.raw('select * from ganesh_poojaevents ORDER BY Date ASC')
	return render(request,'Jai Ganesh 2022/pooja.html',{'list':list2})
def donation(request):

 if request.method=="POST":
    Gothram= request.POST['Gothram']
    LastName= request.POST['LastName']
    FirstName= request.POST['FirstName']
    SpouceName= request.POST['SpouceName']
    Child1= request.POST['Child1']
    Child2=request.POST['Child2']
    Amount=request.POST['Amount']
    print('Gothram',LastName,FirstName)
    ins=Donation(Gothram=Gothram,LastName=LastName,FirstName=FirstName,SpouceName=SpouceName,Child1=Child1,Child2=Child2,Amount=Amount)
    ins.save()
 return render(request,'Jai Ganesh 2022/donation.html')

def poojaevents(request):

 if request.method=="POST":
    Gotram= request.POST['Gotram']
    SurName= request.POST['SurName']
    Name= request.POST['Name']
    SpouseName= request.POST['SpouseName']
    Date=request.POST['Date']
    Time=request.POST['Time']
    cun=connection.cursor()

    cun.execute('select count(*) from ganesh_Poojaevents where Date="'+Date+'" and TIME="'+Time+'"')
    s=cun.fetchone()
    print(type(s[0]))

    if s[0]>=2:
       messages.success(request,"Slot is full please select available dates to check available date view poojaevents")

       return render(request,'Jai Ganesh 2022/bookpooja.html')
    else:
      ins=Poojaevents(Gotram=Gotram,SurName=SurName,Name=Name,SpouseName=SpouseName,Date=Date,Time=Time)
      ins.save()

 return render(request,'Jai Ganesh 2022/bookpooja.html')

def index(request):
    return render(request, 'Jai Ganesh 2022/live')

#Every time you call the phone and laptop camera method gets frame
#More info found in camera.py
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#Method for laptop camera
def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')


def livecam_feed(request):
   return StreamingHttpResponse(gen(LiveWebCam()),
               content_type='multipart/x-mixed-replace; boundary=frame')

