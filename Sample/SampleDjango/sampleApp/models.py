from django.db import models

# Create your models here.
class s2330(models.Model): #台積電
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數

class s2317(models.Model): #鴻海
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數

class s2454(models.Model): #聯發科
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數

class s2412(models.Model): #中華電
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數

class s6505(models.Model): #台塑化
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數

class s2881(models.Model): #富邦金
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數
    
class s2603(models.Model): #長榮
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數

class s2882(models.Model): #國泰金
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數

class s1301(models.Model): #台塑
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數

class s1303(models.Model): #南亞
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數