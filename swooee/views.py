from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from datetime import datetime
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.contrib.auth.hashers  import make_password,check_password


date1 = datetime.now()

# Create your views here.

# SCRAP FILE HERE





# INDEX PAGE :
def home(request):
    if 'id' in request.session:
        disc =  {
            'title':'Corona Admin',
        }
        return render(request, 'swooee/index.html',disc)
    else:
        return redirect("login")
    
# LOGIN FORM :
def login(request):
    if 'id' in request.session:
        return redirect('home')
    else:
        disc =  {
            'title':'Corona Admin | Login',
            'url' : "/login_admin/"
        }
        return render(request, 'swooee/login.html',disc)

# ADD USER FORM :
def adduserpage(request):
    if 'id' in request.session:
        disc =  {
            'title':'Corona Admin | Add User Form',
        }
        return render(request, 'swooee/form_user.html',disc)
    else:
        return redirect("login")

# ADD CATEGORY FORM :
def categorypage(request):
    if 'id' in request.session:
        cats = Categories.objects.all()
        disc =  {
            'title':'Corona Admin | Add Category Forms',
            'cat' : cats,
        }
        return render(request, 'swooee/form_category.html',disc)
    else:
        return redirect("login")

# ALL PRODUCT PAGE SHOW :
def all_products(request):
    if 'id' in request.session:
        pro = product.objects.all()
        disc =  {
            'title':'Corona Admin | All Products',
            'pro':pro
        }
        return render(request, 'swooee/all_product.html',disc)
    else:
        return redirect("login")

# ADD PRODUCT FORM :
def productpage(request):
    if 'id' in request.session:
        cat = Categories.objects.filter(status=0)
        disc =  {
            'title':'Corona Admin | Add Product Form',
            'cat':cat,
        }
        return render(request, 'swooee/form_product.html',disc)
    else:
        return redirect('login')

# ADMIN LOGIN FUCTION :
def login_admin(request):
    try:
        if request.method == "POST":
            ur = request.POST['email']
            pwd = request.POST['pswd']

            user = admin_user.objects.filter(username=ur)
            if len(user) > 0:
                if user[0].password == pwd:
                    request.session['id']= user[0].id
                    return redirect("home")
                else:
                    msg = "Password is Incorrect..!"
                    return render(request, "swooee/login.html",{'err':msg,'em':ur})

            else:
                msg = "User Doesn't Found"
                return render(request, "swooee/login.html",{'err':msg,'em':ur})
        else:
            msg = "Somthing Wrong"
            return render(request, "swooee/login.html",{'err':msg,'em':ur})
    except:
        return redirect("login")
    
# ADMIN LOGOUT :
def logout_admin(request):
    if 'id' in request.session:
        del request.session['id']
        return redirect("login")
    else:
        return redirect("login")
        
# ADD CATEGORY FUNNCTION :
def add_category(request):
    if 'id' in request.session:      
        name = request.POST['cname']
        cimg = request.FILES['cimg[]']
        try:
            cate = request.POST['ccat']
            cat = Categories.objects.get(category=cate)
                
        except:
            pass
        try:
            cate = Categories.objects.create(category=name,created_at=date1,parent=cat,updated_at=date1,Image=cimg)
        except:
            cate = Categories.objects.create(category=name,created_at=date1,updated_at=date1,Image=cimg)
        return redirect("allCat")
    else:
        return redirect("login")

# ADD PRODUCT FUNCTION :
def add_product(request):
    if 'id' in request.session:
        # Product Details
        product_name = request.POST['pname']
        product_dis = request.POST['pdiscription']
        product_cat = request.POST['pcat']
        product_img = request.FILES['img[]']
        # Amzon Links
        product_url = request.POST['paurl'] if request.POST['paurl'] else 'None'
        product_min = request.POST['pamin'] if request.POST['pamin'] else 'None'
        product_max = request.POST['pamax'] if request.POST['pamax'] else 'None'
        # Awin Links
        product_aurl = request.POST['pawurl'] if request.POST['pawurl'] else 'None'
        product_amin = request.POST['pawmin'] if request.POST['pawmin'] else 'None'
        product_amax = request.POST['pawmax'] if request.POST['pawmax'] else 'None'
        # Ebay Links
        product_eurl = request.POST['peurl'] if request.POST['peurl'] else 'None'
        product_emin = request.POST['pemin'] if request.POST['pemin'] else 'None'
        product_emax = request.POST['pemax'] if request.POST['pemax'] else 'None'
        # Walmart Links
        product_wurl = request.POST['pwurl'] if request.POST['pwurl'] else 'None'
        product_wmin = request.POST['pwmin'] if request.POST['pwmin'] else 'None'
        product_wmax = request.POST['pwmax'] if request.POST['pwmax'] else 'None'
        # Youtube Links
        product_youtube = request.POST['pyoutube'] if request.POST['pyoutube'] else 'None'
                
        categor = Categories.objects.get(category=product_cat)
        produ = product.objects.create(
            name = product_name,
            slug = product_name,
            discription = product_dis,
            category = categor,
            Image = product_img,
            created_at=date1,
            updated_at=date1,
        # )
        # pr = product.objects.filter(name=product_name)[0]
        # links = egg_pr.objects.create(
        #     product_id = pr,
            amazon = product_url,
            amazon_sell_price =  product_min,
            amazon_MRP = product_max,
            awin = product_aurl,
            awin_sell_price = product_amin,
            awin_MRP = product_amax,
            ebay = product_eurl,
            ebay_sell_price = product_emin,
            ebay_MRP = product_emax,
            walmart = product_wurl,
            walmart_sell_price = product_wmin,
            walmart_MRP = product_wmax,
            youtube = product_youtube,
        )
        return redirect('allProduct')
    else:
        return redirect('login')

# ALL USER PAGE SHOW :  
def all_user(request):
    if 'id' in request.session:
        getusr = user.objects.all()
        disc =  {
            'title':'Corona Admin | All User Page',
            'usr':getusr,
        }
        return render(request,'swooee/all_user.html',disc)
    else:
        return redirect('login')

# ALL CATEGORY PAGE SHOW :  
def all_cat(request):
    if 'id' in request.session:
        getcat = Categories.objects.all()
        disc =  {
            'title':'Corona Admin | All Category Page',
            'cat':getcat,
        }
        return render(request,'swooee/all_category.html',disc)
    else:
        return redirect('login')
    
# EDIT CATEGORY PAGE SHOW :
def edit_cat_page(request,slug):
    if 'id' in request.session:
        getcat = Categories.objects.get(slug=slug)
        cats = Categories.objects.all()
        disc =  {
            'title': getcat.category ,
            'cat':getcat,
            'parent' : getcat.parent,
            'cats' : cats,
        }
        return render(request,'swooee/edit_category.html',disc)
    else:
        return redirect('login')
    
# EDIT PRODUCT PAGE SHOW :
def edit_product_page(request,slug):
    if 'id' in request.session:
        getpro = product.objects.get(slug=slug)
        cat = Categories.objects.filter(status=0)
        disc =  {
            'title': getpro.name,
            'getpro':getpro,
            'cat' : cat
        }
        return render(request,'swooee/edit_product.html',disc)
    else:
        return redirect('login')
    
# EDIT PRODUCT FUNCTION :
def edit_product(request,slug):
    if  'id' in request.session:
        productdata = product.objects.get(slug=slug)
        
        productdata.name = request.POST['pname'] if request.POST['pname'] else productdata.name
        productdata.slug = request.POST['pname'] if request.POST['pname'] else productdata.slug
        productdata.discription = request.POST['pdiscription'] if request.POST['pdiscription'] else productdata.discription
        productdata.updated_at = date1
        productdata.status = request.POST['radiobtn'] if request.POST['radiobtn'] else productdata.status
        try:
            productdata.Image = request.FILES['img']
        except :
            productdata.Image = productdata.Image
        categ = request.POST['pcat']
        cat = Categories.objects.get(category=categ)
        productdata.category = cat if cat else productdata.category
        productdata.save()
        return redirect('allProduct')
    else:
        return redirect('login')
    
# EDIT CATEGORY FUNCTION :
def edit_category(request,slug):
    if  'id' in request.session:
        catdata = Categories.objects.get(slug=slug)
        catdata.category = request.POST['cname'] if request.POST['cname'] else catdata.category
        catdata.slug = request.POST['cname'] if request.POST['cname'] else catdata.slug
        catdata.updated_at = date1
        try:
            categ = request.POST['ccat']
            if categ == 'NULL':
                catdata.parent = None
            else:
                cat = Categories.objects.get(category=categ)
            
                if catdata.category == categ:
                    catdata.parent = catdata.parent
                else:
                    catdata.parent = cat if cat else catdata.parent
        except:
            catdata.parent = catdata.parent
        
        catdata.status = request.POST['radiobtn'] if request.POST['radiobtn'] else catdata.status
        try:
            catdata.Image = request.FILES['name']
        except :
            catdata.Image = catdata.Image
        catdata.save()
        return redirect('allCat')
    else:
        return redirect('login')
    
# DELETE CATEGORY FUNNCTION :
# Ajax Using CODE.
def delete_cat(request):
    if request.method=='POST':
        id = request.POST.get('pid')
        print(id)
        getpas = Categories.objects.get(pk=id)
        getpas.delete()
        return JsonResponse({'status':1})
        # return redirect("Home")
    else:
        return JsonResponse({'status':0})
    
# DELETE PRODUCT FUNNCTION :
# Ajax Using CODE.
def delete_product(request):
    if request.method=='POST':
        id = request.POST.get('pid')
        print(id)
        getpas = product.objects.get(pk=id)
        getpas.delete()
        return JsonResponse({'status':1})
        # return redirect("Home")
    else:
        return JsonResponse({'status':0})
    
# STATIC EXTRA PAGES SHOW CONTAIN :
def staticpage(request):
    if  'id' in request.session:
        disc =  {
                'title':'Corona Admin | Add Dyanmic Page',
            }
        return render(request, 'swooee/form_static_page.html',disc)
    else:
        return redirect('login')

# STATIC PAGE CONTAIN :
def add_static_page(request):
    if  'id' in request.session:
        title = request.POST['pname']
        Image = request.FILES['pimg[]']
        
        discri = request.POST['pdis']
        
        page = render_to_string('head_foot/New.html', {
                            'title1': title,
                            'page': discri,
                        })
        
        sta = static_page.objects.create(title = title, discription = discri, created_at=date1, page=page, updated_at=date1, Image = Image)
        return redirect('allstaticpage')
    else:
        return redirect('login')

# View ALL STATIC PAGES :
def view_static_page(request):
    if  'id' in request.session:
        page = static_page.objects.all()
        disc =  {
                'title':'Corona Admin | Show All Dynamic Page',
                'page':page,
            }
        return render(request, 'swooee/all_static_page.html',disc)
    else:
        return redirect('login')
    
# DELETE PRODUCT FUNNCTION :
# Ajax Using CODE.
def delete_page(request):
    if request.method=='POST':
        id = request.POST.get('pid')
        print(id)
        getpas = static_page.objects.get(pk=id)
        getpas.delete()
        return JsonResponse({'status':1})
        # return redirect("Home")
    else:
        return JsonResponse({'status':0})

# EDIT STATIC PAGE SHOW :
def edit_static_page(request,slug):
    if 'id' in request.session:
        getpage = static_page.objects.get(slug=slug)
        disc =  {
            'title': getpage.title,
            'getpage':getpage,
        }
        return render(request,'swooee/edit_static_page.html',disc)
    else:
        return redirect('login')

# EDIT PAGE CONTAINS :
def edit_page(request,slug):
    if  'id' in request.session:
        pagedata = static_page.objects.get(slug=slug)
        pagedata.title = request.POST['pname'] if request.POST['pname'] else pagedata.name
        pagedata.slug = request.POST['pname'] if request.POST['pname'] else pagedata.slug
        pagedata.discription = request.POST['pdis'] if request.POST['pdis'] else pagedata.discription
        
        page = render_to_string('head_foot/New.html', {
                            'title1': request.POST['pname'],
                            'page': request.POST['pdis'],
                        })
        pagedata.page = page
        print(date1)
        pagedata.updated_at = date1
        pagedata.status = request.POST['radiobtn'] if request.POST['radiobtn'] else pagedata.status
        try:
            pagedata.Image = request.FILES['pimg']
        except :
            pagedata.Image = pagedata.Image
        pagedata.save()
        return redirect('allstaticpage')
    else:
        return redirect('login')
    
# view Static page :
def viewpage(request,slug):
    pagedata = static_page.objects.get(slug=slug)
    # if pagedata.status == '0':    
    disc =  {
        'title': 'Corona Admin | ' + pagedata.title,
        'page':pagedata.page,
    }
    return render(request,'head_foot/New1.html',disc)

# Add User Contains : 
def adduser(request):
    if 'id' in request.session:
        if request.method == "POST":
            usrname = request.POST['username']
            email = request.POST['email'].casefold()
            fname = request.POST['fname']
            lname = request.POST['lname']
            passwrd = request.POST['password']
            image = request.FILES['img[]']
            try :
                # if Value Is 1 == Mail is Sent
                chek =  request.POST['check']
            except:
                # If Value Is 0 == Mail is not sent
                chek = '0'
            
            slug = fname + ' ' + lname
            usr_em = user.objects.filter(email=email)
            if len(usr_em) > 0:
                messages.warning(request, 'Email Is Already Use')
                return redirect('adduserpage')
            else:
                users = user.objects.create(
                    username = usrname,
                    email = email,
                    slug = slug,
                    first_name = fname,
                    last_name = lname,
                    password = passwrd,
                    Image = image,
                    checkbox = chek,
                    created_at = date1,
                    updated_at = date1,
                )
                users.save()
                # Email sending
                if chek == '1':
                    current_site = get_current_site(request)
                    mail_subject = 'Activate 🛎️ your account From Swooee.'
                    message = render_to_string('head_foot/email.html', {
                                'user': user,
                                'fname': fname,
                                'lname' : lname,
                                'domain': current_site.domain,
                                'token': fname + '-' + lname,
                            })
                    email_from = settings.EMAIL_HOST_USER
                    to_email = [email,]
                    send_mail(mail_subject, message, email_from, to_email)
                # return HttpResponse('Please confirm your email address to complete the registration')
                return redirect('alluser')
    else:
        return redirect('login')

# Edit User Page :
def edit_userpage(request,slug):
    if 'id' in request.session:
        getuser = user.objects.get(slug=slug)
        disc =  {
        'title': 'Corona Admin | ' + getuser.first_name + ' ' + getuser.last_name,
        'usr' : getuser,
        }
        return render(request,'swooee/edit_user.html',disc)
    else:
        return redirect('login')

# Update User Function :
def edit_user(request,slug):
    if  'id' in request.session:
        usrdata = user.objects.get(slug=slug)
        email =request.POST['email'].casefold()
        usrdata.username = request.POST['username'] if request.POST['username'] else usrdata.username
        usrdata.first_name = request.POST['fname'] if request.POST['fname'] else usrdata.first_name
        usrdata.last_name = request.POST['lname'] if request.POST['lname'] else usrdata.last_name
        slug = request.POST['fname'] + ' ' + request.POST['lname']
        usrdata.slug = slug if slug else usrdata.slug
        usrdata.password = request.POST['password'] if request.POST['password'] else usrdata.password
        usrdata.updated_at = date1
        try:
            usrdata.Image = request.FILES['img']
        except :
            usrdata.Image = usrdata.Image
        

        user1 = user.objects.filter(email=email)  
        if(not user1):
            usrdata.email = email
            usrdata.checkbox = '0'
            
        else:
            usrdata.email = usrdata.email        
        
        try : 
            check = request.POST['check']
            usrdata.checkbox = check
        except:
            usrdata.checkbox = usrdata.checkbox
        usrdata.status = request.POST['radiobtn'] if request.POST['radiobtn'] else usrdata.status
        try:
            if check == '1':
                usrdata.checkbox = '1'
                current_site = get_current_site(request)
                mail_subject = 'Activate your account From Swooee.'
                message = render_to_string('head_foot/email.html', {
                            'user': user,
                            'fname': usrdata.first_name,
                            'lname' : usrdata.first_name,
                            'domain': current_site.domain,
                        })
                email_from = settings.EMAIL_HOST_USER
                to_email = [email,]
                send_mail(mail_subject, message, email_from, to_email)
        except:
            pass
        usrdata.save()
        return redirect('alluser')
    else:
        return redirect('login')
        
# DELETE User FUNNCTION :
# Ajax Using CODE.
def delete_user(request):
    if request.method=='POST':
        id = request.POST.get('pid')
        print(id)
        getpas = user.objects.get(pk=id)
        getpas.delete()
        return JsonResponse({'status':1})
        # return redirect("Home")
    else:
        return JsonResponse({'status':0})

# All Banners Show:
def all_banner_page(request):
    if 'id' in request.session:
        banners = banner.objects.all()
        disc =  {
            'title': 'Corona Admin | All Banners',
            'bnr':banners,
        }
        return render(request,'swooee/all_banner_page.html',disc)
    else:
        return redirect('login')
    
# Add Banners Page:
def add_banner_page(request):
    if 'id' in request.session:
        # banners = banner.objects.all()
        disc =  {
            'title': 'Corona Admin | Add Banners',
        }
        return render(request,'swooee/form_banner.html',disc)
    else:
        return redirect('login')

# Added Banner Query :
def add_banner(request):
    if 'id' in request.session:
        if request.method == "POST":
            title = request.POST['title']
            disc = request.POST['discripation']
            file = request.FILES['img[]']
            extens = request.POST['type']
            
            banr = banner.objects.create(
                short_title = title,
                discription = disc,
                file = file,
                extension = extens,
                created_at = date1,
                updated_at = date1,
            )
            return redirect('allbannerpage')
    else:
        return redirect('login')       
        
# Edit Page For Banner :
def edit_banner_page(request,slug):
    if 'id' in request.session:
        getbnr = banner.objects.get(slug=slug)
        disc =  {
            'title': getbnr.short_title,
            'bnr':getbnr,
        }
        return render(request,'swooee/edit_banner_page.html',disc)
    else:
        return redirect('login')

# Update Banner Function:
def edit_banner(request,slug):
    try:
        if 'id' in request.session:
            getbnr = banner.objects.get(slug=slug)
            getbnr.short_title = request.POST['title'] if request.POST['title'] else getbnr.short_title
            getbnr.slug = request.POST['title'] if request.POST['title'] else getbnr.slug
            getbnr.discription = request.POST['discripation'] if request.POST['discripation'] else getbnr.discription
            try :
                getbnr.file = request.FILES['img']
            except:
                getbnr.file = getbnr.file
            try:
                getbnr.extension = request.POST['type']
            except:
                getbnr.extension = getbnr.extension
            getbnr.updated_at = date1
            getbnr.status = request.POST['radiobtn'] if request.POST['radiobtn'] else usrdata.status
            getbnr.save()
            return redirect('allbannerpage')
        else:
            return redirect('login')
    except:
        return render(request, 'swooee/error_404.html')
    
# DELETE Banner FUNNCTION :
# Ajax Using CODE.
def delete_banner(request):
    if request.method=='POST':
        id = request.POST.get('pid')
        print(id)
        getpas = banner.objects.get(pk=id)
        getpas.delete()
        return JsonResponse({'status':1})
        # return redirect("Home")
    else:
        return JsonResponse({'status':0})

# Next One