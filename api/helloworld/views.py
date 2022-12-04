from django.http import HttpResponse, FileResponse, JsonResponse
from helloworld.correlation import *
from helloworld.models import Stocks

stocks = list(set(Stocks.objects.values_list('stock', flat=True)))

def index(request):
    return HttpResponse("Hello, world!")

# This endpoint returns a list of stocks
def getStockList(request):
    return JsonResponse(list(stocks), safe=False)

# This endpoint returns an image, given the name of two stocks
def getCorrelationGraph(request):
    stock1=request.GET["stock1"]
    stock2=request.GET["stock2"]
    
    if request.method == "POST":
        print(request.POST)
        stocks = request.POST
        print(f"stocks: {stocks}")


    df = get_df(["ABCO", "AAP", "ABG", "AAL", "ABBV", "AAWW", "AA", "ABCB", "ABMD", "AAN", "AAON", "AAOI", "AAT", "A", "ABAX", "ABC", "AAPL", "AAMC", "ABFS", "ABM"])
    corr_df = get_correlation(df)
    img = render_matrix(corr_df)

    # img = open(img_file, 'rb')
    # img = open(img.read(), 'rb')
    response = FileResponse(img, content_type="image/png")
    return response