from django.shortcuts import render

# Create your views here.

def main_view(request):
    context = {}

    return render(request,'chat/main.html',context=context)

def home(request):
    context={}

    return render(request,'chat/base.html',context=context)


def msg_view(request):
    context={}

    return render(request,'chat/msg.html',context=context)
