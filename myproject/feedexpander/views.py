from django.shortcuts import render
from django.http import HttpResponse
import feedparser
from BeautifulSoup import BeautifulSoup
import urllib
#from bs4 import BeautifulSoup
from models import Persona, Tweet

# Create your views here.


def mifeed(request, username):
    url = "http://twitrss.me/twitter_user_to_rss/?user=" + username
    dicc = feedparser.parse(url)
    salida = ""

    for number in range(5):
        salida += dicc.entries[number].title + "<br>"
        
        urls = dicc.entries[number].title.split()
        for url in urls:
            if url.find("http") == False:
                url = url.split('&')[0]
                salida += "<li><a href=" + url + ">" + url + "</a></li>"
              
                bSoup = BeautifulSoup(urllib.urlopen(url).read())
                if (bSoup.p) != None:
                    salida += str(bSoup.p).decode('utf8') + "</br>"
                if (bSoup.img) != None:
                    salida += str(bSoup.img).decode('utf8') + "</br>"
        salida+= "</br>"
                
        try:
            fila = Persona.objects.get(name= username)
        except Persona.DoesNotExist:
            fila = Persona(name = username)
            fila.save()
            
        try:
            f = Tweet.objects.get(content= dicc.entries[number].title)
        except Tweet.DoesNotExist:
            f = Tweet(content= dicc.entries[number].title, url= dicc.entries[number].link, name=fila)
            f.save()



    return HttpResponse(salida)
