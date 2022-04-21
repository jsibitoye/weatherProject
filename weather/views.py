from django.shortcuts import render
import json, urllib.request

# Create your views here.

#def index(request):
#    return render(request, 'index.htlm')

def index(request):
    if request.method=='POST':
        city = request.POST['city']
        sitelink = 'http://api.openweathermap.org/data/2.5/weather?q='
        api = '&appid=c3b282d8a7ba963e435e1dbbbfa84d63'
        res = urllib.request.urlopen(sitelink+city+api).read()
        json_data = json.loads(res)
        data = {

            "country_code": str(json_data['sys']['country']), 
            "rain": str(json_data['weather'][0]['description']),
            "coordinate": str(json_data['coord']['lon'])+ str(json_data['coord']['lat']),
            "temp":  str(json_data['main']['temp'])+'k',
            "pressure":  str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "city": city
        }
    else :
        city =''
        res = ''
        data =''

    return render (request, 'index.html', {'data': data})