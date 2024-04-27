from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html>
    <body bgcolor="yellow">
    <center>
    <h1 color="red">
    welcome to sravani
    </h1>
    </center>
    </body>
    <head>""")
    return res