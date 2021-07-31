from django.shortcuts import render
from time import gmtime, strftime, time
from datetime import datetime
from django.utils import timezone
    
def time_display(request):
    context = {
        "title": "Hora Actual",
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "time2": datetime.now(),
        "time3": timezone.now(),
    }
    return render(request,'index.html', context)