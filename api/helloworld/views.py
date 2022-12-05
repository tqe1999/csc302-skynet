from django.http import HttpResponse, FileResponse, JsonResponse, HttpResponseBadRequest
from helloworld.correlation import *
from helloworld.models import Stocks
from django.views.decorators.csrf import csrf_exempt
import json

stocks = list(set(Stocks.objects.values_list('stock', flat=True)))

def index(request):
    return HttpResponse("Hello, world!")

# This endpoint returns a list of stocks
def getStockList(request):
    return JsonResponse(list(stocks), safe=False)

# This endpoint returns an image, given the name of two stocks
@csrf_exempt
def getCorrelationGraph(request):
    
    stocks = []

    if request.method == "POST":
        print(request.POST)
        stocks = json.loads(request.POST["stocks"])
    elif request.method == "GET":
        stocks.append(request.GET["stock1"])
        stocks.append(request.GET["stock2"])
    else:
        return HttpResponseBadRequest()


    df = get_df(stocks)
    corr_df = get_correlation(df)
    img = render_matrix(corr_df)

    response = FileResponse(img, content_type="image/png")
    return response