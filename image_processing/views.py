from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from django.contrib import messages 
from .models import Upload
from .forms import SaveUploaded
from .utils import get_watermark_image
from pathlib import Path
import os

#connect database to diractries
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR,'media').replace('\\', '/')
IMAGES_ROOT = os.path.join(MEDIA_ROOT,'images/').replace('\\', '/')
OUTPUT_ROOT  = os.path.join(MEDIA_ROOT,'output/').replace('\\', '/')
WATERMARK_ROOT = os.path.join(MEDIA_ROOT,'watermarks/').replace('\\', '/')


def index(request):
    messages.info(request,'Here You can overlay watermark on a image.')
    #to delete trash data from models
    Upload.objects.all().delete()
    #to delete unusual images from input and output diracteries
    for root,dirs,files in os.walk(IMAGES_ROOT):
        for file in files:
            os.remove(IMAGES_ROOT+file)
    for root,dirs,files in os.walk(WATERMARK_ROOT):
        for file in files:
            os.remove(WATERMARK_ROOT+file)
    if request.method=="POST":
        submitted_form = SaveUploaded(request.POST, request.FILES)
        watermark = request.FILES['watermark']
        flag = request.POST.get('flag')
        alpha = request.POST.get('alpha')
        wat_url = WATERMARK_ROOT+watermark.name
        img_url = IMAGES_ROOT
        output_url = OUTPUT_ROOT
        if submitted_form.is_valid():
            submitted_form.save()
            filename = get_watermark_image(wat_url,img_url,output_url,int(flag),float(alpha))
            messages.success(request,'Conratulations! Saved.')
            return render(request,'main/index.html',{'src':'media/output/'+filename,'filename':filename})
        else:
            messages.error(request,'Error! You make mistake to fill information.')
    return render(request,'main/index.html',{'src':''})