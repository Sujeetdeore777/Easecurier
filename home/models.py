from django.db import models
from colorfield.fields import ColorField

# index page model start
class Mainheader(models.Model):
    heading = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    buttontext = models.CharField(max_length=50)
    buttoncolour = models.CharField(max_length=10)
    def __str__(self):
        return self.heading
    
class Mainimg(models.Model):
   mainimg = models.ImageField(upload_to="myimage")
   smallimg = models.ImageField(upload_to="myimage")
   
class Subimg(models.Model):
   subimg = models.ImageField(upload_to="myimage")
   
class Buisness(models.Model):
    smallheading = models.CharField(max_length=2000)
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading
    
class Buisnessdetails(models.Model):
    img = models.ImageField(upload_to="myimage")
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading
    
class Plan(models.Model):
    img = models.ImageField(upload_to="myimage")
    heading = models.CharField(max_length=2000)
    buttontext = models.CharField(max_length=1000)
    def __str__(self):
        return self.heading
    
class Whychooesus(models.Model):
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=5000)
    def __str__(self):
        return self.heading

class Slideimg_rightdescription_active(models.Model):
    img = models.ImageField(upload_to="myimage")
    heading1 = models.CharField(max_length=2000)
    description1 = models.CharField(max_length=1000)
    heading2 = models.CharField(max_length=2000)
    description2 = models.CharField(max_length=1000)
    heading3 = models.CharField(max_length=2000)
    description3 = models.CharField(max_length=1000)
    heading4 = models.CharField(max_length=2000)
    description4 = models.CharField(max_length=1000)
    def __str__(self):
        return self.heading1
    
class Slideimg_rightdescription(models.Model):
    img = models.ImageField(upload_to="myimage")
    heading1 = models.CharField(max_length=2000)
    description1 = models.CharField(max_length=1000)
    heading2 = models.CharField(max_length=2000)
    description2 = models.CharField(max_length=1000)
    heading3 = models.CharField(max_length=2000)
    description3 = models.CharField(max_length=1000)
    heading4 = models.CharField(max_length=2000)
    description4 = models.CharField(max_length=1000)
    def __str__(self):
        return self.heading1
    
class Cartheading(models.Model):
    heading = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading
    
class Cart(models.Model):
    img = models.ImageField(upload_to="myimage")
    heading1 = models.CharField(max_length=2000)
    description1 = models.CharField(max_length=1000)
    buttontext = models.CharField(max_length=2000)
    buttonlink = models.CharField(max_length=2000)

    
    def __str__(self):
        return self.heading1
    
class Slidercart(models.Model):
    heading = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading
    
class Slidermaincart(models.Model):
    img = models.ImageField(upload_to="myimage")
    description = models.CharField(max_length=2000)
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    
class Slidermaincart2(models.Model):
    img = models.ImageField(upload_to="myimage")
    description = models.CharField(max_length=2000)
    
class Brandtext(models.Model):
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.heading
    
class Brandimg(models.Model):
    img = models.ImageField(upload_to="myimage")
    
class Brandimg2(models.Model):
    img = models.ImageField(upload_to="myimage")
    
class Suggested(models.Model):
    img = models.ImageField(upload_to="myimage")
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=1000)
    buttonname = models.CharField(max_length=1000)
    buttonurl = models.CharField(max_length=1000)
    def __str__(self):
        return self.heading
    
class Suggestedheading(models.Model):
    heading = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading
    
class Newsheading(models.Model):
    heading = models.CharField(max_length=2000)
    buttontext = models.CharField(max_length=2000)
    buttonurl = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading
    
class Newsimg(models.Model):
    img = models.ImageField(upload_to="myimage")


    
    # index page model end
    
    
      
    # features page model start
    
class featureheading(models.Model):
    heading = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading   
    
class Featurecard(models.Model):
    img = models.ImageField(upload_to="myimage")
    heading = models.CharField(max_length=2000)
    shortdescription = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.heading
 
class featureheading2(models.Model):
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=5000)
    def __str__(self):
        return self.heading   
    
class Featurecard2(models.Model):
    img = models.ImageField(upload_to="myimage")
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=5000)
    def __str__(self):
        return self.heading
       
    
    
    
    
     # features page model end
     
     
     
     # prising page model start
     
class Prisingheading(models.Model):
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=5000)
    def __str__(self):
        return self.heading    
    
    
    
    
class Prisingcart(models.Model):
    heading1 = models.CharField(max_length=2000)
    heading2 = models.CharField(max_length=2000)
    paragraph = models.CharField(max_length=2000)
    buttontext = models.CharField(max_length=2000)
    buttonlink = models.CharField(max_length=2000)
    featiurenameheading = models.CharField(max_length=2000)
    features1 = models.CharField(max_length=2000)
    features2 = models.CharField(max_length=2000)
    features3 = models.CharField(max_length=2000)
    features4 = models.CharField(max_length=2000, null=True, blank=True )
    features5 = models.CharField(max_length=2000, null=True, blank=True)
    features6 = models.CharField(max_length=2000, null=True, blank=True)
    features7 = models.CharField(max_length=2000, null=True, blank=True)
    features8 = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.heading1  
    
    
class Prisingcart2heading(models.Model):
    heading1 = models.CharField(max_length=2000)

    def __str__(self):
        return self.heading1 
    
class Prisingcart2(models.Model):
    heading1 = models.CharField(max_length=2000)
    heading2 = models.CharField(max_length=2000, null=True, blank=True )
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.heading1 
    
class Faqheading(models.Model):
    heading = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading
    
class Faq(models.Model):
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.heading 
    
    
class Last(models.Model):
    heading = models.CharField(max_length=2000)
    buttontext = models.CharField(max_length=2000)
    backgroundcolour = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading 
    
     
        # prising page model end
        
           # Aboutus page model start
           
class Aboutusstart(models.Model):
    heading1 = models.CharField(max_length=2000)
    heading2 = models.CharField(max_length=2000)
    img = models.ImageField(upload_to="myimage")
    heading3 = models.CharField(max_length=2000)
    description = models.CharField(max_length=5000)
    lastmassage = models.CharField(max_length=5000)
    def __str__(self):
        return self.heading1    
    
    
class Counterheading(models.Model):
    heading1 = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading1   
    
class Counter(models.Model):
    counternumber = models.CharField(max_length=2000)
    countertext = models.CharField(max_length=2000)
    def __str__(self):
        return self.countertext      
    
class Trustedbuisness_heading(models.Model):
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading
    
class Trustedbuisness_img(models.Model):
    img = models.ImageField(upload_to="myimage")

class News_section(models.Model):
    heading = models.CharField(max_length=2000)
    buttontext = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading
    
class Newssection_img(models.Model):
    img = models.ImageField(upload_to="myimage")
    
class Ourteam_section(models.Model):
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    buttontext = models.CharField(max_length=2000)
    buttonlink = models.CharField(max_length=2000)
    def __str__(self):
        return self.heading
    
class Team_member(models.Model):
    name = models.CharField(max_length=2000)
    position = models.CharField(max_length=2000)
    img = models.ImageField(upload_to="myimage")
    facebooklink = models.CharField(max_length=2000)
    twiterlink = models.CharField(max_length=2000)
    linkesinlink = models.CharField(max_length=2000)
    instagramlink = models.CharField(max_length=2000)
    def __str__(self):
        return self.name
           
           
           
              # Aboutus page model end
              
              
              
                # track order page model start
class Track_order(models.Model):
    heading = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    logo = models.ImageField(upload_to="myimage")
    serchtitle = models.CharField(max_length=2000)
    wavesimg = models.ImageField(upload_to="myimage")
    
    def __str__(self):
        return self.heading               
                
                
                
                
                    # track order page model end
                    
         # jyoti mam models  start            
         
     # -------------------section first---------------------------

class Hyperlocal_service(models.Model):
  title=models.CharField(max_length=500)
  description= models.TextField(max_length=5000,blank=True,null=True)
  def _str_(self):
        return self.title   


 # -------------------section second---------------------------
class Hyperlocal_card_info(models.Model):
 title=models.CharField(max_length=500)
    

class Hyperlocal_card(models.Model):
  card_img = models.ImageField(upload_to="myimage")
  card_title=models.CharField(max_length=500)
  card_description= models.TextField(max_length=5000,blank=True,null=True)

  # -------------------section third---------------------------
class Hyperlocal_info(models.Model):
   title=models.CharField(max_length=500)
   card_image =models.ImageField(upload_to="myimage")
   sub_title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)

    # -------------------section fourth---------------------------
class Hyperlocal_company_info(models.Model):
    title=models.CharField(max_length=500)
 
class Hyperlocal_comapny_images(models.Model):
   image =models.ImageField(upload_to="myimage")


  # -------------------section five---------------------------
class Hyperlocal_places(models.Model):
    title=models.CharField(max_length=500)
 
class Hyperlocal_company_images(models.Model):
   image =models.ImageField(upload_to="myimage")
   image_name=models.CharField(max_length=500)

    # -------------------section six---------------------------
class Hyperlocal_slider_info(models.Model):
    title=models.CharField(max_length=500)
 
class Hyperlocal_image_slider(models.Model):
   image =models.ImageField(upload_to="myimage")


    # -------------------section seven---------------------------

class Hyperlocal_review(models.Model):
     title=models.CharField(max_length=500)
 
class Hyperlocal_review_card(models.Model):
   card_image =models.ImageField(upload_to="myimage")
   card_title=models.CharField(max_length=500)
   card_description= models.TextField(max_length=5000,blank=True,null=True)


    # -------------------section Eight---------------------------
class Hyperlocal_testimonials(models.Model):
   image =models.ImageField(upload_to="myimage")
   description= models.TextField(max_length=5000,blank=True,null=True)

    # -------------------section nine---------------------------
class Hyperlocal_company_info1(models.Model):
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)

class Hyperlocal_company_logo(models.Model):
   image =models.ImageField(upload_to="myimage")


   
    # -------------------section ten---------------------------
class Hyperlocal_Suggetion(models.Model):
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)
   image =models.ImageField(upload_to="myimage")

    # -------------------section eleven---------------------------
class Hyperlocal_faq_info(models.Model):
    title=models.CharField(max_length=500)
    
class Hyperlocal_faq(models.Model):
    title=models.CharField(max_length=500)
    description= models.TextField(max_length=5000,blank=True,null=True)


     # -------------------section twelve---------------------------
class Hyperlocal_end(models.Model):
    title=models.CharField(max_length=500)
    
    



# ------------------------ Bulk-------------------------------
     # -------------------section first---------------------------

class Bulk_service(models.Model):
  title=models.CharField(max_length=500)
  description= models.TextField(max_length=5000,blank=True,null=True)
  button_text=models.CharField(max_length=500)
  button_url=models.CharField(max_length=500)
  image =models.ImageField(upload_to="myimage")
  def _str_(self):
        return self.title   


class Bulk_service_info(models.Model):
  title=models.CharField(max_length=500)
  description= models.TextField(max_length=5000,blank=True,null=True)
  button_text=models.CharField(max_length=500)
  button_url=models.CharField(max_length=500)
  def _str_(self):
        return self.title  
 # -------------------section second---------------------------
class Bulk_card_info(models.Model):
 title=models.CharField(max_length=500)
 description= models.TextField(max_length=5000,blank=True,null=True)
 
 
class Bulk_card_data(models.Model):
 title=models.CharField(max_length=500)
 image =models.ImageField(upload_to="myimage")
 
class Bulk_info(models.Model):
   title=models.CharField(max_length=500)
   card_image =models.ImageField(upload_to="myimage")
   
class Bulk_info1(models.Model):  
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)

 
  # -------------------section third---------------------------
class Bulk_card_information(models.Model):
  title=models.CharField(max_length=500)    
  description= models.TextField(max_length=5000,blank=True,null=True)

class Bulk_card(models.Model):
  card_image =models.ImageField(upload_to="myimage")
  card_title=models.CharField(max_length=500)
  card_description= models.TextField(max_length=5000,blank=True,null=True)

    # -------------------section fourth---------------------------
class Bulk_slider(models.Model):
    title=models.CharField(max_length=500)
 
class Bulk_company_slider(models.Model):
   image_slider =models.ImageField(upload_to="myimage")
   


# -------------------bulk five---------------------------
class Bulk_review(models.Model):
     title=models.CharField(max_length=500)
 
class Bulk_review_card(models.Model):
   card_image =models.ImageField(upload_to="myimage")
   card_title=models.CharField(max_length=500)
   card_description= models.TextField(max_length=5000,blank=True,null=True)


    # -------------------section Eight---------------------------
class Bulk_testimonials(models.Model):
   image =models.ImageField(upload_to="myimage")
   description= models.TextField(max_length=5000,blank=True,null=True)

    # -------------------section nine---------------------------
class Bulk_company_info(models.Model):
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)

class Bulk_company_logo(models.Model):
   image =models.ImageField(upload_to="myimage")


   
    # -------------------section ten---------------------------
class Bulk_Suggetion_info(models.Model):
   title=models.CharField(max_length=500)
   button_text=models.CharField(max_length=500)
   button_url=models.CharField(max_length=500)
    
class Bulk_Suggetion(models.Model):
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)
   image =models.ImageField(upload_to="myimage")

   
     # -------------------section eleven---------------------------
class Bulk_end(models.Model):
    title=models.CharField(max_length=500)
    button_text=models.CharField(max_length=500)
    button_url=models.CharField(max_length=500)
         
         
         
         
         

# ------------------------ Sprint-------------------------------
     # -------------------section first---------------------------
class Sprint_service(models.Model):
  image =models.ImageField(upload_to="myimage")
  title=models.CharField(max_length=500)
  description= models.TextField(max_length=5000,blank=True,null=True)
  button_text=models.CharField(max_length=500)
  button_url=models.CharField(max_length=500)
  def __str__(self):
        return self.title   


 # -------------------section second---------------------------
class Sprint_card_info(models.Model):
  title=models.CharField(max_length=500)
    

class Sprint_card(models.Model):
  card_image =models.ImageField(upload_to="myimage")
  card_title=models.CharField(max_length=500)
  

  # -------------------section third---------------------------
class Sprint_info(models.Model):
   title=models.CharField(max_length=500)
   image =models.ImageField(upload_to="myimage")
   
class Sprint_install_info(models.Model):  
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)

    # -------------------section fourth---------------------------
class Sprint_information(models.Model): 
    title=models.CharField(max_length=500)
    button_text=models.CharField(max_length=500)
    button_url=models.CharField(max_length=500)
    button_color=models.CharField(max_length=500)

    # -------------------section five---------------------------
class Sprint_slider_info(models.Model):
    title=models.CharField(max_length=500)
 
class Sprint_company_slider(models.Model):
   image =models.ImageField(upload_to="myimage")

    # -------------------section seven---------------------------

class Sprint_review(models.Model):
     title=models.CharField(max_length=500)
 
class Sprint_review_card(models.Model):
   card_image =models.ImageField(upload_to="myimage")
   card_title=models.CharField(max_length=500)
   card_description= models.TextField(max_length=5000,blank=True,null=True)


    # -------------------section Eight---------------------------
class Sprint_testimonials(models.Model):
   image =models.ImageField(upload_to="myimage")
   description= models.TextField(max_length=5000,blank=True,null=True)

    # -------------------section nine---------------------------
class Sprint_company_info(models.Model):
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)

class Sprint_company_logo(models.Model):
   image =models.ImageField(upload_to="myimage")


   
    # -------------------section ten---------------------------
class Sprint_Suggetion_info(models.Model):
   title=models.CharField(max_length=500)
   button_text=models.CharField(max_length=500)
   button_url=models.CharField(max_length=500)
   button_color=models.CharField(max_length=500)
    
class Sprint_Suggetion(models.Model):
   image =models.ImageField(upload_to="myimage")
   title=models.CharField(max_length=500)
   sub_title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)
   button_url=models.CharField(max_length=500)

    # -------------------section eleven---------------------------
class Sprint_faq_info(models.Model):
    title=models.CharField(max_length=500)
    
class Sprint_faq(models.Model):
    title=models.CharField(max_length=500)
    description= models.TextField(max_length=5000,blank=True,null=True)


     # -------------------section twelve---------------------------
class Sprint_end(models.Model):
    title=models.CharField(max_length=500)
    button_text=models.CharField(max_length=500)
    button_url=models.CharField(max_length=500)
   
    #faq model
# ===================section first===================
class Faq_page(models.Model):
    title=models.CharField(max_length=500)
    title1=models.CharField(max_length=500)
    title2=models.CharField(max_length=500)
    
       
class Faq_info_card(models.Model):
    title=models.CharField(max_length=500)
    description= models.TextField(max_length=500,blank=True,null=True)
    
    
class Faq_section_card(models.Model):
    title=models.CharField(max_length=500)
    description= models.TextField(max_length=500,blank=True,null=True)
    
class Faq_card(models.Model):
    title=models.CharField(max_length=500)
    description= models.TextField(max_length=500,blank=True,null=True)
         
         # jyoti mam models  end          
  
class Glosary(models.Model):   
    title=models.CharField(max_length=500)
    description= models.TextField(max_length=500,blank=True,null=True)          
    
 # ================media feature=====================
    
        # -------------------section eleven---------------------------
class Media_feature(models.Model):
    image =models.ImageField(upload_to="myimage")
    title=models.CharField(max_length=500)

    
class Media_feature_card(models.Model):
    image =models.ImageField(upload_to="myimage")
    description= models.TextField(max_length=500,blank=True,null=True)
    button_url=models.CharField(max_length=500)
    button_text=models.CharField(max_length=500)


     # -------------------section twelve---------------------------
class Media_card_info(models.Model):
    title=models.CharField(max_length=500)
    
class Media_card(models.Model):
    image =models.ImageField(upload_to="myimage")
    title=models.CharField(max_length=500)
    description= models.TextField(max_length=500,blank=True,null=True)
    button_url=models.CharField(max_length=500)
    button_text=models.CharField(max_length=500)
    

# --------------singlepage-------------
    
    
    
class Single(models.Model):   
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500,blank=True,null=True)
    sub_title = models.CharField(max_length=500)
    image =models.ImageField(upload_to="myimage")
    sub_description = models.TextField(max_length=500,blank=True,null=True)
    
class Single_card_info(models.Model):   
    title = models.CharField(max_length=500)
    
class Single_card(models.Model):   
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500,blank=True,null=True)
    
class Single_info(models.Model):   
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500,blank=True,null=True)
    
class Single_icon(models.Model):
    icon_class= models.CharField(max_length=500)
    icon_url= models.CharField(max_length=500)
    
    

    
class Double(models.Model):   
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500,blank=True,null=True)
    sub_title = models.CharField(max_length=500)
    image =models.ImageField(upload_to="myimage")
    sub_description = models.TextField(max_length=500,blank=True,null=True)
    
class Double_card_info(models.Model):   
    title = models.CharField(max_length=500)
    
class Double_card(models.Model):   
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500,blank=True,null=True)
    
class Double_info(models.Model):   
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500,blank=True,null=True)
    
class Double_icon(models.Model):
    icon_class= models.CharField(max_length=500)
    icon_url= models.CharField(max_length=500)
    
    
    
   

class Triple(models.Model):   
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500,blank=True,null=True)
    sub_title = models.CharField(max_length=500)
    image =models.ImageField(upload_to="myimage")
    sub_description = models.TextField(max_length=500,blank=True,null=True)
    
class Triple_card_info(models.Model):   
    title = models.CharField(max_length=500)
    
class Triple_card(models.Model):   
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500,blank=True,null=True)
    
class Triple_info(models.Model):   
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500,blank=True,null=True)
    
class Triple_icon(models.Model):
    icon_class= models.CharField(max_length=500)
    icon_url= models.CharField(max_length=500)
    



 # ------------------------ international-------------------------------
     # -------------------section first---------------------------

class International_service1(models.Model):
  title=models.CharField(max_length=500)
  description= models.TextField(max_length=5000,blank=True,null=True)
  button_text=models.CharField(max_length=500)
  button_url=models.CharField(max_length=500)
  image =models.ImageField(upload_to="myimage")
  def _str_(self):
        return self.title   


 # -------------------section second---------------------------
class International_card_info(models.Model):
  title=models.CharField(max_length=500)
    

class International_card(models.Model):
  card_image =models.ImageField(upload_to="myimage")
  card_title=models.CharField(max_length=500)
  card_description= models.TextField(max_length=5000,blank=True,null=True)

  # -------------------section third---------------------------
class International_info(models.Model):
   title=models.CharField(max_length=500)
   card_image =models.ImageField(upload_to="myimage")
   
class International_infocard(models.Model):  
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)

    # -------------------section fourth---------------------------
class International_places(models.Model):
    title=models.CharField(max_length=500)
 
class International_feature_images(models.Model):
   image =models.ImageField(upload_to="myimage")
   image_name=models.CharField(max_length=500)



    # -------------------section five---------------------------
class International_slider_info(models.Model):
    title=models.CharField(max_length=500)
 
class International_company_slider(models.Model):
   image =models.ImageField(upload_to="myimage")


    # -------------------section seven---------------------------

class International_review(models.Model):
     title=models.CharField(max_length=500)
 
class International_review_card(models.Model):
   card_image =models.ImageField(upload_to="myimage")
   card_title=models.CharField(max_length=500)
   card_description= models.TextField(max_length=5000,blank=True,null=True)


    # -------------------section Eight---------------------------
class International_testimonials(models.Model):
   image =models.ImageField(upload_to="myimage")
   description= models.TextField(max_length=5000,blank=True,null=True)

    # -------------------section nine---------------------------
class International_company_info(models.Model):
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)

class International_company_logo(models.Model):
   image =models.ImageField(upload_to="myimage")


   
    # -------------------section ten---------------------------
class International_Suggetion_info(models.Model):
   title=models.CharField(max_length=500)
   buttontext=models.CharField(max_length=500)
   buttonurl=models.CharField(max_length=500)
    
class International_Suggetion(models.Model):
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)
   image =models.ImageField(upload_to="myimage")

    # -------------------section eleven---------------------------
class International_faq_info(models.Model):
    title=models.CharField(max_length=500)
    
class International_faq(models.Model):
    title=models.CharField(max_length=500)
    description= models.TextField(max_length=5000,blank=True,null=True)


     # -------------------section twelve---------------------------
class International_end(models.Model):
    title=models.CharField(max_length=500)
    buttontext=models.CharField(max_length=500)
    buttonurl=models.CharField(max_length=500)
    
    
    
    
    
    
# ------------------------ ecommerce-------------------------------
     # -------------------section first---------------------------

class Ecommerce_service(models.Model):
  title=models.CharField(max_length=500)
  description= models.TextField(max_length=5000,blank=True,null=True)
  button_text=models.CharField(max_length=500)
  button_url=models.CharField(max_length=500)
  image =models.ImageField(upload_to="myimage")
  def _str_(self):
        return self.title   
    
    
class Ecommerce_serviceneww(models.Model):
  title=models.CharField(max_length=500)
  description= models.TextField(max_length=5000,blank=True,null=True)
  button_text=models.CharField(max_length=500)
  button_url=models.CharField(max_length=500)
  image =models.ImageField(upload_to="myimage")
  def _str_(self):
        return self.title  


 # -------------------section second---------------------------
class Ecommerce_card_info(models.Model):
 title=models.CharField(max_length=500)
 image =models.ImageField(upload_to="myimage")
 
class Ecommerce_info(models.Model):
  title=models.CharField(max_length=500)
  card_image =models.ImageField(upload_to="myimage")
  
class Ecommerce_info1(models.Model):
  title=models.CharField(max_length=500)
  description= models.TextField(max_length=5000,blank=True,null=True)

 
  # -------------------section third---------------------------
class Ecommerce_card_information(models.Model):
  title=models.CharField(max_length=500)    

class Ecommerce_card(models.Model):
  card_image =models.ImageField(upload_to="myimage")
  card_title=models.CharField(max_length=500)
  card_description= models.TextField(max_length=5000,blank=True,null=True)

    # -------------------section fourth---------------------------
class Ecommerce_slider(models.Model):
    title=models.CharField(max_length=500)
 
class Ecommerce_company_slider(models.Model):
   image_slider =models.ImageField(upload_to="myimage")
   


# -------------------section five---------------------------
class Ecommerce_review(models.Model):
    title=models.CharField(max_length=500)
 
class Ecommerce_review_card(models.Model):
   card_image =models.ImageField(upload_to="myimage")
   card_title=models.CharField(max_length=500)
   card_description= models.TextField(max_length=5000,blank=True,null=True)


    # -------------------section Eight---------------------------
class Ecommerce_testimonials(models.Model):
   image =models.ImageField(upload_to="myimage")
   description= models.TextField(max_length=5000,blank=True,null=True)

    # -------------------section nine---------------------------
class Ecommerce_company_info(models.Model):
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)

class Ecommerce_company_logo(models.Model):
   image =models.ImageField(upload_to="myimage")


   
    # -------------------section ten---------------------------
class Ecommerce_Suggetion_info(models.Model):
   title=models.CharField(max_length=500)
   button_text=models.CharField(max_length=500)
   button_url=models.CharField(max_length=500)
    
class Ecommerce_Suggetion(models.Model):
   title=models.CharField(max_length=500)
   description= models.TextField(max_length=5000,blank=True,null=True)
   image =models.ImageField(upload_to="myimage")

    # -------------------section eleven---------------------------
class Ecommerce_faq_info(models.Model):
    title=models.CharField(max_length=500)
    
class Ecommerce_faq(models.Model):
    title=models.CharField(max_length=500)
    description= models.TextField(max_length=5000,blank=True,null=True)


     # -------------------section twelve---------------------------
class Ecommerce_end(models.Model):
    title=models.CharField(max_length=500)
    button_text=models.CharField(max_length=500)
    button_url=models.CharField(max_length=500)
    
    
    

     # -------------------sregister page---------------------------
class Registerfirst(models.Model):
    heading=models.CharField(max_length=500)
    paragraph1=models.CharField(max_length=500)
    paragraph2=models.CharField(max_length=500)
    image =models.ImageField(upload_to="myimage")
    
class Logisticheading(models.Model):
    heading=models.CharField(max_length=500)
    
class Logisticdetails(models.Model):
    heading=models.CharField(max_length=500)
    paragraph1=models.CharField(max_length=500)
    image =models.ImageField(upload_to="myimage")
    
    
class Partnersdetails(models.Model):
    heading=models.CharField(max_length=500)
    paragraph1=models.CharField(max_length=500)
    image =models.ImageField(upload_to="myimage")
    
    
class Features(models.Model):
    heading=models.CharField(max_length=500)
    image =models.ImageField(upload_to="myimage")
    
class Trusted(models.Model):
    heading=models.CharField(max_length=500)
    
    
class Trustedcards(models.Model):
    heading1=models.CharField(max_length=500)
    heading2=models.CharField(max_length=500)
    paragraph1=models.CharField(max_length=5000)
    image =models.ImageField(upload_to="myimage")
  
   


    
    
