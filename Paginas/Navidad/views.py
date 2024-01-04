from django.shortcuts import render, redirect
import os
# Create your views here.
def index(request):
    return render(request,"index.html")
    redirect ('/')

def afiliacion(request):
    return render(request, "afiliacion.html")

def planEmpresarial(request):
    return render(request, "planEmpresarial.html")

def superOfertas(request):
    return render(request, "superOfertas.html")

def beneficios(request):
    return render(request, "beneficios.html")

def canastosyDespensas(request):
    return render (request, "canastosyDespensas.html")

def trabajeconNosotros (request):
    return render (request,"trabajeconNosotros.html")

def locales(request):
    return render(request,"locales.html")

def productosSupermaxi(request):
    return render(request,"productosSupermaxi.html")

def catalogos (request):
    return render (request,"catalogos.html")

def responsabilidadSocial (request):
    return render (request,"responsabilidadSocial.html")

def vinos (request):
    return render (request,"vinos.html")

def maxiplus (request):
    return render (request,"maxiplus.html")

def recetas (request):
    return render (request,"recetas.html")

def maxinoticias (request):
    return render (request,"maxinoticias.html")
