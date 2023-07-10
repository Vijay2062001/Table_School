from django.shortcuts import render

# Create your views here.

from app.models import *

from django.http import HttpResponse

def Insert_collage(request):
    tn=input('Enter The Collage Name' )
    To=Collage.objects.get_or_create(collage_name=tn)[0]
    To.save()
    return HttpResponse ('Created Collage')


def Insert_student(request):
    tn=input('Enter The Collage Name' )
    To=Collage.objects.get_or_create(collage_name=tn)[0]
    To.save()
    tn4=input('Enter The Student Name')
    tn5=input('Enter The Student id')
    tn6=input('Enter The Student rol')
    tn7=input('Enter The Student address')
    To1= Student.objects.get_or_create(collage_name=To,stusent_name=tn4,student_id=tn5,student_rol=tn6,student_address=tn7)[0]
    To1.save()
    return HttpResponse ('Created Student')

