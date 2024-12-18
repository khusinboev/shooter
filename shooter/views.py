from django.shortcuts import render
from django.http import HttpResponse
import os
from pathlib import Path

def index(request):
    #return HttpResponse(os.path.join(Path(__file__).resolve().parent)
    return render(request, "index.html")
def int_tir(request):
    return render(request, "int_tir.html")
def laser_tir(request):
    return render(request, "laser_tir.html")
def panarama(request):
    return render(request, "panarama.html")
def btr(request):
    return render(request, "btr.html")
def desant(request):
    return render(request, "desant.html")
def dpm(request):
    return render(request, "dpm.html")
def mobil(request):
    return render(request, "mobil.html")
def pzrk(request):
    return render(request, "pzrk.html")
def vr(request):
    return render(request, "vr.html")


def start_bot(request):
    # from bot.exarid import main
    # import asyncio
    #
    # asyncio.run(main.main())
    return HttpResponse("Done!")

# Create your views here.
