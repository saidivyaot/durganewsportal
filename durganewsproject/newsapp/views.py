from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'newsapp/index.html')


def moviesinfo(request):
    head_msg='Latest movie information'
    msg1='tabu is actcing in webseries'
    msg2='RRR is going bto release in jab 18 2022'
    msg3='Sarkaru vari pata is going to release in next summer'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg = 'Latest political information'
    msg1 = 'KCR is going to face big defeat in telangana at 2024 elections '
    msg2 = 'REVENANTH REDDY may be the next cm of telangana'
    msg3 = 'hope KTR in jail'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg = 'Latest sports information'
    msg1 = 'pak won by 10 wickets '
    msg2 = 'MSD is the mentor of team india'
    msg3 = 'Vamika is osm -virat'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request,'newsapp/news.html',context=my_dict)