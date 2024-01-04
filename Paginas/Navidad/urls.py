from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index),
    path('afiliacion/',views.afiliacion),
    path('planEmpresarial/',views.planEmpresarial),
    path('superOfertas/',views.superOfertas),
    path ('beneficios/',views.beneficios),
    path('canastosyDespensas/',views.canastosyDespensas),
    path('trabajeconNosotros/',views.trabajeconNosotros),
    path('locales/',views.locales),
    path('productosSupermaxi/',views.productosSupermaxi),
    path('catalogos/',views.catalogos),
    path('responsabilidadSocial/',views.responsabilidadSocial),
    path('vinos/',views.vinos),
    path('maxiplus/',views.maxiplus),
    path('recetas/',views.recetas),
    path('maxinoticias/',views.maxinoticias)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
