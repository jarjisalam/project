from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs,Internship

# Create your views here.
def home(request):
    return render (request,'home.html')

def handleblog(request):
    posts=Blogs.objects.all
    context={"posts":posts}
    return render (request,'handleblog.html',context)


def about(request):
    return render (request,'about.html')

def internshipdetails(request):

    # if not request.user.is_authenticated:
    #     messages.warning(request,"Please login to access this page")
    #     return redirect(request,"/auth/login/")

    if request.method=="POST":
        fname=request.POST.get('name')
        fusn=request.POST.get('usn')
        femail=request.POST.get('email')
        fcollage=request.POST.get('cname')
        foffer=request.POST.get('offer')
        fstartdate=request.POST.get('startdate')
        fenddate=request.POST.get('enddate')
        fprojreport=request.POST.get('projreport')
        
        # converting uppercase
        # fname=fname.upper()
        # fusn=fusn.upper()
        # fcollage=fcollage.upper()
        # foffer=foffer.upper()
        # fprojreport=fprojreport.upper()
        
        query=Internship(fullname=fname,usn=fusn,email=femail,collage_name=fcollage,offer_stutas=foffer,start_date=fstartdate,end_date=fenddate,proj_report=fprojreport)
        query.save()
        messages.success(request,'Form is submitted Successfully')
        return redirect (request,'/internshipdetails')

    return render (request,'internship.html')

def contact(request):
    

    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('number')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,'Thanks for cantacting us. we will get by you soon')
        # messages.info(request,f'the name is {name}, & email is {email}, your number is {phoneno}, & your query is {desc}')
        return redirect ('/contact')
    
    return render (request,'contact.html')



def resume(request):
    return render (request,'resume.html')

