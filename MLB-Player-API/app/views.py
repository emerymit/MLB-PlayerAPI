from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):

    page = requests.get("http://m.bluejays.mlb.com/roster/40-man")
    names = []

    soup = BeautifulSoup(page.content, 'html.parser')

    player_Names = soup.find_all(class_="dg-name_display_first_last")


    for x in range(2, len(player_Names)):
        if(player_Names[x].find('a') != None):
            names.append(player_Names[x].find('a').get_text() + " ")


    return HttpResponse(names)