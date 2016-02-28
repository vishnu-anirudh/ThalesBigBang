# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.views.generic import View

import sys

from .models import Question
from .forms import ContactForm
from .code_script import FileClone


#import pdb; pdb.set_trace()

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('kids_gui/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request):
    form_class = ContactForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():

            your_name = request.POST.get('your_name', '' )

            max_dist = request.POST.get('max_dist', '' )

            #Input for Left sensor
            #
            left_sensor=request.POST.get('left_sensor', '' )
            #Input for Left wheel
            #
            #IF Left_sensor is ON
            #
            left_wheel_1=request.POST.get('left_wheel_1', '' )
            #IF Left_sensor is OFF
            #
            left_wheel_2=request.POST.get('left_wheel_2', '' )
            

            #Input for Right sensor
            #
            right_sensor=request.POST.get('right_sensor', '' )

            #Input for Right wheel
            #
            #IF Right_sensor is ON
            #
            right_wheel_1=request.POST.get('right_wheel_1', '' )
            #IF Right_sensor is OFF
            #
            right_wheel_2=request.POST.get('right_wheel_2', '' )
            
            app=FileClone()
            app.main(your_name, max_dist, left_sensor, left_wheel_1, left_wheel_2, right_sensor, right_wheel_1, right_wheel_2)

            return HttpResponseRedirect('/home/')
	
    return render(request, 'kids_gui/detail.html', {'form': form_class,})

"""
contact_name = request.POST.get(
    'contact_name'
, '')
 
contact_email = request.POST.get(
    'contact_email'
, '')
form_content = request.POST.get('content', '')
"""