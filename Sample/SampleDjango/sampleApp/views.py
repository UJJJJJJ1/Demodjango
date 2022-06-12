from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from sampleApp import models
import twstock
import random
import time


# Create your views here.
def sayhello(request):
    return HttpResponse('hello moto!')

def templateHello(request):
    now=datetime.now()
    return render(request,"HelloTemplate.html",locals())

def insert(request):
    codes = ['1301','1303','2317','2330','2412','2454','2603','2881','2882','6505']
    class_list = [models.s1301 , models.s1303 , models.s2317 , models.s2330 , models.s2412 , models.s2454 , models.s2603 , models.s2881 , models.s2882 ,models.s6505]
    for i, code in enumerate(codes):
        stock = twstock.Stock(code)
        data_list=[class_list[i](**(data._asdict())) for data in stock.fetch_from(2022,3)]
        class_list[i].objects.bulk_create(data_list)
    return HttpResponse('完成')

def fetch_from(self,year:int,month:int):
    self.raw_data=[]
    self.data=[]
    today = datetime.datetime.today()
    for year,month in self._month_year_iter(month,year,today.month,today.year):
        self.raw_data.append(self.fetcher.fetch(year,month,self.sid))
        self.data.extend(self.raw_data[-1]['data'])
        time.sleep(random.randint(5,10))
    return self.data