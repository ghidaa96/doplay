from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import Show
def index(request):
    return redirect('/shows')
def shows(request):
    contex={
        'show':Show.objects.all()
    }
    return render(request,'show.html',contex)
def show(request, num):
    contex={
        'show':Show.objects.get(id=num)
    }
    return render(request,'showInfo.html',contex)
def shownew(request):
    return render(request,'new.html')
def newShow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len( errors )> 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title= request.POST['title']
        network= request.POST['network']
        date= request.POST['date']
        desc = request.POST['desc']
        show = Show.objects.create(title=title,network=network,release_date=date,desc=desc)
        show.save()
        messages.success(request, "Show added successfully")
        return redirect(f'/shows/{show.id}')
def edit(request,num): 
    contex={
        'num' : num
    }
    return render(request,"update.html",contex)
def update(request,num):
    errors = Show.objects.update_validator(request.POST,num)
    if len(errors )> 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{num}/edit')
    else:
        show = Show.objects.get(id=num)
        title= request.POST['title']
        network= request.POST['network']
        date= request.POST['date']
        desc = request.POST['desc']
        if show.title != title :
            show.title=title
        else:
            pass
        if show.network != network :
            show.network=network
            show.save()
        else:
            pass
        if show.release_date != date :
            show.release_date=date
            show.save()
        else:
            pass
        if show.desc != desc :
            show.desc=desc
            show.save()
        else:
            pass
        show.save()
        messages.success(request, "Show updated successfully", num)
        return redirect(f'/shows/{num}')
def destroy(request,num):
    show = Show.objects.get(id=num)
    show.delete()
    return redirect('/shows')