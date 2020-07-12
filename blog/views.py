from django.shortcuts import render


def index(request):
    """
    首頁看有哪些功能
    """
    return render(
    	request,
    	'index.html',
    )
    

