from django.http import HttpResponse, FileResponse, JsonResponse
from helloworld.models import Stocks

stocks = Stocks.objects.values_list('stock', flat=True)

def index(request):
    return HttpResponse("Hello, world!")

# This endpoint returns a list of stocks
def getStockList(request):
    # return JsonResponse(["stock1", "stock2", "stock3"], safe=False)
    return JsonResponse(list(stocks), safe=False)

# This endpoint returns an image, given the name of two stocks
def getCorrelationGraph(request):
    stock1=request.GET["stock1"]
    stock2=request.GET["stock2"]

    img = open('hello.png', 'rb')
    response = FileResponse(img)
    return response