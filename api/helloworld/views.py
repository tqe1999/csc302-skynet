from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world!")

def getStockList(request):
    return JsonResponse(["stock1", "stock2", "stock3"], safe=False)
