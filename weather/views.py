from django.shortcuts import render
import requests


# Create your views here.
def weather_view(request):
    context={}
    if request.method=='POST':
        data=request.POST
        city=data.get('city')
        URL=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=98b43cecd25bb5ae95501199abcf12f9'
        resp=requests.get(url=URL)
        w_data=resp.json()
        if w_data['cod']==200:
            context={
                'w_data':w_data
                }
        else:
            context={'error':'Enter a proper City Name'}

    return render(request,'weather.html',context)