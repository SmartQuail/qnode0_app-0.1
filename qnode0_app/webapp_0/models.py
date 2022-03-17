import datetime
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.functional import cached_property
from django.http import Http404
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag as TaggitTag
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from streams import blocks
#from wagtail.core import blocks
from wagtail.core.models import Page,Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField, RichTextField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtailmetadata.models import MetadataPageMixin

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting



    



# pagina de inicio
class consultas(AbstractFormField):
    page = ParentalKey('index', on_delete=models.CASCADE, related_name='form_fields')

class Index(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp_0/index.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de Galerias
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')
    banner_title6 = RichTextField(blank=True,verbose_name='Titulo de galeria-3  ')
    banner_title7 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')

    # Empieza Banner de Tearsheet
    TS_info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-1 info')
    TS_date1 = models.DateField("Fecha de Tearsheet-1",null=True, blank=True)
    TS_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-2 info')
    TS_date2 = models.DateField("Fecha de Tearsheet-2",null=True, blank=True)
    TS_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-3 info')
    TS_date3 = models.DateField("Fecha de Tearsheet-3",null=True, blank=True)
    TS_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-4 info')
    TS_date4 = models.DateField("Fecha de Tearsheet-4",null=True, blank=True)
    TS_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-5 info')
    TS_date5 = models.DateField("Fecha de Tearsheet-5",null=True, blank=True)
    TS_info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-6 info')
    TS_date6 = models.DateField("Fecha de Tearsheet-6",null=True, blank=True)
    TS_info7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-7 info')
    TS_date7 = models.DateField("Fecha de Tearsheet-7",null=True, blank=True)
    TS_info8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-8 info')
    TS_date8 = models.DateField("Fecha de Tearsheet-8",null=True, blank=True)
    TS_info9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-9 info')
    TS_date9 = models.DateField("Fecha de Tearsheet-9",null=True, blank=True)
    TS_info10 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-10 info')
    TS_date10 = models.DateField("Fecha de Tearsheet-10",null=True, blank=True)
    TS_info11 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-11 info')
    TS_date11 = models.DateField("Fecha de Tearsheet-11",null=True, blank=True)
    TS_info12 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-12 info')
    TS_date12 = models.DateField("Fecha de Tearsheet-12",null=True, blank=True)
    TS_info13 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-13 info')
    TS_date13 = models.DateField("Fecha de Tearsheet-13",null=True, blank=True)
    TS_info14 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-14 info')
    TS_date14 = models.DateField("Fecha de Tearsheet-14",null=True, blank=True)
    TS_info15 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-15 info')
    TS_date15 = models.DateField("Fecha de Tearsheet-15",null=True, blank=True)
    TS_info16 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-16 info')
    TS_date16 = models.DateField("Fecha de Tearsheet-16",null=True, blank=True)
    TS_info17 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-17 info')
    TS_date17 = models.DateField("Fecha de Tearsheet-17",null=True, blank=True)
    TS_info18 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-18 info')
    TS_date18 = models.DateField("Fecha de Tearsheet-18",null=True, blank=True)
    TS_info19 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-19 info')
    TS_date19 = models.DateField("Fecha de Tearsheet-19",null=True, blank=True)
    TS_info20 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-20 info')
    TS_date20 = models.DateField("Fecha de Tearsheet-20",null=True, blank=True)
    
    #Campos de Noticias

    #template = "webapp_0/index.html"
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

       # FieldPanel('title', classname="full"),
      #  FieldPanel('cliente_Navbar', classname="full"),
      #  FieldPanel('banner_info1', classname="full"),
      #  FieldPanel('banner_title2', classname="full"),
      #  FieldPanel('banner_info2', classname="full"),
      #  FieldPanel('banner_title3', classname="full"),
      #  FieldPanel('banner_info3', classname="full"),
    #Panel Gelerias
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('banner_title7', classname="full"),
    #Tearsheet Info
        FieldPanel('TS_info1', classname="full"),
        FieldPanel('TS_date1', classname="full"),
        FieldPanel('TS_info2', classname="full"),
        FieldPanel('TS_date2', classname="full"),
        FieldPanel('TS_info3', classname="full"),
        FieldPanel('TS_date3', classname="full"),
        FieldPanel('TS_info4', classname="full"),
        FieldPanel('TS_date4', classname="full"),
        FieldPanel('TS_info5', classname="full"),
        FieldPanel('TS_date5', classname="full"),
        FieldPanel('TS_info6', classname="full"),
        FieldPanel('TS_date6', classname="full"),
        FieldPanel('TS_info7', classname="full"),
        FieldPanel('TS_date7', classname="full"),
        FieldPanel('TS_info8', classname="full"),
        FieldPanel('TS_date8', classname="full"),
        FieldPanel('TS_info9', classname="full"),
        FieldPanel('TS_date9', classname="full"),
        FieldPanel('TS_info10', classname="full"),
        FieldPanel('TS_date10', classname="full"),
        FieldPanel('TS_info11', classname="full"),
        FieldPanel('TS_date11', classname="full"),
        FieldPanel('TS_info12', classname="full"),
        FieldPanel('TS_date12', classname="full"),
        FieldPanel('TS_info13', classname="full"),
        FieldPanel('TS_date13', classname="full"),
        FieldPanel('TS_info14', classname="full"),
        FieldPanel('TS_date14', classname="full"),
        FieldPanel('TS_info15', classname="full"),
        FieldPanel('TS_date15', classname="full"),
        FieldPanel('TS_info16', classname="full"),
        FieldPanel('TS_date16', classname="full"),
        FieldPanel('TS_info17', classname="full"),
        FieldPanel('TS_date17', classname="full"),
        FieldPanel('TS_info18', classname="full"),
        FieldPanel('TS_date18', classname="full"),
        FieldPanel('TS_info19', classname="full"),
        FieldPanel('TS_date19', classname="full"),
        FieldPanel('TS_info20', classname="full"),
        FieldPanel('TS_date20', classname="full"),
#panel para campos de consulta
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = NewsDetailPage.objects.live().public()
        return context
        

class GaleriadeImagenes(Orderable):
    page = ParentalKey(Index, on_delete=models.CASCADE, related_name='galleria')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    profile_pic = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')
    image_4_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_5_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_6_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')
    image_7_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_8_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_9_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')
    image_10_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')
    
    # Imagenes Thumb Portfolio
    
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Advertising Thumb-Galeria')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Product Thumb2-Galeria')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Documentary Thumb3-Galeria')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Landscape Thumb4-Galeria')

    # Fotos TearSheate
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-1')
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-2')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-3')
    image_11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-4')
    image_12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-5 ')
    image_13 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-6')
    image_14 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-7')
    image_15 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-8')
    image_16 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-9')
    image_17 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-10')
    image_18 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-11')
    image_19 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-12')
    image_20 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-13')
    image_21 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-14')
    image_22 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-15')
    image_23 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-16')
    image_24 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-17')
    image_25 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-18')
    image_26 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-19')
    image_27 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-20')
     

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('profile_pic'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4_2'),
        ImageChooserPanel('image_5_2'),
        ImageChooserPanel('image_6_2'),
        ImageChooserPanel('image_7_2'),
        ImageChooserPanel('image_8_2'),
        ImageChooserPanel('image_9_2'),
        ImageChooserPanel('image_10_2'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image_9'),
        ImageChooserPanel('image_10'),
        ImageChooserPanel('image_11'),
        ImageChooserPanel('image_12'),
        ImageChooserPanel('image_13'),
        ImageChooserPanel('image_14'),
        ImageChooserPanel('image_15'),
        ImageChooserPanel('image_16'),
        ImageChooserPanel('image_17'),
        ImageChooserPanel('image_18'),
        ImageChooserPanel('image_19'),
        ImageChooserPanel('image_20'),
        ImageChooserPanel('image_21'),
        ImageChooserPanel('image_22'),
        ImageChooserPanel('image_23'),
        ImageChooserPanel('image_24'),
        ImageChooserPanel('image_25'),
        ImageChooserPanel('image_26'),
        ImageChooserPanel('image_27'),
        
    ]


class consultas_publicidad(AbstractFormField):
    page = ParentalKey('publicidad', on_delete=models.CASCADE, related_name='form_fields')

class publicidad(AbstractEmailForm):
    # Empieza Galeria de Imagenes
    template = "webapp_0/publicidad.html"
    Ad_info = models.CharField(max_length= 500, null=True, blank=True,verbose_name='Advertising info')
    Ad_link = RichTextField(blank=True,verbose_name='Enlace para volver al inicio')
    Ad_info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-1 info')
    Ad_date1 = models.DateField("Fecha de Advertising-1",null=True, blank=True)
    Ad_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-2 info')
    Ad_date2 = models.DateField("Fecha de Advertising-2",null=True, blank=True)
    Ad_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-3 info')
    Ad_date3 = models.DateField("Fecha de Advertising-3",null=True, blank=True)
    Ad_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-4 info')
    Ad_date4 = models.DateField("Fecha de Advertising-4",null=True, blank=True)
    Ad_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-5 info')
    Ad_date5 = models.DateField("Fecha de Advertising-5",null=True, blank=True)
    Ad_info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-6 info')
    Ad_date6 = models.DateField("Fecha de Advertising-6",null=True, blank=True)
    Ad_info7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-7 info')
    Ad_date7 = models.DateField("Fecha de Advertising-7",null=True, blank=True)
    Ad_info8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-8 info')
    Ad_date8 = models.DateField("Fecha de Advertising-8",null=True, blank=True)
    Ad_info9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-9 info')
    Ad_date9 = models.DateField("Fecha de Advertising-9",null=True, blank=True)
    Ad_info10 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-10 info')
    Ad_date10 = models.DateField("Fecha de Advertising-10",null=True, blank=True)
    Ad_info11 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-11 info')
    Ad_date11 = models.DateField("Fecha de Advertising-11",null=True, blank=True)
    Ad_info12 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-12 info')
    Ad_date12 = models.DateField("Fecha de Advertising-12",null=True, blank=True)
    Ad_info13 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-13 info')
    Ad_date13 = models.DateField("Fecha de Advertising-13",null=True, blank=True)
    Ad_info14 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-14 info')
    Ad_date14 = models.DateField("Fecha de Advertising-14",null=True, blank=True)
    Ad_info15 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-15 info')
    Ad_date15 = models.DateField("Fecha de Advertising-15",null=True, blank=True)
    Ad_info16 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-16 info')
    Ad_date16 = models.DateField("Fecha de Advertising-16",null=True, blank=True)
    Ad_info17 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-17 info')
    Ad_date17 = models.DateField("Fecha de Advertising-17",null=True, blank=True)
    Ad_info18 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-18 info')
    Ad_date18 = models.DateField("Fecha de Advertising-18",null=True, blank=True)
    Ad_info19 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-19 info')
    Ad_date19 = models.DateField("Fecha de Advertising-19",null=True, blank=True)
    Ad_info20 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-20 info')
    Ad_date20 = models.DateField("Fecha de Advertising-20",null=True, blank=True)
    Ad_info21 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-21 info')
    Ad_date21 = models.DateField("Fecha de Advertising-21",null=True, blank=True)
    Ad_info22 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-22 info')
    Ad_date22 = models.DateField("Fecha de Advertising-22",null=True, blank=True)
    Ad_info23 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-23 info')
    Ad_date23 = models.DateField("Fecha de Advertising-23",null=True, blank=True)
    Ad_info24 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-24 info')
    Ad_date24 = models.DateField("Fecha de Advertising-24",null=True, blank=True)
    Ad_info25 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-25 info')
    Ad_date25 = models.DateField("Fecha de Advertising-25",null=True, blank=True)
    Ad_info26 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-26 info')
    Ad_date26 = models.DateField("Fecha de Advertising-26",null=True, blank=True)
    Ad_info27 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-27 info')
    Ad_date27 = models.DateField("Fecha de Advertising-27",null=True, blank=True)
    Ad_info28 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-28 info')
    Ad_date28 = models.DateField("Fecha de Advertising-28",null=True, blank=True)
    Ad_info29 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-29 info')
    Ad_date29 = models.DateField("Fecha de Advertising-29",null=True, blank=True)
    Ad_info30 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-30 info')
    Ad_date30 = models.DateField("Fecha de Advertising-30",null=True, blank=True)
    Ad_info31 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-31 info')
    Ad_date31 = models.DateField("Fecha de Advertising-31",null=True, blank=True)
    Ad_info32 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-32 info')
    Ad_date32 = models.DateField("Fecha de Advertising-32",null=True, blank=True)
    Ad_info33 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-33 info')
    Ad_date33 = models.DateField("Fecha de Advertising-33",null=True, blank=True)
    Ad_info34 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-34 info')
    Ad_date34 = models.DateField("Fecha de Advertising-34",null=True, blank=True)
    Ad_info35 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-35 info')
    Ad_date35 = models.DateField("Fecha de Advertising-35",null=True, blank=True)
    Ad_info36 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-36 info')
    Ad_date36 = models.DateField("Fecha de Advertising-36",null=True, blank=True)
    Ad_info37 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-37 info')
    Ad_date37 = models.DateField("Fecha de Advertising-37",null=True, blank=True)
    Ad_info38 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-38 info')
    Ad_date38 = models.DateField("Fecha de Advertising-38",null=True, blank=True)
    Ad_info39 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-39 info')
    Ad_date39 = models.DateField("Fecha de Advertising-39",null=True, blank=True)
    Ad_info40 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-40 info')
    Ad_date40 = models.DateField("Fecha de Advertising-40",null=True, blank=True)
    Ad_info41 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-41 info')
    Ad_date41 = models.DateField("Fecha de Advertising-41",null=True, blank=True)
    Ad_info42 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-42 info')
    Ad_date42 = models.DateField("Fecha de Advertising-42",null=True, blank=True)
    Ad_info43 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-43 info')
    Ad_date43 = models.DateField("Fecha de Advertising-43",null=True, blank=True)
    Ad_info44 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-44 info')
    Ad_date44 = models.DateField("Fecha de Advertising-44",null=True, blank=True)
    Ad_info45 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-45 info')
    Ad_date45 = models.DateField("Fecha de Advertising-45",null=True, blank=True)
    Ad_info46 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-46 info')
    Ad_date46 = models.DateField("Fecha de Advertising-46",null=True, blank=True)
    Ad_info47 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-47 info')
    Ad_date47 = models.DateField("Fecha de Advertising-47",null=True, blank=True)
    Ad_info48 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-48 info')
    Ad_date48 = models.DateField("Fecha de Advertising-48",null=True, blank=True)
    Ad_info49 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-49 info')
    Ad_date49 = models.DateField("Fecha de Advertising-49",null=True, blank=True)
    Ad_info50 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-50 info')
    Ad_date50 = models.DateField("Fecha de Advertising-50",null=True, blank=True)
    Ad_info51 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-51 info')
    Ad_date51 = models.DateField("Fecha de Advertising-51",null=True, blank=True)
    Ad_info52 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-52 info')
    Ad_date52 = models.DateField("Fecha de Advertising-52",null=True, blank=True)
    Ad_info53 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-53 info')
    Ad_date53 = models.DateField("Fecha de Advertising-53",null=True, blank=True)
    Ad_info54 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-54 info')
    Ad_date54 = models.DateField("Fecha de Advertising-54",null=True, blank=True)
    Ad_info55 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-55 info')
    Ad_date55 = models.DateField("Fecha de Advertising-55",null=True, blank=True)
    Ad_info56 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-56 info')
    Ad_date56 = models.DateField("Fecha de Advertising-56",null=True, blank=True)
    Ad_info57 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-57 info')
    Ad_date57 = models.DateField("Fecha de Advertising-57",null=True, blank=True)
    Ad_info58 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-58 info')
    Ad_date58 = models.DateField("Fecha de Advertising-58",null=True, blank=True)
    Ad_info59 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-59 info')
    Ad_date59 = models.DateField("Fecha de Advertising-59",null=True, blank=True)
    Ad_info60 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-60 info')
    Ad_date60 = models.DateField("Fecha de Advertising-60",null=True, blank=True)
    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    
    
    
    content_panels = Page.content_panels + [
        FieldPanel('Ad_info', classname="full"),
        FieldPanel('Ad_link', classname="full"),
        FieldPanel('Ad_info1', classname="full"),
        FieldPanel('Ad_date1', classname="full"),
        FieldPanel('Ad_info2', classname="full"),
        FieldPanel('Ad_date2', classname="full"),
        FieldPanel('Ad_info3', classname="full"),
        FieldPanel('Ad_date3', classname="full"),
        FieldPanel('Ad_info4', classname="full"),
        FieldPanel('Ad_date4', classname="full"),
        FieldPanel('Ad_info5', classname="full"),
        FieldPanel('Ad_date5', classname="full"),
        FieldPanel('Ad_info6', classname="full"),
        FieldPanel('Ad_date6', classname="full"),
        FieldPanel('Ad_info7', classname="full"),
        FieldPanel('Ad_date7', classname="full"),
        FieldPanel('Ad_info8', classname="full"),
        FieldPanel('Ad_date8', classname="full"),
        FieldPanel('Ad_info9', classname="full"),
        FieldPanel('Ad_date9', classname="full"),
        FieldPanel('Ad_info10', classname="full"),
        FieldPanel('Ad_date10', classname="full"),
        FieldPanel('Ad_info11', classname="full"),
        FieldPanel('Ad_date11', classname="full"),
        FieldPanel('Ad_info12', classname="full"),
        FieldPanel('Ad_date12', classname="full"),
        FieldPanel('Ad_info13', classname="full"),
        FieldPanel('Ad_date13', classname="full"),
        FieldPanel('Ad_info14', classname="full"),
        FieldPanel('Ad_date14', classname="full"),
        FieldPanel('Ad_info15', classname="full"),
        FieldPanel('Ad_date15', classname="full"),
        FieldPanel('Ad_info16', classname="full"),
        FieldPanel('Ad_date16', classname="full"),
        FieldPanel('Ad_info17', classname="full"),
        FieldPanel('Ad_date17', classname="full"),
        FieldPanel('Ad_info18', classname="full"),
        FieldPanel('Ad_date18', classname="full"),
        FieldPanel('Ad_info19', classname="full"),
        FieldPanel('Ad_date19', classname="full"),
        FieldPanel('Ad_info20', classname="full"),
        FieldPanel('Ad_date20', classname="full"),
        FieldPanel('Ad_info21', classname="full"),
        FieldPanel('Ad_date21', classname="full"),
        FieldPanel('Ad_info22', classname="full"),
        FieldPanel('Ad_date22', classname="full"),
        FieldPanel('Ad_info23', classname="full"),
        FieldPanel('Ad_date23', classname="full"),
        FieldPanel('Ad_info24', classname="full"),
        FieldPanel('Ad_date24', classname="full"),
        FieldPanel('Ad_info25', classname="full"),
        FieldPanel('Ad_date25', classname="full"),
        FieldPanel('Ad_info26', classname="full"),
        FieldPanel('Ad_date26', classname="full"),
        FieldPanel('Ad_info27', classname="full"),
        FieldPanel('Ad_date27', classname="full"),
        FieldPanel('Ad_info28', classname="full"),
        FieldPanel('Ad_date28', classname="full"),
        FieldPanel('Ad_info29', classname="full"),
        FieldPanel('Ad_date29', classname="full"),
        FieldPanel('Ad_info30', classname="full"),
        FieldPanel('Ad_date30', classname="full"),
        FieldPanel('Ad_info31', classname="full"),
        FieldPanel('Ad_date31', classname="full"),
        FieldPanel('Ad_info32', classname="full"),
        FieldPanel('Ad_date32', classname="full"),
        FieldPanel('Ad_info33', classname="full"),
        FieldPanel('Ad_date33', classname="full"),
        FieldPanel('Ad_info34', classname="full"),
        FieldPanel('Ad_date34', classname="full"),
        FieldPanel('Ad_info35', classname="full"),
        FieldPanel('Ad_date35', classname="full"),
        FieldPanel('Ad_info36', classname="full"),
        FieldPanel('Ad_date36', classname="full"),
        FieldPanel('Ad_info37', classname="full"),
        FieldPanel('Ad_date37', classname="full"),
        FieldPanel('Ad_info38', classname="full"),
        FieldPanel('Ad_date38', classname="full"),
        FieldPanel('Ad_info39', classname="full"),
        FieldPanel('Ad_date39', classname="full"),
        FieldPanel('Ad_info40', classname="full"),
        FieldPanel('Ad_date40', classname="full"),
        FieldPanel('Ad_info41', classname="full"),
        FieldPanel('Ad_date41', classname="full"),
        FieldPanel('Ad_info42', classname="full"),
        FieldPanel('Ad_date42', classname="full"),
        FieldPanel('Ad_info43', classname="full"),
        FieldPanel('Ad_date43', classname="full"),
        FieldPanel('Ad_info44', classname="full"),
        FieldPanel('Ad_date44', classname="full"),
        FieldPanel('Ad_info45', classname="full"),
        FieldPanel('Ad_date45', classname="full"),
        FieldPanel('Ad_info46', classname="full"),
        FieldPanel('Ad_date46', classname="full"),
        FieldPanel('Ad_info47', classname="full"),
        FieldPanel('Ad_date47', classname="full"),
        FieldPanel('Ad_info48', classname="full"),
        FieldPanel('Ad_date48', classname="full"),
        FieldPanel('Ad_info49', classname="full"),
        FieldPanel('Ad_date49', classname="full"),
        FieldPanel('Ad_info50', classname="full"),
        FieldPanel('Ad_date50', classname="full"),
        FieldPanel('Ad_info51', classname="full"),
        FieldPanel('Ad_date51', classname="full"),
        FieldPanel('Ad_info52', classname="full"),
        FieldPanel('Ad_date52', classname="full"),
        FieldPanel('Ad_info53', classname="full"),
        FieldPanel('Ad_date53', classname="full"),
        FieldPanel('Ad_info54', classname="full"),
        FieldPanel('Ad_date54', classname="full"),
        FieldPanel('Ad_info55', classname="full"),
        FieldPanel('Ad_date55', classname="full"),
        FieldPanel('Ad_info56', classname="full"),
        FieldPanel('Ad_date56', classname="full"),
        FieldPanel('Ad_info57', classname="full"),
        FieldPanel('Ad_date57', classname="full"),
        FieldPanel('Ad_info58', classname="full"),
        FieldPanel('Ad_date58', classname="full"),
        FieldPanel('Ad_info59', classname="full"),
        FieldPanel('Ad_date59', classname="full"),
        FieldPanel('Ad_info60', classname="full"),
        FieldPanel('Ad_date60', classname="full"),
        FieldPanel('consulta', classname="full"),
        InlinePanel('galleria_2', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]  


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # If you need to show results only on landing page,
        # you may need check request.method

        results = dict()
        # Get information about form fields
        data_fields = [
            (field.clean_name, field.label)
            for field in self.get_form_fields()
        ]

        # Get all submissions for current page
        submissions = self.get_submission_class().objects.filter(page=self)
        for submission in submissions:
            data = submission.get_data()

            # Count results for each question
            for name, label in data_fields:
                answer = data.get(name)
                if answer is None:
                    # Something wrong with data.
                    # Probably you have changed questions
                    # and now we are receiving answers for old questions.
                    # Just skip them.
                    continue

                if type(answer) is list:
                    # Answer is a list if the field type is 'Checkboxes'
                    answer = u', '.join(answer)

                question_stats = results.get(label, {})
                question_stats[answer] = question_stats.get(answer, 0) + 1
                results[label] = question_stats

        context.update({
            'results': results,
        })
        return context   
    

class GaleriadeImagenes2(Orderable):
    page = ParentalKey(publicidad, on_delete=models.CASCADE, related_name='galleria_2')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 3')
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 4')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 5')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 6')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 7')
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 8')
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 9')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 10')
    image_11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 11')
    image_12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 12 ')
    image_13 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 13')
    image_14 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 14')
    image_15 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 15')
    image_16 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 16')
    image_17 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 17')
    image_18 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 18')
    image_19 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 19')
    image_20 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 20')
    image_21 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 21')
    image_22 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 22')
    image_23 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 23')
    image_24 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 24')
    image_25 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 25')
    image_26 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 26')
    image_27 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 27')
    image_28 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 28')
    image_29 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 29')
    image_30 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 30')
    image_31 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 31')
    image_32 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 32')
    image_33 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 33')
    image_34 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 34')
    image_35 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 35')
    image_36 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 36')
    image_37 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 37')
    image_38 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 38')
    image_39 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 39')
    image_40 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 40')
    image_41 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 41')
    image_42 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 42 ')
    image_43 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 43')
    image_44 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 44')
    image_45 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 45')
    image_46 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 46')
    image_47 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 47')
    image_48 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 48')
    image_49 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 49')
    image_50 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 50')
    image_51 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 51')
    image_52 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 52')
    image_53 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 53')
    image_54 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 54')
    image_55 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 55')
    image_56 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 56')
    image_57 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 57')
    image_58 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 58')
    image_59 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 59')
    image_60 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 60')

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
     

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image_9'),
        ImageChooserPanel('image_10'),
        ImageChooserPanel('image_11'),
        ImageChooserPanel('image_12'),
        ImageChooserPanel('image_13'),
        ImageChooserPanel('image_14'),
        ImageChooserPanel('image_15'),
        ImageChooserPanel('image_16'),
        ImageChooserPanel('image_17'),
        ImageChooserPanel('image_18'),
        ImageChooserPanel('image_19'),
        ImageChooserPanel('image_20'),
        ImageChooserPanel('image_21'),
        ImageChooserPanel('image_22'),
        ImageChooserPanel('image_23'),
        ImageChooserPanel('image_24'),
        ImageChooserPanel('image_25'),
        ImageChooserPanel('image_26'),
        ImageChooserPanel('image_27'),
        ImageChooserPanel('image_28'),
        ImageChooserPanel('image_29'),
        ImageChooserPanel('image_30'),
        ImageChooserPanel('image_31'),
        ImageChooserPanel('image_32'),
        ImageChooserPanel('image_33'),
        ImageChooserPanel('image_34'),
        ImageChooserPanel('image_35'),
        ImageChooserPanel('image_36'),
        ImageChooserPanel('image_37'),
        ImageChooserPanel('image_38'),
        ImageChooserPanel('image_39'),
        ImageChooserPanel('image_40'),
        ImageChooserPanel('image_41'),
        ImageChooserPanel('image_42'),
        ImageChooserPanel('image_43'),
        ImageChooserPanel('image_44'),
        ImageChooserPanel('image_45'),
        ImageChooserPanel('image_46'),
        ImageChooserPanel('image_47'),
        ImageChooserPanel('image_48'),
        ImageChooserPanel('image_49'),
        ImageChooserPanel('image_50'),
        ImageChooserPanel('image_51'),
        ImageChooserPanel('image_52'),
        ImageChooserPanel('image_53'),
        ImageChooserPanel('image_54'),
        ImageChooserPanel('image_55'),
        ImageChooserPanel('image_56'),
        ImageChooserPanel('image_57'),
        ImageChooserPanel('image_58'),
        ImageChooserPanel('image_59'),
        ImageChooserPanel('image_60'),
        
    ]


class NewsDetailPage(Page):
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Titulo de la publicacion ")
    news_image = models.ForeignKey("wagtailimages.Image", blank=False,null=True,related_name="+", on_delete = models.SET_NULL )
    Fecha = models.DateTimeField(null=True)
    author = models.CharField(max_length=100,blank=True,null=True,help_text="Nombre del Autor ")
    content  = StreamField(
    [
    ("title_and_text", blocks.TitleAndTextBlock()),
    ("full_richtext", blocks.RichtextBlock()),
    ("simple_richtext", blocks.SimpleRichtextBlock()),
    ("cards", blocks.CardBlock()),
    ],null = True, blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("author"),
        FieldPanel("Fecha"),
        ImageChooserPanel("news_image"),
        InlinePanel('galleria_News', label="Imagenes Shooting Now"),
        StreamFieldPanel("content")
        ]

class GaleriadeImagenes_News(Orderable):
    page = ParentalKey(NewsDetailPage, on_delete=models.CASCADE, related_name='galleria_News')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto 3')
    
    
    # Imagenes Thumb Portfolio
    
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto 4')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto 5')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto 6')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto 7')

    # Fotos TearSheate
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto 8')
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto 9')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto 10')

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image_9'),
        ImageChooserPanel('image_10')
    ]
    
   




@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True,null=True,help_text="")
    twitter = models.URLField(blank=True,null=True,help_text="")
    instagram = models.URLField(blank=True,null=True,help_text="")
    youtube = models.URLField(blank=True,null=True,help_text="")

    panels = [
        MultiFieldPanel(
            [
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("instagram"),
            FieldPanel("youtube"),           
            ]
        ,heading= "Social Media Settings")
    ]



class consultas_Prod(AbstractFormField):
    page = ParentalKey('Productos', on_delete=models.CASCADE, related_name='form_fields')

class Productos(AbstractEmailForm):
    # Empieza Galeria de Imagenes
    template = "webapp_0/Productos.html"
    Ad_info = models.CharField(max_length= 500, null=True, blank=True,verbose_name='Advertising info')
    Ad_link = RichTextField(blank=True,verbose_name='Enlace para volver al inicio')
    Ad_info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-1 info')
    Ad_date1 = models.DateField("Fecha de Advertising-1",null=True, blank=True)
    Ad_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-2 info')
    Ad_date2 = models.DateField("Fecha de Advertising-2",null=True, blank=True)
    Ad_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-3 info')
    Ad_date3 = models.DateField("Fecha de Advertising-3",null=True, blank=True)
    Ad_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-4 info')
    Ad_date4 = models.DateField("Fecha de Advertising-4",null=True, blank=True)
    Ad_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-5 info')
    Ad_date5 = models.DateField("Fecha de Advertising-5",null=True, blank=True)
    Ad_info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-6 info')
    Ad_date6 = models.DateField("Fecha de Advertising-6",null=True, blank=True)
    Ad_info7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-7 info')
    Ad_date7 = models.DateField("Fecha de Advertising-7",null=True, blank=True)
    Ad_info8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-8 info')
    Ad_date8 = models.DateField("Fecha de Advertising-8",null=True, blank=True)
    Ad_info9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-9 info')
    Ad_date9 = models.DateField("Fecha de Advertising-9",null=True, blank=True)
    Ad_info10 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-10 info')
    Ad_date10 = models.DateField("Fecha de Advertising-10",null=True, blank=True)
    Ad_info11 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-11 info')
    Ad_date11 = models.DateField("Fecha de Advertising-11",null=True, blank=True)
    Ad_info12 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-12 info')
    Ad_date12 = models.DateField("Fecha de Advertising-12",null=True, blank=True)
    Ad_info13 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-13 info')
    Ad_date13 = models.DateField("Fecha de Advertising-13",null=True, blank=True)
    Ad_info14 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-14 info')
    Ad_date14 = models.DateField("Fecha de Advertising-14",null=True, blank=True)
    Ad_info15 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-15 info')
    Ad_date15 = models.DateField("Fecha de Advertising-15",null=True, blank=True)
    Ad_info16 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-16 info')
    Ad_date16 = models.DateField("Fecha de Advertising-16",null=True, blank=True)
    Ad_info17 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-17 info')
    Ad_date17 = models.DateField("Fecha de Advertising-17",null=True, blank=True)
    Ad_info18 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-18 info')
    Ad_date18 = models.DateField("Fecha de Advertising-18",null=True, blank=True)
    Ad_info19 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-19 info')
    Ad_date19 = models.DateField("Fecha de Advertising-19",null=True, blank=True)
    Ad_info20 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-20 info')
    Ad_date20 = models.DateField("Fecha de Advertising-20",null=True, blank=True)
    Ad_info21 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-21 info')
    Ad_date21 = models.DateField("Fecha de Advertising-21",null=True, blank=True)
    Ad_info22 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-22 info')
    Ad_date22 = models.DateField("Fecha de Advertising-22",null=True, blank=True)
    Ad_info23 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-23 info')
    Ad_date23 = models.DateField("Fecha de Advertising-23",null=True, blank=True)
    Ad_info24 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-24 info')
    Ad_date24 = models.DateField("Fecha de Advertising-24",null=True, blank=True)
    Ad_info25 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-25 info')
    Ad_date25 = models.DateField("Fecha de Advertising-25",null=True, blank=True)
    Ad_info26 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-26 info')
    Ad_date26 = models.DateField("Fecha de Advertising-26",null=True, blank=True)
    Ad_info27 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-27 info')
    Ad_date27 = models.DateField("Fecha de Advertising-27",null=True, blank=True)
    Ad_info28 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-28 info')
    Ad_date28 = models.DateField("Fecha de Advertising-28",null=True, blank=True)
    Ad_info29 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-29 info')
    Ad_date29 = models.DateField("Fecha de Advertising-29",null=True, blank=True)
    Ad_info30 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-30 info')
    Ad_date30 = models.DateField("Fecha de Advertising-30",null=True, blank=True)
    Ad_info31 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-31 info')
    Ad_date31 = models.DateField("Fecha de Advertising-31",null=True, blank=True)
    Ad_info32 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-32 info')
    Ad_date32 = models.DateField("Fecha de Advertising-32",null=True, blank=True)
    Ad_info33 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-33 info')
    Ad_date33 = models.DateField("Fecha de Advertising-33",null=True, blank=True)
    Ad_info34 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-34 info')
    Ad_date34 = models.DateField("Fecha de Advertising-34",null=True, blank=True)
    Ad_info35 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-35 info')
    Ad_date35 = models.DateField("Fecha de Advertising-35",null=True, blank=True)
    Ad_info36 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-36 info')
    Ad_date36 = models.DateField("Fecha de Advertising-36",null=True, blank=True)
    Ad_info37 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-37 info')
    Ad_date37 = models.DateField("Fecha de Advertising-37",null=True, blank=True)
    Ad_info38 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-38 info')
    Ad_date38 = models.DateField("Fecha de Advertising-38",null=True, blank=True)
    Ad_info39 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-39 info')
    Ad_date39 = models.DateField("Fecha de Advertising-39",null=True, blank=True)
    Ad_info40 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-40 info')
    Ad_date40 = models.DateField("Fecha de Advertising-40",null=True, blank=True)
    Ad_info41 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-41 info')
    Ad_date41 = models.DateField("Fecha de Advertising-41",null=True, blank=True)
    Ad_info42 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-42 info')
    Ad_date42 = models.DateField("Fecha de Advertising-42",null=True, blank=True)
    Ad_info43 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-43 info')
    Ad_date43 = models.DateField("Fecha de Advertising-43",null=True, blank=True)
    Ad_info44 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-44 info')
    Ad_date44 = models.DateField("Fecha de Advertising-44",null=True, blank=True)
    Ad_info45 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-45 info')
    Ad_date45 = models.DateField("Fecha de Advertising-45",null=True, blank=True)
    Ad_info46 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-46 info')
    Ad_date46 = models.DateField("Fecha de Advertising-46",null=True, blank=True)
    Ad_info47 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-47 info')
    Ad_date47 = models.DateField("Fecha de Advertising-47",null=True, blank=True)
    Ad_info48 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-48 info')
    Ad_date48 = models.DateField("Fecha de Advertising-48",null=True, blank=True)
    Ad_info49 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-49 info')
    Ad_date49 = models.DateField("Fecha de Advertising-49",null=True, blank=True)
    Ad_info50 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-50 info')
    Ad_date50 = models.DateField("Fecha de Advertising-50",null=True, blank=True)
    Ad_info51 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-51 info')
    Ad_date51 = models.DateField("Fecha de Advertising-51",null=True, blank=True)
    Ad_info52 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-52 info')
    Ad_date52 = models.DateField("Fecha de Advertising-52",null=True, blank=True)
    Ad_info53 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-53 info')
    Ad_date53 = models.DateField("Fecha de Advertising-53",null=True, blank=True)
    Ad_info54 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-54 info')
    Ad_date54 = models.DateField("Fecha de Advertising-54",null=True, blank=True)
    Ad_info55 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-55 info')
    Ad_date55 = models.DateField("Fecha de Advertising-55",null=True, blank=True)
    Ad_info56 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-56 info')
    Ad_date56 = models.DateField("Fecha de Advertising-56",null=True, blank=True)
    Ad_info57 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-57 info')
    Ad_date57 = models.DateField("Fecha de Advertising-57",null=True, blank=True)
    Ad_info58 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-58 info')
    Ad_date58 = models.DateField("Fecha de Advertising-58",null=True, blank=True)
    Ad_info59 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-59 info')
    Ad_date59 = models.DateField("Fecha de Advertising-59",null=True, blank=True)
    Ad_info60 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-60 info')
    Ad_date60 = models.DateField("Fecha de Advertising-60",null=True, blank=True)
    # Comentario de Galeria
    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('Ad_info', classname="full"),
        FieldPanel('Ad_link', classname="full"),
        FieldPanel('Ad_info1', classname="full"),
        FieldPanel('Ad_date1', classname="full"),
        FieldPanel('Ad_info2', classname="full"),
        FieldPanel('Ad_date2', classname="full"),
        FieldPanel('Ad_info3', classname="full"),
        FieldPanel('Ad_date3', classname="full"),
        FieldPanel('Ad_info4', classname="full"),
        FieldPanel('Ad_date4', classname="full"),
        FieldPanel('Ad_info5', classname="full"),
        FieldPanel('Ad_date5', classname="full"),
        FieldPanel('Ad_info6', classname="full"),
        FieldPanel('Ad_date6', classname="full"),
        FieldPanel('Ad_info7', classname="full"),
        FieldPanel('Ad_date7', classname="full"),
        FieldPanel('Ad_info8', classname="full"),
        FieldPanel('Ad_date8', classname="full"),
        FieldPanel('Ad_info9', classname="full"),
        FieldPanel('Ad_date9', classname="full"),
        FieldPanel('Ad_info10', classname="full"),
        FieldPanel('Ad_date10', classname="full"),
        FieldPanel('Ad_info11', classname="full"),
        FieldPanel('Ad_date11', classname="full"),
        FieldPanel('Ad_info12', classname="full"),
        FieldPanel('Ad_date12', classname="full"),
        FieldPanel('Ad_info13', classname="full"),
        FieldPanel('Ad_date13', classname="full"),
        FieldPanel('Ad_info14', classname="full"),
        FieldPanel('Ad_date14', classname="full"),
        FieldPanel('Ad_info15', classname="full"),
        FieldPanel('Ad_date15', classname="full"),
        FieldPanel('Ad_info16', classname="full"),
        FieldPanel('Ad_date16', classname="full"),
        FieldPanel('Ad_info17', classname="full"),
        FieldPanel('Ad_date17', classname="full"),
        FieldPanel('Ad_info18', classname="full"),
        FieldPanel('Ad_date18', classname="full"),
        FieldPanel('Ad_info19', classname="full"),
        FieldPanel('Ad_date19', classname="full"),
        FieldPanel('Ad_info20', classname="full"),
        FieldPanel('Ad_date20', classname="full"),
        FieldPanel('Ad_info21', classname="full"),
        FieldPanel('Ad_date21', classname="full"),
        FieldPanel('Ad_info22', classname="full"),
        FieldPanel('Ad_date22', classname="full"),
        FieldPanel('Ad_info23', classname="full"),
        FieldPanel('Ad_date23', classname="full"),
        FieldPanel('Ad_info24', classname="full"),
        FieldPanel('Ad_date24', classname="full"),
        FieldPanel('Ad_info25', classname="full"),
        FieldPanel('Ad_date25', classname="full"),
        FieldPanel('Ad_info26', classname="full"),
        FieldPanel('Ad_date26', classname="full"),
        FieldPanel('Ad_info27', classname="full"),
        FieldPanel('Ad_date27', classname="full"),
        FieldPanel('Ad_info28', classname="full"),
        FieldPanel('Ad_date28', classname="full"),
        FieldPanel('Ad_info29', classname="full"),
        FieldPanel('Ad_date29', classname="full"),
        FieldPanel('Ad_info30', classname="full"),
        FieldPanel('Ad_date30', classname="full"),
        FieldPanel('Ad_info31', classname="full"),
        FieldPanel('Ad_date31', classname="full"),
        FieldPanel('Ad_info32', classname="full"),
        FieldPanel('Ad_date32', classname="full"),
        FieldPanel('Ad_info33', classname="full"),
        FieldPanel('Ad_date33', classname="full"),
        FieldPanel('Ad_info34', classname="full"),
        FieldPanel('Ad_date34', classname="full"),
        FieldPanel('Ad_info35', classname="full"),
        FieldPanel('Ad_date35', classname="full"),
        FieldPanel('Ad_info36', classname="full"),
        FieldPanel('Ad_date36', classname="full"),
        FieldPanel('Ad_info37', classname="full"),
        FieldPanel('Ad_date37', classname="full"),
        FieldPanel('Ad_info38', classname="full"),
        FieldPanel('Ad_date38', classname="full"),
        FieldPanel('Ad_info39', classname="full"),
        FieldPanel('Ad_date39', classname="full"),
        FieldPanel('Ad_info40', classname="full"),
        FieldPanel('Ad_date40', classname="full"),
        FieldPanel('Ad_info41', classname="full"),
        FieldPanel('Ad_date41', classname="full"),
        FieldPanel('Ad_info42', classname="full"),
        FieldPanel('Ad_date42', classname="full"),
        FieldPanel('Ad_info43', classname="full"),
        FieldPanel('Ad_date43', classname="full"),
        FieldPanel('Ad_info44', classname="full"),
        FieldPanel('Ad_date44', classname="full"),
        FieldPanel('Ad_info45', classname="full"),
        FieldPanel('Ad_date45', classname="full"),
        FieldPanel('Ad_info46', classname="full"),
        FieldPanel('Ad_date46', classname="full"),
        FieldPanel('Ad_info47', classname="full"),
        FieldPanel('Ad_date47', classname="full"),
        FieldPanel('Ad_info48', classname="full"),
        FieldPanel('Ad_date48', classname="full"),
        FieldPanel('Ad_info49', classname="full"),
        FieldPanel('Ad_date49', classname="full"),
        FieldPanel('Ad_info50', classname="full"),
        FieldPanel('Ad_date50', classname="full"),
        FieldPanel('Ad_info51', classname="full"),
        FieldPanel('Ad_date51', classname="full"),
        FieldPanel('Ad_info52', classname="full"),
        FieldPanel('Ad_date52', classname="full"),
        FieldPanel('Ad_info53', classname="full"),
        FieldPanel('Ad_date53', classname="full"),
        FieldPanel('Ad_info54', classname="full"),
        FieldPanel('Ad_date54', classname="full"),
        FieldPanel('Ad_info55', classname="full"),
        FieldPanel('Ad_date55', classname="full"),
        FieldPanel('Ad_info56', classname="full"),
        FieldPanel('Ad_date56', classname="full"),
        FieldPanel('Ad_info57', classname="full"),
        FieldPanel('Ad_date57', classname="full"),
        FieldPanel('Ad_info58', classname="full"),
        FieldPanel('Ad_date58', classname="full"),
        FieldPanel('Ad_info59', classname="full"),
        FieldPanel('Ad_date59', classname="full"),
        FieldPanel('Ad_info60', classname="full"),
        FieldPanel('Ad_date60', classname="full"),
        FieldPanel('consulta', classname="full"),
        InlinePanel('galleria_3', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_form_fields(self):
        return self.form_fields.all()

    def get_data_fields(self):
        data_fields = [
            ('name', 'Name'),
        ]
        data_fields += super().get_data_fields()

        return data_fields

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # If you need to show results only on landing page,
        # you may need check request.method

        results = dict()
        # Get information about form fields
        data_fields = [
            (field.clean_name, field.label)
            for field in self.get_form_fields()
        ]

        # Get all submissions for current page
        submissions = self.get_submission_class().objects.filter(page=self)
        for submission in submissions:
            data = submission.get_data()

            # Count results for each question
            for name, label in data_fields:
                answer = data.get(name)
                if answer is None:
                    # Something wrong with data.
                    # Probably you have changed questions
                    # and now we are receiving answers for old questions.
                    # Just skip them.
                    continue

                if type(answer) is list:
                    # Answer is a list if the field type is 'Checkboxes'
                    answer = u', '.join(answer)

                question_stats = results.get(label, {})
                question_stats[answer] = question_stats.get(answer, 0) + 1
                results[label] = question_stats

        context.update({
            'results': results,
        })
        return context


class GaleriadeImagenes3(Orderable):
    page = ParentalKey(Productos, on_delete=models.CASCADE, related_name='galleria_3')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 3')
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 4')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 5')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 6')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 7')
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 8')
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 9')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 10')
    image_11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 11')
    image_12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 12 ')
    image_13 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 13')
    image_14 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 14')
    image_15 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 15')
    image_16 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 16')
    image_17 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 17')
    image_18 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 18')
    image_19 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 19')
    image_20 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 20')
    image_21 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 21')
    image_22 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 22')
    image_23 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 23')
    image_24 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 24')
    image_25 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 25')
    image_26 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 26')
    image_27 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 27')
    image_28 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 28')
    image_29 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 29')
    image_30 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 30')
    image_31 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 31')
    image_32 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 32')
    image_33 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 33')
    image_34 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 34')
    image_35 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 35')
    image_36 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 36')
    image_37 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 37')
    image_38 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 38')
    image_39 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 39')
    image_40 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 40')
    image_41 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 41')
    image_42 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 42 ')
    image_43 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 43')
    image_44 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 44')
    image_45 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 45')
    image_46 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 46')
    image_47 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 47')
    image_48 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 48')
    image_49 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 49')
    image_50 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 50')
    image_51 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 51')
    image_52 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 52')
    image_53 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 53')
    image_54 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 54')
    image_55 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 55')
    image_56 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 56')
    image_57 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 57')
    image_58 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 58')
    image_59 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 59')
    image_60 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 60')
     

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image_9'),
        ImageChooserPanel('image_10'),
        ImageChooserPanel('image_11'),
        ImageChooserPanel('image_12'),
        ImageChooserPanel('image_13'),
        ImageChooserPanel('image_14'),
        ImageChooserPanel('image_15'),
        ImageChooserPanel('image_16'),
        ImageChooserPanel('image_17'),
        ImageChooserPanel('image_18'),
        ImageChooserPanel('image_19'),
        ImageChooserPanel('image_20'),
        ImageChooserPanel('image_21'),
        ImageChooserPanel('image_22'),
        ImageChooserPanel('image_23'),
        ImageChooserPanel('image_24'),
        ImageChooserPanel('image_25'),
        ImageChooserPanel('image_26'),
        ImageChooserPanel('image_27'),
        ImageChooserPanel('image_28'),
        ImageChooserPanel('image_29'),
        ImageChooserPanel('image_30'),
        ImageChooserPanel('image_31'),
        ImageChooserPanel('image_32'),
        ImageChooserPanel('image_33'),
        ImageChooserPanel('image_34'),
        ImageChooserPanel('image_35'),
        ImageChooserPanel('image_36'),
        ImageChooserPanel('image_37'),
        ImageChooserPanel('image_38'),
        ImageChooserPanel('image_39'),
        ImageChooserPanel('image_40'),
        ImageChooserPanel('image_41'),
        ImageChooserPanel('image_42'),
        ImageChooserPanel('image_43'),
        ImageChooserPanel('image_44'),
        ImageChooserPanel('image_45'),
        ImageChooserPanel('image_46'),
        ImageChooserPanel('image_47'),
        ImageChooserPanel('image_48'),
        ImageChooserPanel('image_49'),
        ImageChooserPanel('image_50'),
        ImageChooserPanel('image_51'),
        ImageChooserPanel('image_52'),
        ImageChooserPanel('image_53'),
        ImageChooserPanel('image_54'),
        ImageChooserPanel('image_55'),
        ImageChooserPanel('image_56'),
        ImageChooserPanel('image_57'),
        ImageChooserPanel('image_58'),
        ImageChooserPanel('image_59'),
        ImageChooserPanel('image_60'),
        
    ]

class consultas_Land(AbstractFormField):
    page = ParentalKey('Landscape', on_delete=models.CASCADE, related_name='form_fields')

class Landscape(AbstractEmailForm):
    template = "webapp_0/Landscape.html"
    # Empieza Galeria de Imagenes
    Ad_info = models.CharField(max_length= 500, null=True, blank=True,verbose_name='Advertising info')
    Ad_link = RichTextField(blank=True,verbose_name='Enlace para volver al inicio')
    Ad_info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-1 info')
    Ad_date1 = models.DateField("Fecha de Advertising-1",null=True, blank=True)
    Ad_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-2 info')
    Ad_date2 = models.DateField("Fecha de Advertising-2",null=True, blank=True)
    Ad_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-3 info')
    Ad_date3 = models.DateField("Fecha de Advertising-3",null=True, blank=True)
    Ad_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-4 info')
    Ad_date4 = models.DateField("Fecha de Advertising-4",null=True, blank=True)
    Ad_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-5 info')
    Ad_date5 = models.DateField("Fecha de Advertising-5",null=True, blank=True)
    Ad_info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-6 info')
    Ad_date6 = models.DateField("Fecha de Advertising-6",null=True, blank=True)
    Ad_info7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-7 info')
    Ad_date7 = models.DateField("Fecha de Advertising-7",null=True, blank=True)
    Ad_info8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-8 info')
    Ad_date8 = models.DateField("Fecha de Advertising-8",null=True, blank=True)
    Ad_info9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-9 info')
    Ad_date9 = models.DateField("Fecha de Advertising-9",null=True, blank=True)
    Ad_info10 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-10 info')
    Ad_date10 = models.DateField("Fecha de Advertising-10",null=True, blank=True)
    Ad_info11 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-11 info')
    Ad_date11 = models.DateField("Fecha de Advertising-11",null=True, blank=True)
    Ad_info12 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-12 info')
    Ad_date12 = models.DateField("Fecha de Advertising-12",null=True, blank=True)
    Ad_info13 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-13 info')
    Ad_date13 = models.DateField("Fecha de Advertising-13",null=True, blank=True)
    Ad_info14 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-14 info')
    Ad_date14 = models.DateField("Fecha de Advertising-14",null=True, blank=True)
    Ad_info15 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-15 info')
    Ad_date15 = models.DateField("Fecha de Advertising-15",null=True, blank=True)
    Ad_info16 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-16 info')
    Ad_date16 = models.DateField("Fecha de Advertising-16",null=True, blank=True)
    Ad_info17 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-17 info')
    Ad_date17 = models.DateField("Fecha de Advertising-17",null=True, blank=True)
    Ad_info18 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-18 info')
    Ad_date18 = models.DateField("Fecha de Advertising-18",null=True, blank=True)
    Ad_info19 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-19 info')
    Ad_date19 = models.DateField("Fecha de Advertising-19",null=True, blank=True)
    Ad_info20 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-20 info')
    Ad_date20 = models.DateField("Fecha de Advertising-20",null=True, blank=True)
    Ad_info21 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-21 info')
    Ad_date21 = models.DateField("Fecha de Advertising-21",null=True, blank=True)
    Ad_info22 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-22 info')
    Ad_date22 = models.DateField("Fecha de Advertising-22",null=True, blank=True)
    Ad_info23 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-23 info')
    Ad_date23 = models.DateField("Fecha de Advertising-23",null=True, blank=True)
    Ad_info24 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-24 info')
    Ad_date24 = models.DateField("Fecha de Advertising-24",null=True, blank=True)
    Ad_info25 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-25 info')
    Ad_date25 = models.DateField("Fecha de Advertising-25",null=True, blank=True)
    Ad_info26 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-26 info')
    Ad_date26 = models.DateField("Fecha de Advertising-26",null=True, blank=True)
    Ad_info27 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-27 info')
    Ad_date27 = models.DateField("Fecha de Advertising-27",null=True, blank=True)
    Ad_info28 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-28 info')
    Ad_date28 = models.DateField("Fecha de Advertising-28",null=True, blank=True)
    Ad_info29 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-29 info')
    Ad_date29 = models.DateField("Fecha de Advertising-29",null=True, blank=True)
    Ad_info30 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-30 info')
    Ad_date30 = models.DateField("Fecha de Advertising-30",null=True, blank=True)
    Ad_info31 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-31 info')
    Ad_date31 = models.DateField("Fecha de Advertising-31",null=True, blank=True)
    Ad_info32 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-32 info')
    Ad_date32 = models.DateField("Fecha de Advertising-32",null=True, blank=True)
    Ad_info33 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-33 info')
    Ad_date33 = models.DateField("Fecha de Advertising-33",null=True, blank=True)
    Ad_info34 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-34 info')
    Ad_date34 = models.DateField("Fecha de Advertising-34",null=True, blank=True)
    Ad_info35 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-35 info')
    Ad_date35 = models.DateField("Fecha de Advertising-35",null=True, blank=True)
    Ad_info36 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-36 info')
    Ad_date36 = models.DateField("Fecha de Advertising-36",null=True, blank=True)
    Ad_info37 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-37 info')
    Ad_date37 = models.DateField("Fecha de Advertising-37",null=True, blank=True)
    Ad_info38 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-38 info')
    Ad_date38 = models.DateField("Fecha de Advertising-38",null=True, blank=True)
    Ad_info39 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-39 info')
    Ad_date39 = models.DateField("Fecha de Advertising-39",null=True, blank=True)
    Ad_info40 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-40 info')
    Ad_date40 = models.DateField("Fecha de Advertising-40",null=True, blank=True)
    Ad_info41 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-41 info')
    Ad_date41 = models.DateField("Fecha de Advertising-41",null=True, blank=True)
    Ad_info42 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-42 info')
    Ad_date42 = models.DateField("Fecha de Advertising-42",null=True, blank=True)
    Ad_info43 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-43 info')
    Ad_date43 = models.DateField("Fecha de Advertising-43",null=True, blank=True)
    Ad_info44 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-44 info')
    Ad_date44 = models.DateField("Fecha de Advertising-44",null=True, blank=True)
    Ad_info45 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-45 info')
    Ad_date45 = models.DateField("Fecha de Advertising-45",null=True, blank=True)
    Ad_info46 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-46 info')
    Ad_date46 = models.DateField("Fecha de Advertising-46",null=True, blank=True)
    Ad_info47 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-47 info')
    Ad_date47 = models.DateField("Fecha de Advertising-47",null=True, blank=True)
    Ad_info48 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-48 info')
    Ad_date48 = models.DateField("Fecha de Advertising-48",null=True, blank=True)
    Ad_info49 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-49 info')
    Ad_date49 = models.DateField("Fecha de Advertising-49",null=True, blank=True)
    Ad_info50 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-50 info')
    Ad_date50 = models.DateField("Fecha de Advertising-50",null=True, blank=True)
    Ad_info51 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-51 info')
    Ad_date51 = models.DateField("Fecha de Advertising-51",null=True, blank=True)
    Ad_info52 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-52 info')
    Ad_date52 = models.DateField("Fecha de Advertising-52",null=True, blank=True)
    Ad_info53 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-53 info')
    Ad_date53 = models.DateField("Fecha de Advertising-53",null=True, blank=True)
    Ad_info54 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-54 info')
    Ad_date54 = models.DateField("Fecha de Advertising-54",null=True, blank=True)
    Ad_info55 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-55 info')
    Ad_date55 = models.DateField("Fecha de Advertising-55",null=True, blank=True)
    Ad_info56 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-56 info')
    Ad_date56 = models.DateField("Fecha de Advertising-56",null=True, blank=True)
    Ad_info57 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-57 info')
    Ad_date57 = models.DateField("Fecha de Advertising-57",null=True, blank=True)
    Ad_info58 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-58 info')
    Ad_date58 = models.DateField("Fecha de Advertising-58",null=True, blank=True)
    Ad_info59 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-59 info')
    Ad_date59 = models.DateField("Fecha de Advertising-59",null=True, blank=True)
    Ad_info60 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-60 info')
    Ad_date60 = models.DateField("Fecha de Advertising-60",null=True, blank=True)
    # Comentario de Galeria
    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('Ad_info', classname="full"),
        FieldPanel('Ad_link', classname="full"),
        FieldPanel('Ad_info1', classname="full"),
        FieldPanel('Ad_date1', classname="full"),
        FieldPanel('Ad_info2', classname="full"),
        FieldPanel('Ad_date2', classname="full"),
        FieldPanel('Ad_info3', classname="full"),
        FieldPanel('Ad_date3', classname="full"),
        FieldPanel('Ad_info4', classname="full"),
        FieldPanel('Ad_date4', classname="full"),
        FieldPanel('Ad_info5', classname="full"),
        FieldPanel('Ad_date5', classname="full"),
        FieldPanel('Ad_info6', classname="full"),
        FieldPanel('Ad_date6', classname="full"),
        FieldPanel('Ad_info7', classname="full"),
        FieldPanel('Ad_date7', classname="full"),
        FieldPanel('Ad_info8', classname="full"),
        FieldPanel('Ad_date8', classname="full"),
        FieldPanel('Ad_info9', classname="full"),
        FieldPanel('Ad_date9', classname="full"),
        FieldPanel('Ad_info10', classname="full"),
        FieldPanel('Ad_date10', classname="full"),
        FieldPanel('Ad_info11', classname="full"),
        FieldPanel('Ad_date11', classname="full"),
        FieldPanel('Ad_info12', classname="full"),
        FieldPanel('Ad_date12', classname="full"),
        FieldPanel('Ad_info13', classname="full"),
        FieldPanel('Ad_date13', classname="full"),
        FieldPanel('Ad_info14', classname="full"),
        FieldPanel('Ad_date14', classname="full"),
        FieldPanel('Ad_info15', classname="full"),
        FieldPanel('Ad_date15', classname="full"),
        FieldPanel('Ad_info16', classname="full"),
        FieldPanel('Ad_date16', classname="full"),
        FieldPanel('Ad_info17', classname="full"),
        FieldPanel('Ad_date17', classname="full"),
        FieldPanel('Ad_info18', classname="full"),
        FieldPanel('Ad_date18', classname="full"),
        FieldPanel('Ad_info19', classname="full"),
        FieldPanel('Ad_date19', classname="full"),
        FieldPanel('Ad_info20', classname="full"),
        FieldPanel('Ad_date20', classname="full"),
        FieldPanel('Ad_info21', classname="full"),
        FieldPanel('Ad_date21', classname="full"),
        FieldPanel('Ad_info22', classname="full"),
        FieldPanel('Ad_date22', classname="full"),
        FieldPanel('Ad_info23', classname="full"),
        FieldPanel('Ad_date23', classname="full"),
        FieldPanel('Ad_info24', classname="full"),
        FieldPanel('Ad_date24', classname="full"),
        FieldPanel('Ad_info25', classname="full"),
        FieldPanel('Ad_date25', classname="full"),
        FieldPanel('Ad_info26', classname="full"),
        FieldPanel('Ad_date26', classname="full"),
        FieldPanel('Ad_info27', classname="full"),
        FieldPanel('Ad_date27', classname="full"),
        FieldPanel('Ad_info28', classname="full"),
        FieldPanel('Ad_date28', classname="full"),
        FieldPanel('Ad_info29', classname="full"),
        FieldPanel('Ad_date29', classname="full"),
        FieldPanel('Ad_info30', classname="full"),
        FieldPanel('Ad_date30', classname="full"),
        FieldPanel('Ad_info31', classname="full"),
        FieldPanel('Ad_date31', classname="full"),
        FieldPanel('Ad_info32', classname="full"),
        FieldPanel('Ad_date32', classname="full"),
        FieldPanel('Ad_info33', classname="full"),
        FieldPanel('Ad_date33', classname="full"),
        FieldPanel('Ad_info34', classname="full"),
        FieldPanel('Ad_date34', classname="full"),
        FieldPanel('Ad_info35', classname="full"),
        FieldPanel('Ad_date35', classname="full"),
        FieldPanel('Ad_info36', classname="full"),
        FieldPanel('Ad_date36', classname="full"),
        FieldPanel('Ad_info37', classname="full"),
        FieldPanel('Ad_date37', classname="full"),
        FieldPanel('Ad_info38', classname="full"),
        FieldPanel('Ad_date38', classname="full"),
        FieldPanel('Ad_info39', classname="full"),
        FieldPanel('Ad_date39', classname="full"),
        FieldPanel('Ad_info40', classname="full"),
        FieldPanel('Ad_date40', classname="full"),
        FieldPanel('Ad_info41', classname="full"),
        FieldPanel('Ad_date41', classname="full"),
        FieldPanel('Ad_info42', classname="full"),
        FieldPanel('Ad_date42', classname="full"),
        FieldPanel('Ad_info43', classname="full"),
        FieldPanel('Ad_date43', classname="full"),
        FieldPanel('Ad_info44', classname="full"),
        FieldPanel('Ad_date44', classname="full"),
        FieldPanel('Ad_info45', classname="full"),
        FieldPanel('Ad_date45', classname="full"),
        FieldPanel('Ad_info46', classname="full"),
        FieldPanel('Ad_date46', classname="full"),
        FieldPanel('Ad_info47', classname="full"),
        FieldPanel('Ad_date47', classname="full"),
        FieldPanel('Ad_info48', classname="full"),
        FieldPanel('Ad_date48', classname="full"),
        FieldPanel('Ad_info49', classname="full"),
        FieldPanel('Ad_date49', classname="full"),
        FieldPanel('Ad_info50', classname="full"),
        FieldPanel('Ad_date50', classname="full"),
        FieldPanel('Ad_info51', classname="full"),
        FieldPanel('Ad_date51', classname="full"),
        FieldPanel('Ad_info52', classname="full"),
        FieldPanel('Ad_date52', classname="full"),
        FieldPanel('Ad_info53', classname="full"),
        FieldPanel('Ad_date53', classname="full"),
        FieldPanel('Ad_info54', classname="full"),
        FieldPanel('Ad_date54', classname="full"),
        FieldPanel('Ad_info55', classname="full"),
        FieldPanel('Ad_date55', classname="full"),
        FieldPanel('Ad_info56', classname="full"),
        FieldPanel('Ad_date56', classname="full"),
        FieldPanel('Ad_info57', classname="full"),
        FieldPanel('Ad_date57', classname="full"),
        FieldPanel('Ad_info58', classname="full"),
        FieldPanel('Ad_date58', classname="full"),
        FieldPanel('Ad_info59', classname="full"),
        FieldPanel('Ad_date59', classname="full"),
        FieldPanel('Ad_info60', classname="full"),
        FieldPanel('Ad_date60', classname="full"),
        FieldPanel('consulta', classname="full"),
        InlinePanel('galleria_4', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # If you need to show results only on landing page,
        # you may need check request.method

        results = dict()
        # Get information about form fields
        data_fields = [
            (field.clean_name, field.label)
            for field in self.get_form_fields()
        ]

        # Get all submissions for current page
        submissions = self.get_submission_class().objects.filter(page=self)
        for submission in submissions:
            data = submission.get_data()

            # Count results for each question
            for name, label in data_fields:
                answer = data.get(name)
                if answer is None:
                    # Something wrong with data.
                    # Probably you have changed questions
                    # and now we are receiving answers for old questions.
                    # Just skip them.
                    continue

                if type(answer) is list:
                    # Answer is a list if the field type is 'Checkboxes'
                    answer = u', '.join(answer)

                question_stats = results.get(label, {})
                question_stats[answer] = question_stats.get(answer, 0) + 1
                results[label] = question_stats

        context.update({
            'results': results,
        })
        return context

class GaleriadeImagenes4(Orderable):
    page = ParentalKey(Landscape, on_delete=models.CASCADE, related_name='galleria_4')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 3')
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 4')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 5')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 6')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 7')
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 8')
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 9')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 10')
    image_11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 11')
    image_12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 12 ')
    image_13 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 13')
    image_14 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 14')
    image_15 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 15')
    image_16 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 16')
    image_17 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 17')
    image_18 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 18')
    image_19 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 19')
    image_20 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 20')
    image_21 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 21')
    image_22 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 22')
    image_23 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 23')
    image_24 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 24')
    image_25 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 25')
    image_26 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 26')
    image_27 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 27')
    image_28 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 28')
    image_29 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 29')
    image_30 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 30')
    image_31 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 31')
    image_32 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 32')
    image_33 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 33')
    image_34 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 34')
    image_35 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 35')
    image_36 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 36')
    image_37 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 37')
    image_38 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 38')
    image_39 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 39')
    image_40 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 40')
    image_41 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 41')
    image_42 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 42 ')
    image_43 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 43')
    image_44 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 44')
    image_45 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 45')
    image_46 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 46')
    image_47 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 47')
    image_48 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 48')
    image_49 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 49')
    image_50 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 50')
    image_51 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 51')
    image_52 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 52')
    image_53 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 53')
    image_54 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 54')
    image_55 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 55')
    image_56 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 56')
    image_57 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 57')
    image_58 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 58')
    image_59 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 59')
    image_60 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 60')
     

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image_9'),
        ImageChooserPanel('image_10'),
        ImageChooserPanel('image_11'),
        ImageChooserPanel('image_12'),
        ImageChooserPanel('image_13'),
        ImageChooserPanel('image_14'),
        ImageChooserPanel('image_15'),
        ImageChooserPanel('image_16'),
        ImageChooserPanel('image_17'),
        ImageChooserPanel('image_18'),
        ImageChooserPanel('image_19'),
        ImageChooserPanel('image_20'),
        ImageChooserPanel('image_21'),
        ImageChooserPanel('image_22'),
        ImageChooserPanel('image_23'),
        ImageChooserPanel('image_24'),
        ImageChooserPanel('image_25'),
        ImageChooserPanel('image_26'),
        ImageChooserPanel('image_27'),
        ImageChooserPanel('image_28'),
        ImageChooserPanel('image_29'),
        ImageChooserPanel('image_30'),
        ImageChooserPanel('image_31'),
        ImageChooserPanel('image_32'),
        ImageChooserPanel('image_33'),
        ImageChooserPanel('image_34'),
        ImageChooserPanel('image_35'),
        ImageChooserPanel('image_36'),
        ImageChooserPanel('image_37'),
        ImageChooserPanel('image_38'),
        ImageChooserPanel('image_39'),
        ImageChooserPanel('image_40'),
        ImageChooserPanel('image_41'),
        ImageChooserPanel('image_42'),
        ImageChooserPanel('image_43'),
        ImageChooserPanel('image_44'),
        ImageChooserPanel('image_45'),
        ImageChooserPanel('image_46'),
        ImageChooserPanel('image_47'),
        ImageChooserPanel('image_48'),
        ImageChooserPanel('image_49'),
        ImageChooserPanel('image_50'),
        ImageChooserPanel('image_51'),
        ImageChooserPanel('image_52'),
        ImageChooserPanel('image_53'),
        ImageChooserPanel('image_54'),
        ImageChooserPanel('image_55'),
        ImageChooserPanel('image_56'),
        ImageChooserPanel('image_57'),
        ImageChooserPanel('image_58'),
        ImageChooserPanel('image_59'),
        ImageChooserPanel('image_60'),
        
    ]

class consultas_Doc(AbstractFormField):
    page = ParentalKey('Documentary', on_delete=models.CASCADE, related_name='form_fields')

class Documentary(AbstractEmailForm):
    # Empieza Galeria de Imagenes
    template = "webapp_0/Documentary.html"
    
    Ad_info = models.CharField(max_length= 500, null=True, blank=True,verbose_name='Documentary info')
    Ad_link = RichTextField(blank=True,verbose_name='Enlace para volver al inicio')
    Ad_info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-1 info')
    Ad_date1 = models.DateField("Fecha de Advertising-1",null=True, blank=True)
    Ad_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-2 info')
    Ad_date2 = models.DateField("Fecha de Advertising-2",null=True, blank=True)
    Ad_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-3 info')
    Ad_date3 = models.DateField("Fecha de Advertising-3",null=True, blank=True)
    Ad_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-4 info')
    Ad_date4 = models.DateField("Fecha de Advertising-4",null=True, blank=True)
    Ad_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-5 info')
    Ad_date5 = models.DateField("Fecha de Advertising-5",null=True, blank=True)
    Ad_info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-6 info')
    Ad_date6 = models.DateField("Fecha de Advertising-6",null=True, blank=True)
    Ad_info7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-7 info')
    Ad_date7 = models.DateField("Fecha de Advertising-7",null=True, blank=True)
    Ad_info8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-8 info')
    Ad_date8 = models.DateField("Fecha de Advertising-8",null=True, blank=True)
    Ad_info9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-9 info')
    Ad_date9 = models.DateField("Fecha de Advertising-9",null=True, blank=True)
    Ad_info10 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-10 info')
    Ad_date10 = models.DateField("Fecha de Advertising-10",null=True, blank=True)
    Ad_info11 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-11 info')
    Ad_date11 = models.DateField("Fecha de Advertising-11",null=True, blank=True)
    Ad_info12 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-12 info')
    Ad_date12 = models.DateField("Fecha de Advertising-12",null=True, blank=True)
    Ad_info13 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-13 info')
    Ad_date13 = models.DateField("Fecha de Advertising-13",null=True, blank=True)
    Ad_info14 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-14 info')
    Ad_date14 = models.DateField("Fecha de Advertising-14",null=True, blank=True)
    Ad_info15 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-15 info')
    Ad_date15 = models.DateField("Fecha de Advertising-15",null=True, blank=True)
    Ad_info16 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-16 info')
    Ad_date16 = models.DateField("Fecha de Advertising-16",null=True, blank=True)
    Ad_info17 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-17 info')
    Ad_date17 = models.DateField("Fecha de Advertising-17",null=True, blank=True)
    Ad_info18 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-18 info')
    Ad_date18 = models.DateField("Fecha de Advertising-18",null=True, blank=True)
    Ad_info19 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-19 info')
    Ad_date19 = models.DateField("Fecha de Advertising-19",null=True, blank=True)
    Ad_info20 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-20 info')
    Ad_date20 = models.DateField("Fecha de Advertising-20",null=True, blank=True)
    Ad_info21 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-21 info')
    Ad_date21 = models.DateField("Fecha de Advertising-21",null=True, blank=True)
    Ad_info22 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-22 info')
    Ad_date22 = models.DateField("Fecha de Advertising-22",null=True, blank=True)
    Ad_info23 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-23 info')
    Ad_date23 = models.DateField("Fecha de Advertising-23",null=True, blank=True)
    Ad_info24 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-24 info')
    Ad_date24 = models.DateField("Fecha de Advertising-24",null=True, blank=True)
    Ad_info25 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-25 info')
    Ad_date25 = models.DateField("Fecha de Advertising-25",null=True, blank=True)
    Ad_info26 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-26 info')
    Ad_date26 = models.DateField("Fecha de Advertising-26",null=True, blank=True)
    Ad_info27 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-27 info')
    Ad_date27 = models.DateField("Fecha de Advertising-27",null=True, blank=True)
    Ad_info28 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-28 info')
    Ad_date28 = models.DateField("Fecha de Advertising-28",null=True, blank=True)
    Ad_info29 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-29 info')
    Ad_date29 = models.DateField("Fecha de Advertising-29",null=True, blank=True)
    Ad_info30 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-30 info')
    Ad_date30 = models.DateField("Fecha de Advertising-30",null=True, blank=True)
    Ad_info31 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-31 info')
    Ad_date31 = models.DateField("Fecha de Advertising-31",null=True, blank=True)
    Ad_info32 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-32 info')
    Ad_date32 = models.DateField("Fecha de Advertising-32",null=True, blank=True)
    Ad_info33 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-33 info')
    Ad_date33 = models.DateField("Fecha de Advertising-33",null=True, blank=True)
    Ad_info34 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-34 info')
    Ad_date34 = models.DateField("Fecha de Advertising-34",null=True, blank=True)
    Ad_info35 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-35 info')
    Ad_date35 = models.DateField("Fecha de Advertising-35",null=True, blank=True)
    Ad_info36 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-36 info')
    Ad_date36 = models.DateField("Fecha de Advertising-36",null=True, blank=True)
    Ad_info37 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-37 info')
    Ad_date37 = models.DateField("Fecha de Advertising-37",null=True, blank=True)
    Ad_info38 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-38 info')
    Ad_date38 = models.DateField("Fecha de Advertising-38",null=True, blank=True)
    Ad_info39 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-39 info')
    Ad_date39 = models.DateField("Fecha de Advertising-39",null=True, blank=True)
    Ad_info40 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-40 info')
    Ad_date40 = models.DateField("Fecha de Advertising-40",null=True, blank=True)
    Ad_info41 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-41 info')
    Ad_date41 = models.DateField("Fecha de Advertising-41",null=True, blank=True)
    Ad_info42 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-42 info')
    Ad_date42 = models.DateField("Fecha de Advertising-42",null=True, blank=True)
    Ad_info43 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-43 info')
    Ad_date43 = models.DateField("Fecha de Advertising-43",null=True, blank=True)
    Ad_info44 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-44 info')
    Ad_date44 = models.DateField("Fecha de Advertising-44",null=True, blank=True)
    Ad_info45 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-45 info')
    Ad_date45 = models.DateField("Fecha de Advertising-45",null=True, blank=True)
    Ad_info46 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-46 info')
    Ad_date46 = models.DateField("Fecha de Advertising-46",null=True, blank=True)
    Ad_info47 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-47 info')
    Ad_date47 = models.DateField("Fecha de Advertising-47",null=True, blank=True)
    Ad_info48 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-48 info')
    Ad_date48 = models.DateField("Fecha de Advertising-48",null=True, blank=True)
    Ad_info49 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-49 info')
    Ad_date49 = models.DateField("Fecha de Advertising-49",null=True, blank=True)
    Ad_info50 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-50 info')
    Ad_date50 = models.DateField("Fecha de Advertising-50",null=True, blank=True)
    Ad_info51 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-51 info')
    Ad_date51 = models.DateField("Fecha de Advertising-51",null=True, blank=True)
    Ad_info52 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-52 info')
    Ad_date52 = models.DateField("Fecha de Advertising-52",null=True, blank=True)
    Ad_info53 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-53 info')
    Ad_date53 = models.DateField("Fecha de Advertising-53",null=True, blank=True)
    Ad_info54 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-54 info')
    Ad_date54 = models.DateField("Fecha de Advertising-54",null=True, blank=True)
    Ad_info55 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-55 info')
    Ad_date55 = models.DateField("Fecha de Advertising-55",null=True, blank=True)
    Ad_info56 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-56 info')
    Ad_date56 = models.DateField("Fecha de Advertising-56",null=True, blank=True)
    Ad_info57 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-57 info')
    Ad_date57 = models.DateField("Fecha de Advertising-57",null=True, blank=True)
    Ad_info58 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-58 info')
    Ad_date58 = models.DateField("Fecha de Advertising-58",null=True, blank=True)
    Ad_info59 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-59 info')
    Ad_date59 = models.DateField("Fecha de Advertising-59",null=True, blank=True)
    Ad_info60 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Advertising-60 info')
    Ad_date60 = models.DateField("Fecha de Advertising-60",null=True, blank=True)
    # Comentario de Galeria
    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)


    
    
    content_panels = Page.content_panels + [
        FieldPanel('Ad_info', classname="full"),
        FieldPanel('Ad_link', classname="full"),
        FieldPanel('Ad_info1', classname="full"),
        FieldPanel('Ad_date1', classname="full"),
        FieldPanel('Ad_info2', classname="full"),
        FieldPanel('Ad_date2', classname="full"),
        FieldPanel('Ad_info3', classname="full"),
        FieldPanel('Ad_date3', classname="full"),
        FieldPanel('Ad_info4', classname="full"),
        FieldPanel('Ad_date4', classname="full"),
        FieldPanel('Ad_info5', classname="full"),
        FieldPanel('Ad_date5', classname="full"),
        FieldPanel('Ad_info6', classname="full"),
        FieldPanel('Ad_date6', classname="full"),
        FieldPanel('Ad_info7', classname="full"),
        FieldPanel('Ad_date7', classname="full"),
        FieldPanel('Ad_info8', classname="full"),
        FieldPanel('Ad_date8', classname="full"),
        FieldPanel('Ad_info9', classname="full"),
        FieldPanel('Ad_date9', classname="full"),
        FieldPanel('Ad_info10', classname="full"),
        FieldPanel('Ad_date10', classname="full"),
        FieldPanel('Ad_info11', classname="full"),
        FieldPanel('Ad_date11', classname="full"),
        FieldPanel('Ad_info12', classname="full"),
        FieldPanel('Ad_date12', classname="full"),
        FieldPanel('Ad_info13', classname="full"),
        FieldPanel('Ad_date13', classname="full"),
        FieldPanel('Ad_info14', classname="full"),
        FieldPanel('Ad_date14', classname="full"),
        FieldPanel('Ad_info15', classname="full"),
        FieldPanel('Ad_date15', classname="full"),
        FieldPanel('Ad_info16', classname="full"),
        FieldPanel('Ad_date16', classname="full"),
        FieldPanel('Ad_info17', classname="full"),
        FieldPanel('Ad_date17', classname="full"),
        FieldPanel('Ad_info18', classname="full"),
        FieldPanel('Ad_date18', classname="full"),
        FieldPanel('Ad_info19', classname="full"),
        FieldPanel('Ad_date19', classname="full"),
        FieldPanel('Ad_info20', classname="full"),
        FieldPanel('Ad_date20', classname="full"),
        FieldPanel('Ad_info21', classname="full"),
        FieldPanel('Ad_date21', classname="full"),
        FieldPanel('Ad_info22', classname="full"),
        FieldPanel('Ad_date22', classname="full"),
        FieldPanel('Ad_info23', classname="full"),
        FieldPanel('Ad_date23', classname="full"),
        FieldPanel('Ad_info24', classname="full"),
        FieldPanel('Ad_date24', classname="full"),
        FieldPanel('Ad_info25', classname="full"),
        FieldPanel('Ad_date25', classname="full"),
        FieldPanel('Ad_info26', classname="full"),
        FieldPanel('Ad_date26', classname="full"),
        FieldPanel('Ad_info27', classname="full"),
        FieldPanel('Ad_date27', classname="full"),
        FieldPanel('Ad_info28', classname="full"),
        FieldPanel('Ad_date28', classname="full"),
        FieldPanel('Ad_info29', classname="full"),
        FieldPanel('Ad_date29', classname="full"),
        FieldPanel('Ad_info30', classname="full"),
        FieldPanel('Ad_date30', classname="full"),
        FieldPanel('Ad_info31', classname="full"),
        FieldPanel('Ad_date31', classname="full"),
        FieldPanel('Ad_info32', classname="full"),
        FieldPanel('Ad_date32', classname="full"),
        FieldPanel('Ad_info33', classname="full"),
        FieldPanel('Ad_date33', classname="full"),
        FieldPanel('Ad_info34', classname="full"),
        FieldPanel('Ad_date34', classname="full"),
        FieldPanel('Ad_info35', classname="full"),
        FieldPanel('Ad_date35', classname="full"),
        FieldPanel('Ad_info36', classname="full"),
        FieldPanel('Ad_date36', classname="full"),
        FieldPanel('Ad_info37', classname="full"),
        FieldPanel('Ad_date37', classname="full"),
        FieldPanel('Ad_info38', classname="full"),
        FieldPanel('Ad_date38', classname="full"),
        FieldPanel('Ad_info39', classname="full"),
        FieldPanel('Ad_date39', classname="full"),
        FieldPanel('Ad_info40', classname="full"),
        FieldPanel('Ad_date40', classname="full"),
        FieldPanel('Ad_info41', classname="full"),
        FieldPanel('Ad_date41', classname="full"),
        FieldPanel('Ad_info42', classname="full"),
        FieldPanel('Ad_date42', classname="full"),
        FieldPanel('Ad_info43', classname="full"),
        FieldPanel('Ad_date43', classname="full"),
        FieldPanel('Ad_info44', classname="full"),
        FieldPanel('Ad_date44', classname="full"),
        FieldPanel('Ad_info45', classname="full"),
        FieldPanel('Ad_date45', classname="full"),
        FieldPanel('Ad_info46', classname="full"),
        FieldPanel('Ad_date46', classname="full"),
        FieldPanel('Ad_info47', classname="full"),
        FieldPanel('Ad_date47', classname="full"),
        FieldPanel('Ad_info48', classname="full"),
        FieldPanel('Ad_date48', classname="full"),
        FieldPanel('Ad_info49', classname="full"),
        FieldPanel('Ad_date49', classname="full"),
        FieldPanel('Ad_info50', classname="full"),
        FieldPanel('Ad_date50', classname="full"),
        FieldPanel('Ad_info51', classname="full"),
        FieldPanel('Ad_date51', classname="full"),
        FieldPanel('Ad_info52', classname="full"),
        FieldPanel('Ad_date52', classname="full"),
        FieldPanel('Ad_info53', classname="full"),
        FieldPanel('Ad_date53', classname="full"),
        FieldPanel('Ad_info54', classname="full"),
        FieldPanel('Ad_date54', classname="full"),
        FieldPanel('Ad_info55', classname="full"),
        FieldPanel('Ad_date55', classname="full"),
        FieldPanel('Ad_info56', classname="full"),
        FieldPanel('Ad_date56', classname="full"),
        FieldPanel('Ad_info57', classname="full"),
        FieldPanel('Ad_date57', classname="full"),
        FieldPanel('Ad_info58', classname="full"),
        FieldPanel('Ad_date58', classname="full"),
        FieldPanel('Ad_info59', classname="full"),
        FieldPanel('Ad_date59', classname="full"),
        FieldPanel('Ad_info60', classname="full"),
        FieldPanel('Ad_date60', classname="full"),
        FieldPanel('consulta', classname="full"),
        InlinePanel('galleria_5', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # If you need to show results only on landing page,
        # you may need check request.method

        results = dict()
        # Get information about form fields
        data_fields = [
            (field.clean_name, field.label)
            for field in self.get_form_fields()
        ]

        # Get all submissions for current page
        submissions = self.get_submission_class().objects.filter(page=self)
        for submission in submissions:
            data = submission.get_data()

            # Count results for each question
            for name, label in data_fields:
                answer = data.get(name)
                if answer is None:
                    # Something wrong with data.
                    # Probably you have changed questions
                    # and now we are receiving answers for old questions.
                    # Just skip them.
                    continue

                if type(answer) is list:
                    # Answer is a list if the field type is 'Checkboxes'
                    answer = u', '.join(answer)

                question_stats = results.get(label, {})
                question_stats[answer] = question_stats.get(answer, 0) + 1
                results[label] = question_stats

        context.update({
            'results': results,
        })
        return context

class GaleriadeImagenes5(Orderable):
    page = ParentalKey(Documentary, on_delete=models.CASCADE, related_name='galleria_5')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 3')
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 4')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 5')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 6')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 7')
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 8')
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 9')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 10')
    image_11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 11')
    image_12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 12 ')
    image_13 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 13')
    image_14 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 14')
    image_15 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 15')
    image_16 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 16')
    image_17 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 17')
    image_18 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 18')
    image_19 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 19')
    image_20 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 20')
    image_21 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 21')
    image_22 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 22')
    image_23 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 23')
    image_24 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 24')
    image_25 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 25')
    image_26 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 26')
    image_27 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 27')
    image_28 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 28')
    image_29 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 29')
    image_30 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 30')
    image_31 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 31')
    image_32 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 32')
    image_33 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 33')
    image_34 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 34')
    image_35 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 35')
    image_36 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 36')
    image_37 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 37')
    image_38 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 38')
    image_39 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 39')
    image_40 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 40')
    image_41 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 41')
    image_42 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 42 ')
    image_43 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 43')
    image_44 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 44')
    image_45 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 45')
    image_46 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 46')
    image_47 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 47')
    image_48 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 48')
    image_49 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 49')
    image_50 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 50')
    image_51 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 51')
    image_52 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 52')
    image_53 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 53')
    image_54 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 54')
    image_55 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 55')
    image_56 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 56')
    image_57 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 57')
    image_58 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 58')
    image_59 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 59')
    image_60 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto 60')
     

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image_9'),
        ImageChooserPanel('image_10'),
        ImageChooserPanel('image_11'),
        ImageChooserPanel('image_12'),
        ImageChooserPanel('image_13'),
        ImageChooserPanel('image_14'),
        ImageChooserPanel('image_15'),
        ImageChooserPanel('image_16'),
        ImageChooserPanel('image_17'),
        ImageChooserPanel('image_18'),
        ImageChooserPanel('image_19'),
        ImageChooserPanel('image_20'),
        ImageChooserPanel('image_21'),
        ImageChooserPanel('image_22'),
        ImageChooserPanel('image_23'),
        ImageChooserPanel('image_24'),
        ImageChooserPanel('image_25'),
        ImageChooserPanel('image_26'),
        ImageChooserPanel('image_27'),
        ImageChooserPanel('image_28'),
        ImageChooserPanel('image_29'),
        ImageChooserPanel('image_30'),
        ImageChooserPanel('image_31'),
        ImageChooserPanel('image_32'),
        ImageChooserPanel('image_33'),
        ImageChooserPanel('image_34'),
        ImageChooserPanel('image_35'),
        ImageChooserPanel('image_36'),
        ImageChooserPanel('image_37'),
        ImageChooserPanel('image_38'),
        ImageChooserPanel('image_39'),
        ImageChooserPanel('image_40'),
        ImageChooserPanel('image_41'),
        ImageChooserPanel('image_42'),
        ImageChooserPanel('image_43'),
        ImageChooserPanel('image_44'),
        ImageChooserPanel('image_45'),
        ImageChooserPanel('image_46'),
        ImageChooserPanel('image_47'),
        ImageChooserPanel('image_48'),
        ImageChooserPanel('image_49'),
        ImageChooserPanel('image_50'),
        ImageChooserPanel('image_51'),
        ImageChooserPanel('image_52'),
        ImageChooserPanel('image_53'),
        ImageChooserPanel('image_54'),
        ImageChooserPanel('image_55'),
        ImageChooserPanel('image_56'),
        ImageChooserPanel('image_57'),
        ImageChooserPanel('image_58'),
        ImageChooserPanel('image_59'),
        ImageChooserPanel('image_60'),
        
    ]



