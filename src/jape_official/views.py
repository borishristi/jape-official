from datetime import datetime

from django.shortcuts import render


def index_view(request):
    date = datetime.today()
    print(date)
    print(type(date))
    return render(request, 'index.html', context={"first_name": "Hristi", "date": date})