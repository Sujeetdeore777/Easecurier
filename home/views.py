from django.shortcuts import render, redirect,get_object_or_404

from django.views import View
from datetime import datetime
from django.contrib import messages

from .models import Mainheader 
from .models import Mainimg 
from .models import Subimg 
from .models import Buisness
from .models import Buisnessdetails
from .models import Plan
from .models import Whychooesus
from .models import  Slideimg_rightdescription_active
from .models import  Slideimg_rightdescription
from .models import  Cartheading
from .models import  Cart
from .models import  Slidercart
from .models import  Slidermaincart
from .models import  Slidermaincart2
from .models import  Brandtext
from .models import  Brandimg
from .models import  Brandimg2
from .models import  Suggested
from .models import  Suggestedheading
from .models import  Newsheading
from .models import  Newsimg

from .models import  featureheading
from .models import  Featurecard
from .models import  featureheading2
from .models import  Featurecard2

from .models import  Prisingheading
from .models import  Prisingcart
from .models import  Prisingcart2heading
from .models import  Prisingcart2
from .models import  Faqheading
from .models import  Faq
from .models import  Last

from .models import  Aboutusstart
from .models import  Counter
from .models import  Counterheading
from .models import  Trustedbuisness_img
from .models import  Trustedbuisness_heading
from .models import  Newssection_img
from .models import  News_section
from .models import  Ourteam_section
from .models import  Team_member

from .models import  Track_order

from .models import  Hyperlocal_service
from .models import  Hyperlocal_card_info
from .models import  Hyperlocal_card
from .models import  Hyperlocal_info
from .models import  Hyperlocal_company_info
from .models import  Hyperlocal_comapny_images
from .models import  Hyperlocal_places
from .models import  Hyperlocal_company_images
from .models import  Hyperlocal_slider_info
from .models import  Hyperlocal_image_slider
from .models import  Hyperlocal_review
from .models import  Hyperlocal_review_card
from .models import  Hyperlocal_testimonials
from .models import  Hyperlocal_company_info1
from .models import  Hyperlocal_company_logo
from .models import  Hyperlocal_Suggetion
from .models import  Hyperlocal_faq_info
from .models import  Hyperlocal_faq
from .models import  Hyperlocal_end


from .models import  Bulk_service
from .models import  Bulk_service_info
from .models import  Bulk_card_info
from .models import  Bulk_card_data
from .models import  Bulk_info
from .models import  Bulk_info1
from .models import  Bulk_card_information
from .models import  Bulk_card
from .models import  Bulk_slider
from .models import  Bulk_company_slider
from .models import  Bulk_review
from .models import  Bulk_review_card
from .models import  Bulk_testimonials
from .models import  Bulk_company_info
from .models import  Bulk_company_logo
from .models import  Bulk_Suggetion_info
from .models import  Bulk_Suggetion
from .models import  Bulk_end

from .models import Sprint_service,Sprint_faq,Sprint_card_info,Sprint_card,Sprint_info,Sprint_install_info
from .models import Sprint_information,Sprint_slider_info,Sprint_company_slider,Sprint_review,Sprint_review_card
from .models import Sprint_end,Sprint_testimonials,Sprint_faq_info,Sprint_company_info,Sprint_company_logo,Sprint_Suggetion_info,Sprint_Suggetion



from .models import Faq_page,Faq_info_card,Faq_section_card,Faq_card


from .models import Glosary
from .models import Media_feature,Media_feature_card,Media_card_info,Media_card


from .models import Single,Single_card_info,Single_card,Single_info,Single_icon
from .models import Double,Double_card_info,Double_card,Double_info,Double_icon
from .models import Triple,Triple_card_info,Triple_card,Triple_info,Triple_icon

from .models import International_service1,International_card_info,International_card,International_info,International_places
from .models import International_feature_images,International_slider_info,International_company_slider,International_review,International_review_card
from .models import International_testimonials,International_company_info,International_company_logo,International_Suggetion_info,International_Suggetion,International_faq_info,International_faq,International_end,International_infocard

from .models import Ecommerce_service,Ecommerce_card_info,Ecommerce_info,Ecommerce_card_information,Ecommerce_card,Ecommerce_slider,Ecommerce_company_slider
from .models import Ecommerce_review,Ecommerce_review_card,Ecommerce_testimonials,Ecommerce_company_info,Ecommerce_company_logo,Ecommerce_Suggetion_info,Ecommerce_Suggetion
from .models import Ecommerce_faq_info,Ecommerce_faq,Ecommerce_end,Ecommerce_info1,Ecommerce_serviceneww

from .models import  Registerfirst
from .models import  Logisticheading
from .models import  Logisticdetails
from .models import  Partnersdetails
from .models import  Features
from .models import  Trusted
from .models import  Trustedcards






def register(request):
    registerfirst = Registerfirst.objects.first()
    logisticheading = Logisticheading.objects.first()
    logisticdetails = Logisticdetails.objects.all()
    partnersdetails = Partnersdetails.objects.all()
    features = Features.objects.all()
    trusted = Trusted.objects.first()
    trustedcards = Trustedcards.objects.all()
    data ={
       
        "registerfirst":registerfirst,
        'logisticheading':logisticheading,
        'logisticdetails':logisticdetails,
        'partnersdetails':partnersdetails,
        'features':features,
        'trusted':trusted,
        'trustedcards':trustedcards
    
          }
    return render(request, 'register.html',data)




def international(request):
    international_service = International_service1.objects.first()
    international_card_info = International_card_info.objects.first()
    international_card = International_card.objects.all()
    international_info = International_info.objects.first()
    international_infocard = International_infocard.objects.all()
    international_places= International_places.objects.first()
    international_feature_images= International_feature_images.objects.all()
    international_slider_info= International_slider_info.objects.first()
    international_company_slider= International_company_slider.objects.all()
    international_review= International_review.objects.first()
    international_review_card= International_review_card.objects.all()
    international_testimonials= International_testimonials.objects.all()
    international_company_info= International_company_info.objects.first()
    international_company_logo= International_company_logo.objects.all()
    international_Suggetion_info= International_Suggetion_info.objects.first()
    international_Suggetion=International_Suggetion.objects.all()
    international_faq_info= International_faq_info.objects.first()
    international_faq= International_faq.objects.all()
    international_end= International_end.objects.first()
    
    data ={
        'international_service' : international_service,
        'international_card_info' :international_card_info,
        'international_card' :international_card,
        'international_info' :international_info,
        'international_info1': international_infocard,
        'international_places' : international_places,
        'international_feature_images' : international_feature_images,
        'international_slider_info' :international_slider_info,
        'international_company_slider' :international_company_slider,
        'international_review' : international_review,
        'international_review_card' :international_review_card,
        'international_testimonials' :international_testimonials,
        'international_company_info' :international_company_info,
        'international_company_logo' :international_company_logo,
        'international_Suggetion_info' :international_Suggetion_info,
        'international_Suggetion' :international_Suggetion,
        'international_faq_info' :international_faq_info,
        'international_faq' :international_faq,
        'international_end' :international_end
        
    
          }
    return render(request, 'international.html',data)


def ecommerce(request):
    
    ecommerce_serviceneww = Ecommerce_serviceneww.objects.first()

    ecommerce_service = Ecommerce_service.objects.first()
    ecommerce_card_info = Ecommerce_card_info.objects.first()
    ecommerce_info= Ecommerce_info.objects.first()
    ecommerce_infoform= Ecommerce_info1.objects.all()
    ecommerce_card_information= Ecommerce_card_information.objects.first()
    ecommerce_card= Ecommerce_card.objects.all()
    ecommerce_slider= Ecommerce_slider.objects.first()
    ecommerce_company_slider= Ecommerce_company_slider.objects.all()
    ecommerce_review= Ecommerce_review.objects.first()
    ecommerce_review_card= Ecommerce_review_card.objects.all()
    ecommerce_testimonials= Ecommerce_testimonials.objects.all()
    ecommerce_company_info= Ecommerce_company_info.objects.first()
    ecommerce_company_logo= Ecommerce_company_logo.objects.all()
    ecommerce_Suggetion_info= Ecommerce_Suggetion_info.objects.first()
    ecommerce_Suggetion= Ecommerce_Suggetion.objects.all()
    ecommerce_faq_info= Ecommerce_faq_info.objects.first()
    ecommerce_faq= Ecommerce_faq.objects.all()
    ecommerce_end=Ecommerce_end.objects.first()
    
    data ={
        'ecommerce_serviceneww':ecommerce_serviceneww,
        'ecommerce_service1' : ecommerce_service,
        'ecommerce_card_info' : ecommerce_card_info,
        'ecommerce_info' :ecommerce_info,
        'ecommerce_infoform' :ecommerce_infoform,
        'ecommerce_card_information' :ecommerce_card_information,
        'ecommerce_card' : ecommerce_card,
        'ecommerce_slider' : ecommerce_slider,
        'ecommerce_company_slider' : ecommerce_company_slider,
        'ecommerce_review' : ecommerce_review,
        'ecommerce_review_card' : ecommerce_review_card,
        'ecommerce_testimonials' : ecommerce_testimonials,
        'ecommerce_company_info' : ecommerce_company_info,
        'ecommerce_company_logo' : ecommerce_company_logo,
        'ecommerce_Suggetion_info' :ecommerce_Suggetion_info,
        'ecommerce_Suggetion' : ecommerce_Suggetion,
        'ecommerce_faq_info' : ecommerce_faq_info,
        'ecommerce_faq' :ecommerce_faq,
        'ecommerce_end' :ecommerce_end,
      
          }
    
    return render(request, 'ecommerce.html', data)

def sprint(request):
    top = Sprint_service.objects.first()
    cardinfo = Sprint_card_info.objects.first()
    card = Sprint_card.objects.all()
    info = Sprint_info.objects.first()
    install_info = Sprint_install_info.objects.all()
    information = Sprint_information.objects.all()
    slider_info = Sprint_slider_info.objects.first()
    slider_image = Sprint_company_slider.objects.all()
    review_card_info= Sprint_review.objects.first()
    review_card = Sprint_review_card.objects.all()
    testimonials = Sprint_testimonials.objects.all()
    company_info = Sprint_company_info.objects.first()
    company_logo = Sprint_company_logo.objects.all()
    suggetion_info = Sprint_Suggetion_info.objects.first()
    suggestion = Sprint_Suggetion.objects.all()
    faq_info = Sprint_faq_info.objects.first()
    faq = Sprint_faq.objects.all()
    end= Sprint_end.objects.first()
    
    data={ 
            'top': top,
            'cardinfo': cardinfo,
            'card': card,
            'info': info,
            'install_info' : install_info,
            'information' : information,
            'slider_info': slider_info,
            'slider_image': slider_image,
            'review_card_info' :review_card_info,
            'review_card' : review_card,
            'testimonials' : testimonials,
            'company_info' : company_info,
            'company_logo' : company_logo,
            'suggetion_info' : suggetion_info,
            'suggestion': suggestion,
            'faq_info' :faq_info,
            'faq' : faq,
            'end' : end
            
     }
    
    return render(request, 'sprint.html',data)


def faq(request):
   faq = Faq_page.objects.first()
   info_card = Faq_info_card.objects.all()
   section_card = Faq_section_card.objects.all()
   faq_card = Faq_card.objects.all()
   
   data={
       
        'faqpage': faq,
        'info_card' : info_card,
        'section_card' :section_card,
        'faq_card' :faq_card
        
        
   }
   return render(request, 'faq.html',data)



def glosary(request):
    glosary = Glosary.objects.all()
    data={
        
        'glosary':glosary
    }
    return render(request, 'glosary.html',data)

def mediafeature(request):
    feature = Media_feature.objects.first()
    feature_card = Media_feature_card.objects.all()
    card_info = Media_card_info.objects.first()
    media_card = Media_card.objects.all()
    
    data={
        
        
        'feature' : feature,
        'feature_card' : feature_card,
        'card_info' : card_info,
        'media_card' : media_card
        
        
    }
    return render(request, 'mediafeature.html',data)


def single(request):
   single =Single.objects.first()
   card_info= Single_card_info.objects.first()
   single_card= Single_card.objects.all()
   single_info=Single_info.objects.first()
   single_icon=Single_icon.objects.all()
   
   data={
       
        'single' : single,
        'card_info'  : card_info,
        'single_card' : single_card,
        'single_info' : single_info,
        'single_icon' : single_icon
    }
   return render(request, 'single.html',data)


def double(request):
   double = Double.objects.first()
   card_info= Double_card_info.objects.first()
   double_card= Double_card.objects.all()
   double_info=Double_info.objects.first()
   double_icon=Double_icon.objects.all()
   
   data={
       
        'double1' : double,
        'double_card_info'  : card_info,
        'double_card' : double_card,
        'double_info' : double_info,
        'double_icon' : double_icon,
   }
       
   return render(request, 'single.html',data)



def triple(request):
   triple = Triple.objects.first()
   card_info= Triple_card_info.objects.first()
   triple_card= Triple_card.objects.all()
   triple_info= Triple_info.objects.first()
   triple_icon= Triple_icon.objects.all()
   
   data={
       
        'triple' : triple,
        'triple_card_info'  : card_info,
        'triple_card' : triple_card,
        'triple_info' : triple_info,
        'triple_icon' : triple_icon
    }
   return render(request, 'single.html',data)









def bulk(request):
     bulk_service=Bulk_service.objects.first()
     bulk_service_info=Bulk_service_info.objects.first()
     bulk_card_info=Bulk_card_info.objects.first()
     bulk_card_data=Bulk_card_data.objects.all()
     bulk_info=Bulk_info.objects.first()
     bulk_info1=Bulk_info1.objects.all()
     bulk_card_information=Bulk_card_information.objects.first()
     bulk_card=Bulk_card.objects.all()
     bulk_slider=Bulk_slider.objects.first()
     bulk_company_slider=Bulk_company_slider.objects.all()
     bulk_review=Bulk_review.objects.first()
     bulk_review_card=Bulk_review_card.objects.all()
     bulk_testimonials=Bulk_testimonials.objects.all()
     bulk_company_info=Bulk_company_info.objects.first()
     bulk_company_logo=Bulk_company_logo.objects.all()
     bulk_Suggetion_info=Bulk_Suggetion_info.objects.first()
     bulk_Suggetion=Bulk_Suggetion.objects.all()
     bulk_end=Bulk_end.objects.first()
     

     data={ 
            'bulk_service':bulk_service,
            'bulk_service_info':bulk_service_info,
            'bulk_card_info':bulk_card_info,
            'bulk_card_data':bulk_card_data,
            'bulk_info':bulk_info,
            'bulk_info1':bulk_info1,
            'bulk_card_information':bulk_card_information,
            'bulk_card':bulk_card,
            'bulk_slider':bulk_slider,
            'bulk_company_slider':bulk_company_slider,
            'bulk_review':bulk_review,
            'bulk_review_card':bulk_review_card,
            'bulk_testimonials':bulk_testimonials,
            'bulk_company_info':bulk_company_info,
            'bulk_company_logo':bulk_company_logo,
            'bulk_Suggetion_info':bulk_Suggetion_info,
            'bulk_Suggetion':bulk_Suggetion,
            'bulk_end':bulk_end
           
        }
     return render(request, 'bulk.html',data)




def hyperlocal(request):
    hyperlocal_service=Hyperlocal_service.objects.first()
    hyperlocal_card_info=Hyperlocal_card_info.objects.first()
    hyperlocal_card1=Hyperlocal_card.objects.all()
    hyperlocal_info=Hyperlocal_info.objects.first()
    hyperlocal_company_info=Hyperlocal_company_info.objects.first()
    hyperlocal_comapny_images=Hyperlocal_comapny_images.objects.all()
    hyperlocal_places=Hyperlocal_places.objects.first()
    hyperlocal_company_images=Hyperlocal_company_images.objects.all()
    hyperlocal_slider_info=Hyperlocal_slider_info.objects.first()
    hyperlocal_image_slider=Hyperlocal_image_slider.objects.all()
    hyperlocal_review=Hyperlocal_review.objects.first()
    hyperlocal_review_card=Hyperlocal_review_card.objects.all()
    hyperlocal_testimonials=Hyperlocal_testimonials.objects.all()
    hyperlocal_company_info1=Hyperlocal_company_info1.objects.first()
    hyperlocal_company_logo=Hyperlocal_company_logo.objects.all()  
    hyperlocal_Suggetion=Hyperlocal_Suggetion.objects.all()
    hyperlocal_faq_info=Hyperlocal_faq_info.objects.first()
    hyperlocal_faq=Hyperlocal_faq.objects.all()
    hyperlocal_end=Hyperlocal_end.objects.first()

    data={ 
            'hyperlocal_service':hyperlocal_service,
            'hyperlocal_card_info':hyperlocal_card_info,
            'hyperlocal_card':hyperlocal_card1,
            'hyperlocal_info':hyperlocal_info,
            'hyperlocal_company_info':hyperlocal_company_info,
            'hyperlocal_comapny_images':hyperlocal_comapny_images,
            'hyperlocal_places':hyperlocal_places,
            'hyperlocal_company_images':hyperlocal_company_images,
            'hyperlocal_slider_info':hyperlocal_slider_info,
            'hyperlocal_image_slider':hyperlocal_image_slider,
            'hyperlocal_review':hyperlocal_review,
            'hyperlocal_review_card':hyperlocal_review_card,
            'hyperlocal_testimonials':hyperlocal_testimonials,
            'hyperlocal_company_info1':hyperlocal_company_info1,
            'hyperlocal_company_logo':hyperlocal_company_logo,
            'hyperlocal_Suggetion':hyperlocal_Suggetion,
            'hyperlocal_faq_info':hyperlocal_faq_info,
            'hyperlocal_faq':hyperlocal_faq,
            'hyperlocal_end':hyperlocal_end,
        }
    return render(request, 'hyperlocal.html',data)


def trackorder(request):
    track_order=Track_order.objects.first()
    data={ 
            'track_order':track_order,
        }
    return render(request, 'trackorder.html',data)


def aboutus(request):
    aboutusstart=Aboutusstart.objects.first()
    counterheading=Counterheading.objects.first()
    counter=Counter.objects.all()
    trustedbuisness_img=Trustedbuisness_img.objects.all()
    trustedbuisness_heading=Trustedbuisness_heading.objects.first()
    newssection_img=Newssection_img.objects.all()
    news_section=News_section.objects.first()
    ourteam_section=Ourteam_section.objects.first()
    team_member=Team_member.objects.all()
    data={ 
            'aboutusstart':aboutusstart,
            'counterheading':counterheading,
            'counter':counter,
            'trustedbuisness_img1':trustedbuisness_img,
            'trustedbuisness_heading':trustedbuisness_heading,
            'newssection_img':newssection_img,
            'news_section':news_section,
            'ourteam_section':ourteam_section,
            'team_member':team_member,
        }
    return render(request, 'aboutus.html',data)



def prising(request):
    header=Prisingheading.objects.first()
    cart=Prisingcart.objects.all()
    prisingcart2heading=Prisingcart2heading.objects.first()
    prisingcart2=Prisingcart2.objects.all()
    faqheading=Faqheading.objects.first()
    faq=Faq.objects.all()
    last=Last.objects.first()
    data={ 
            'mainheader':header,
            'cart':cart,
            'prisingcart2heading':prisingcart2heading,
            'prisingcart2':prisingcart2,
            'faqheading':faqheading,
            'faq':faq,
            'last':last,
   
        }
    return render(request, 'prising.html',data)



def features(request):
    header=featureheading.objects.first()
    featurecard=Featurecard.objects.all()
    header2=featureheading2.objects.first()
    featurecard2=Featurecard2.objects.all()
   
    data={ 
            'mainheader':header,
            'featurecard':featurecard,
            'mainheader2':header2,
            'featurecard2':featurecard2
            
        }
    return render(request, 'features.html',data)



def index(request):
     header=Mainheader.objects.first()
     mainimg=Mainimg.objects.first()
     subimg=Subimg.objects.all()
     buisness=Buisness.objects.first()
     buisnessdetails=Buisnessdetails.objects.all()
     plan=Plan.objects.first()
     whychooesus=Whychooesus.objects.first()
     slideimg_rightdescription_active=Slideimg_rightdescription_active.objects.first()
     slideimg_rightdescription=Slideimg_rightdescription.objects.all()
     cartheading=Cartheading.objects.first()
     cart=Cart.objects.all()
     slidercart=Slidercart.objects.first()
     slidermaincart=Slidermaincart.objects.all()
     slidermaincart2=Slidermaincart2.objects.all()
     brandtext=Brandtext.objects.first()
     brandimg=Brandimg.objects.all()
     brandimg2=Brandimg2.objects.all()
     suggested=Suggested.objects.all()
     suggestedheading=Suggestedheading.objects.first()
     newsheading=Newsheading.objects.first()
     newsimg=Newsimg.objects.all()
     
     data={ 
            'mainheader':header,
            'mainimg':mainimg,
            'subimg':subimg,
            'buisness1':buisness,
            'buisnessdetails':buisnessdetails,
            'plan1':plan,
            'slideimg_rightdescription_active':slideimg_rightdescription_active,
            'slideimg_rightdescription':slideimg_rightdescription,
            'cartheading':cartheading,
            'cart':cart,
            'whychooesus':whychooesus,
            'slidercart':slidercart,
            'slidermaincart':slidermaincart,
            'slidermaincart2':slidermaincart2,
            'brandtext':brandtext,
            'brandimg':brandimg,
            'brandimg2':brandimg2,
            'suggested':suggested,
            'suggestedheading':suggestedheading,
            'newsheading':newsheading,
            'newsimg':newsimg,


        }
     return render(request, 'index.html',data)


def base(request):
    return render(request, 'base.html')







def login(request):
    return render(request, 'login.html')







def delta(request):
    return render(request, 'delta.html')
