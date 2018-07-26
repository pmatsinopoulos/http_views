# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def current_datetime(request):
    now = datetime.now()
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Current DateTime</title>
        </head>
        <body>
            <h1>{}</h1>
        </body>
    </html>
    """.format(now)
    return HttpResponse(html, status=200)


def not_found(request):
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Current DateTime</title>
        </head>
        <body>
            <h1>{}</h1>
        </body>
    </html>    
    """.format('Not Found')
    return HttpResponseNotFound(html)
