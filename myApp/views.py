from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import csv

# Create your views here.
def index(requset):
    return render(requset, 'index02.html')

def div(request):
    return render(request, 'div.html')

def map(request):
    return render(request, 'map.html')

def f(request):
    myString = str(request.POST.get('myString'))
    ret = myString + " world"
    print("hello")
    # 字典序列返回
    retDic = {"code": 0, "message": ret}
    return JsonResponse(retDic, safe=False)

# 刷新chart11
def refresh11(request):
    # myString = str(request.POST.get('myString'))
    ret = []
    # print("refresh11")
    with open('static/csv/data11.csv', 'r') as f:
        reader = csv.reader(f)
        # 遍历整个文件
        for row in reader:
            print(row)
            ret.append(row)

    # 字典序列返回
    retDic = {"code": 0, "message": ret}
    return JsonResponse(retDic, safe=False)

# 刷新chart13
def refresh13(request):
    ret = []
    with open('static/csv/data13.csv', 'r') as f:
        reader = csv.reader(f)
        # 遍历整个文件
        for row in reader:
            print(row)
            ret.append(row)

    # 字典序列返回
    retDic = {"code": 0, "message": ret}
    return JsonResponse(retDic, safe=False)

# 刷新chart21
def refresh21(request):
    ret = []
    with open('static/csv/data21.csv', 'r') as f:
        reader = csv.reader(f)
        # 遍历整个文件
        for row in reader:
            print(row)
            ret.append(row)

    # 字典序列返回
    retDic = {"code": 0, "message": ret}
    return JsonResponse(retDic, safe=False)

# 刷新chart23
def refresh23(request):
    ret = []
    with open('static/csv/data23.csv', 'r') as f:
        reader = csv.reader(f)
        # 遍历整个文件
        for row in reader:
            print(row)
            ret.append(row)

    # 字典序列返回
    retDic = {"code": 0, "message": ret}
    return JsonResponse(retDic, safe=False)

# 刷新chart31
def refresh31(request):
    ret = []
    with open('static/csv/data31.csv', 'r') as f:
        reader = csv.reader(f)
        # 遍历整个文件
        for row in reader:
            print(row)
            ret.append(row)

    # 字典序列返回
    retDic = {"code": 0, "message": ret}
    return JsonResponse(retDic, safe=False)

# 刷新chart33
def refresh33(request):
    ret = []
    with open('static/csv/data33.csv', 'r') as f:
        reader = csv.reader(f)
        # 遍历整个文件
        for row in reader:
            print(row)
            ret.append(row)

    # 字典序列返回
    retDic = {"code": 0, "message": ret}
    return JsonResponse(retDic, safe=False)