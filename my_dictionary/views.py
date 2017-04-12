from datetime import date

from django.http import HttpResponse

def index(request):
    today = date.today()
    return HttpResponse("Hello, word! - " + str(date.today()))


