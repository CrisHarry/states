# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from states.models import states,countries

def index(request):
        c = countries.objects.all()
        #s = states.objects.all()
        return render(request, 'index.html',{'countries': c})#'states':s
def apple(request):
    #c = states.objects.all()
    s2 = request.GET.get('f')
    #print s2
    s = states.objects.filter(foreign__countries_name = s2)
    return render(request, 'index.html', {'states' :s})  # 'states':s



    # x = get_object_or_404(countries, pk=country_name)
    # # try:
    # #     selected_choice = x.states_set.get(pk=request.POST['s'])
    # # except:
    # #     raise Http404("Nothing found")
    # return render(request, 'index.html', {'x': x})
    # #
    # # x= countries.objects.get(countries, pk=1)
    # # # abc = get_object_or_404(countries, pk=country_name)
    # # # selected_choice = abc.option_set.get(pk=request.POST['choice'])
    # # #s = states.objects.all()
    # # s = country_name.states_set.filter(foreign__countries_name ='country_name')
    # # return render(request, 'index.html', {'states': s}, {'country_name':country_name})
    #, '_blank'







