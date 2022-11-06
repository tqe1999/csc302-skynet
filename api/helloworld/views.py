from django.http import HttpResponse, FileResponse, JsonResponse

def index(request):
    return HttpResponse("Hello, world!")

def getStockList(request):
    return JsonResponse(["stock1", "stock2", "stock3"], safe=False)

def getCorrelationGraph(request):
    stock1=request.GET["stock1"]
    stock2=request.GET["stock2"]

    img = open('hello.png', 'rb')
    response = FileResponse(img)
    return response