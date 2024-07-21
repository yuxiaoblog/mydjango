from django.shortcuts import render,HttpResponse
from django.http import HttpResponseNotFound
from . import stu
import requests
import re

# Create your views here.

def index_view(request):
    if request.method == 'GET':
    
        return render(request,'mydjango/index.html')

    elif request.method == 'POST':
        if request.POST.get('password') == '1':
            


            url_list=[]
            regex = r"stage..."
            p = re.compile(regex)
            crux = p.findall(request.POST.get('urlpath'))

            crux = str(crux[0])

            regex_s = r"\d\d\d"
            p_s = re.compile(regex_s)
            crux_s = p_s.findall(crux)
            crux_s = str(crux_s[0])

            url = str(f'http://dxx.ahyouth.org.cn/api/peopleRankStage?table_name=reason_stage{crux_s}&level1=%E5%9C%B0%E5%B8%82&level2=%E8%8A%9C%E6%B9%96%E5%B8%82&level3=%E8%8A%9C%E6%B9%96%E8%81%8C%E4%B8%9A%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2%E5%9B%A2%E5%A7%94&level4=%E7%BD%91%E7%BB%9C%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2%E5%9B%A2%E5%A7%94&level5=%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C%E6%8A%80%E6%9C%AF%E4%B8%93%E4%B8%9A2022%E7%BA%A72%E7%8F%AD%E5%9B%A2%E6%94%AF%E9%83%A8')

            url_list.append(url)

            url_path = url_list[0]








            # url = f'http://dxx.ahyouth.org.cn/api/peopleRankStage?table_name=reason_stage235&level1=%E5%9C%B0%E5%B8%82&level2=%E8%8A%9C%E6%B9%96%E5%B8%82&level3=%E8%8A%9C%E6%B9%96%E8%81%8C%E4%B8%9A%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2%E5%9B%A2%E5%A7%94&level4=%E7%BD%91%E7%BB%9C%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2%E5%9B%A2%E5%A7%94&level5=%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C%E6%8A%80%E6%9C%AF%E4%B8%93%E4%B8%9A2022%E7%BA%A72%E7%8F%AD%E5%9B%A2%E6%94%AF%E9%83%A8'
            response = requests.get(url_path)   
            response = response.json() 
            Watcheds = response['list']['list']  
            Roster = []
            for i in stu.info:
                Roster.append(i['name'])
            Wh = []
            Not_in =  []
            Not_look = []
            for i in Watcheds: 
                Wh.append(i['username'])
            for i in Wh:
                if i != '':
                    if i not in Roster:
                        Not_in.append(i)
                        break
                else:
                    continue
            for i in stu.info:
                if i['name'] != '':
                    if i['name'] not in Wh:
                        Not_look.append(i)
                else:
                    continue

            return render(request,'mydjango/shuchu.html',{'per':Not_look})
        else:
            return HttpResponse("errrrrrror")
        

# def api(request):
#     return render(request,'mydjango/stu.json')

# def shuchu_view(request):
    
    
#     # if request.method == 'POST':
#         return render(request,'mydjango/shuchu.html')