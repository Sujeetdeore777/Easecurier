from django.contrib import admin
from .models import Mainheader
from .models import Mainimg
from .models import Subimg
from .models import Buisness
from .models import Buisnessdetails
from .models import Plan
from .models import Whychooesus
from .models import Slideimg_rightdescription
from .models import Slideimg_rightdescription_active
from .models import Cartheading
from .models import Cart
from .models import Slidercart
from .models import Slidermaincart
from .models import Slidermaincart2
from .models import Brandtext
from .models import Brandimg
from .models import Brandimg2
from .models import Suggested
from .models import Suggestedheading
from .models import Newsheading
from .models import Newsimg

from .models import featureheading
from .models import Featurecard
from .models import featureheading2
from .models import Featurecard2

from .models import Prisingheading
from .models import Prisingcart
from .models import Prisingcart2heading
from .models import Prisingcart2
from .models import Faqheading
from .models import Faq
from .models import Last

from .models import Aboutusstart
from .models import Counterheading
from .models import Counter
from .models import Trustedbuisness_img
from .models import Trustedbuisness_heading
from .models import News_section
from .models import Newssection_img
from .models import Ourteam_section
from .models import Team_member

from .models import Track_order


from .models import Hyperlocal_service,Hyperlocal_card_info,Hyperlocal_card,Hyperlocal_info,Hyperlocal_company_info
from .models import Hyperlocal_comapny_images,Hyperlocal_places,Hyperlocal_review,Hyperlocal_review_card
from .models import Hyperlocal_company_images,Hyperlocal_slider_info,Hyperlocal_image_slider,Hyperlocal_faq,Hyperlocal_end
from .models import Hyperlocal_testimonials,Hyperlocal_company_info1,Hyperlocal_company_logo,Hyperlocal_Suggetion,Hyperlocal_faq_info

from .models import Bulk_service,Bulk_service_info,Bulk_card_info,Bulk_card_data,Bulk_info,Bulk_info1
from .models import Bulk_card_information,Bulk_card,Bulk_slider,Bulk_company_slider,Bulk_review
from .models import Bulk_review,Bulk_review_card,Bulk_testimonials,Bulk_company_info
from .models import Bulk_company_logo,Bulk_Suggetion_info,Bulk_Suggetion,Bulk_end


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

from .models import Ecommerce_service,Ecommerce_card_info,Ecommerce_info,Ecommerce_info1,Ecommerce_card_information,Ecommerce_card,Ecommerce_slider,Ecommerce_company_slider
from .models import Ecommerce_review,Ecommerce_review_card,Ecommerce_testimonials,Ecommerce_company_info,Ecommerce_company_logo,Ecommerce_Suggetion_info,Ecommerce_Suggetion
from .models import Ecommerce_faq_info,Ecommerce_faq,Ecommerce_end,Ecommerce_serviceneww

from .models import Registerfirst
from .models import Logisticheading
from .models import Logisticdetails
from .models import Partnersdetails
from .models import Features
from .models import Trusted
from .models import Trustedcards





# Register your models here.

admin.site.register(Registerfirst)
admin.site.register(Logisticheading)
admin.site.register(Logisticdetails)
admin.site.register(Partnersdetails)
admin.site.register(Features)
admin.site.register(Trusted)
admin.site.register(Trustedcards)






admin.site.register(Ecommerce_serviceneww)
admin.site.register(Ecommerce_service)
admin.site.register(Ecommerce_card_info)
admin.site.register(Ecommerce_info)
admin.site.register(Ecommerce_info1)
admin.site.register(Ecommerce_card_information)
admin.site.register(Ecommerce_card)
admin.site.register(Ecommerce_slider)
admin.site.register(Ecommerce_company_slider)
admin.site.register(Ecommerce_review)
admin.site.register(Ecommerce_review_card)
admin.site.register(Ecommerce_testimonials)
admin.site.register(Ecommerce_company_info)
admin.site.register(Ecommerce_company_logo)
admin.site.register(Ecommerce_Suggetion_info)
admin.site.register(Ecommerce_Suggetion)
admin.site.register(Ecommerce_faq_info)
admin.site.register(Ecommerce_faq)
admin.site.register(Ecommerce_end)

# Register your models here.
# Register your models here.
admin.site.register(International_service1)
admin.site.register(International_card_info)
admin.site.register(International_card)
admin.site.register(International_info)
admin.site.register(International_infocard)
admin.site.register(International_places)
admin.site.register(International_feature_images)
admin.site.register(International_slider_info)
admin.site.register(International_company_slider)
admin.site.register(International_review)
admin.site.register(International_review_card)
admin.site.register(International_testimonials)
admin.site.register(International_company_info)
admin.site.register(International_company_logo)
admin.site.register(International_Suggetion_info)
admin.site.register(International_Suggetion)
admin.site.register(International_faq_info)
admin.site.register(International_faq)
admin.site.register(International_end)



admin.site.register(Faq_page)
admin.site.register(Faq_info_card)
admin.site.register(Faq_section_card)
admin.site.register(Faq_card)
admin.site.register(Glosary)
admin.site.register(Media_feature)
admin.site.register(Media_feature_card)
admin.site.register(Media_card_info)
admin.site.register(Media_card)

admin.site.register(Single)
admin.site.register(Single_card_info)
admin.site.register(Single_card)
admin.site.register(Single_info)
admin.site.register(Single_icon)


admin.site.register(Double)
admin.site.register(Double_card_info)
admin.site.register(Double_card)
admin.site.register(Double_info)
admin.site.register(Double_icon)




admin.site.register(Triple)
admin.site.register(Triple_card_info)
admin.site.register(Triple_card)
admin.site.register(Triple_info)
admin.site.register(Triple_icon)









admin.site.register(Mainheader)
admin.site.register(Mainimg)
admin.site.register(Subimg)
admin.site.register(Buisness)
admin.site.register(Buisnessdetails)
admin.site.register(Plan)
admin.site.register(Whychooesus)
admin.site.register(Slideimg_rightdescription_active)
admin.site.register(Slideimg_rightdescription)
admin.site.register(Cartheading)
admin.site.register(Cart)
admin.site.register(Slidercart)
admin.site.register(Slidermaincart)
admin.site.register(Slidermaincart2)
admin.site.register(Brandtext)
admin.site.register(Brandimg)
admin.site.register(Brandimg2)
admin.site.register(Suggested)
admin.site.register(Suggestedheading)
admin.site.register(Newsheading)
admin.site.register(Newsimg)

admin.site.register(featureheading)
admin.site.register(Featurecard)
admin.site.register(featureheading2)
admin.site.register(Featurecard2)

admin.site.register(Prisingheading)
admin.site.register(Prisingcart)
admin.site.register(Prisingcart2heading)
admin.site.register(Prisingcart2)
admin.site.register(Faqheading)
admin.site.register(Faq)
admin.site.register(Last)

admin.site.register(Aboutusstart)
admin.site.register(Counterheading)
admin.site.register(Counter)
admin.site.register(Trustedbuisness_img)
admin.site.register(Trustedbuisness_heading)
admin.site.register(News_section)
admin.site.register(Newssection_img)
admin.site.register(Ourteam_section)
admin.site.register(Team_member)

admin.site.register(Track_order)


admin.site.register(Hyperlocal_service)
admin.site.register(Hyperlocal_card_info)
admin.site.register(Hyperlocal_card)
admin.site.register(Hyperlocal_info)
admin.site.register(Hyperlocal_company_info1)
admin.site.register(Hyperlocal_comapny_images)
admin.site.register(Hyperlocal_places)
admin.site.register(Hyperlocal_company_images)
admin.site.register(Hyperlocal_slider_info)
admin.site.register(Hyperlocal_image_slider)
admin.site.register(Hyperlocal_review)
admin.site.register(Hyperlocal_review_card)
admin.site.register(Hyperlocal_testimonials)
admin.site.register(Hyperlocal_company_info)
admin.site.register(Hyperlocal_company_logo)
admin.site.register(Hyperlocal_Suggetion)
admin.site.register(Hyperlocal_faq_info)
admin.site.register(Hyperlocal_faq)
admin.site.register(Hyperlocal_end)



# Register your models here.
admin.site.register(Bulk_service)
admin.site.register(Bulk_service_info)
admin.site.register(Bulk_card_info)
admin.site.register(Bulk_card_data)
admin.site.register(Bulk_info)
admin.site.register(Bulk_info1)
admin.site.register(Bulk_card_information)
admin.site.register(Bulk_card)
admin.site.register(Bulk_slider)
admin.site.register(Bulk_company_slider)
admin.site.register(Bulk_review)
admin.site.register(Bulk_review_card)
admin.site.register(Bulk_testimonials)
admin.site.register(Bulk_company_info)
admin.site.register(Bulk_company_logo)
admin.site.register(Bulk_Suggetion_info)
admin.site.register(Bulk_Suggetion)
admin.site.register(Bulk_end)



admin.site.register(Sprint_service)
admin.site.register(Sprint_card_info)
admin.site.register(Sprint_card)
admin.site.register(Sprint_info)
admin.site.register(Sprint_information)
admin.site.register(Sprint_install_info)
admin.site.register(Sprint_slider_info)
admin.site.register(Sprint_company_slider)
admin.site.register(Sprint_review)
admin.site.register(Sprint_review_card)
admin.site.register(Sprint_testimonials)
admin.site.register(Sprint_company_info)
admin.site.register(Sprint_company_logo)
admin.site.register(Sprint_Suggetion_info)
admin.site.register(Sprint_Suggetion)
admin.site.register(Sprint_faq_info)
admin.site.register(Sprint_faq)
admin.site.register(Sprint_end)









