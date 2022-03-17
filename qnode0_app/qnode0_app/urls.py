from django.urls import path,re_path,include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
#from noticias.sitemaps import PostSitemap

#from baton.autodiscover import admin
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
#from qr_code import urls as qr_code_urls


#sitemaps = {
    #'posts': PostSitemap,
#}


urlpatterns = [
    #path(_('payment/'), include('payment.urls', namespace='payment')),
    #path(_('coupons/'), include('coupons.urls', namespace='coupons')),
    path('admin/', admin.site.urls),
    #path('sqaccounts/',include('sqaccounts.urls')),
    #path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    #path(_('ProFit/'), include('ProFit.urls')),
    #path(_('baton/'),include('baton.urls')),
    #path(_('cart/'), include('cart.urls', namespace='cart')),
    #path('edificios/', include('HOMEDETAIL.urls', namespace='edificio')),
    #path('cotizaciones/', include('HOMEDETAIL.urls', namespace='cotizacion')),
    #path('qr-code/', include(qr_code_urls, namespace="qr_code")),
    #path('services/', include('services.urls', namespace="services")),
    #path(_('noticias/'), include('noticias.urls', namespace='noticias')),
    #path(_('sitemap.xml'), sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    #path(_('social-auth/'), include('social_django.urls', namespace='social')),
    #path(_('images/'), include('images.urls', namespace='images')),
    #path(_('Orders/'), include('orders.urls', namespace='orders')),
    #path(_('cotizaciones_profit/'), include('cotizaciones.urls', namespace='cotizaciones')),
    
    
    #path(_('rosetta/'),include('rosetta.urls')),
    #path(_('Proyectos/'), include('Proyectos.urls', namespace='Proyectos')),

    

    re_path(r'^customers/', include(wagtailadmin_urls),name='wagtail'),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
