from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponse
def hello_world(request):
    output = """
        <!DOCTYPE html>
        <html>
           <head>
           </head>
           <body>
               Hello World! <em style="color:LightSeaGreen;">{current_time}</em>
           </body>
        </html>
    """.format(current_time=datetime.now())

    return HttpResponse(output)
