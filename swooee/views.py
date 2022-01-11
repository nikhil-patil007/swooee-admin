from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from datetime import datetime
from django.template.loader import render_to_string
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

# ADD SUBCATEGORY FORM :
def subcategorypage(request):
    if 'id' in request.session:
        cats = Categories.objects.all()
        disc =  {
            'title':'Corona Admin | Add SubCategory Forms',
            'cat' : cats,
        }
        return render(request, 'swooee/form_subcategory.html',disc)
    else:
        return redirect("login")
    
# ADD SUBCATEGORY FORM :
def childcategorypage(request):
    if 'id' in request.session:
        cats = Categories.objects.all()
        disc =  {
            'title':'Corona Admin | Add ChildCategory Forms',
            'cat' : cats,
        }
        return render(request, 'swooee/form_childcategory.html',disc)
    else:
        return redirect("login")

# ALL PRODUCT PAGE SHOW :
def all_products(request):
    if 'id' in request.session:
        pro = Product.objects.all()
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

            user = Admin_user.objects.filter(username=ur)
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
        produ = Product.objects.create(
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
        getusr = User.objects.all()
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
        getpro = Product.objects.get(slug=slug)
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
        productdata = Product.objects.get(slug=slug)
        
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
        getpas = Product.objects.get(pk=id)
        getpas.delete()
        return JsonResponse({'status':1})
        # return redirect("Home")
    else:
        return JsonResponse({'status':0})
    
# STATIC PAGE CONTAIN :
def add_static_page(request):
    if  'id' in request.session:
        if request.method == "POST":
            form = Static_pageForm(data=request.POST)
            if form.is_valid():
                form = form.save(commit=False)
            if 'Image' in request.FILES:
                form.Image = request.FILES['Image']
            form.save()
            return redirect('allstaticpage')
    else:
        return redirect('login')

# STATIC EXTRA PAGES SHOW CONTAIN :
def staticpage(request):
    if  'id' in request.session:
        form = Static_pageForm()
        disc =  {
                'title':'Corona Admin | Add Dyanmic Page',
                'form' :form,
            }
        return render(request, 'swooee/form_static_page.html',disc)
    else:
        return redirect('login')

# View ALL STATIC PAGES :
def view_static_page(request):
    if  'id' in request.session:
        page = Static_page.objects.all()
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
        getpas = Static_page.objects.get(pk=id)
        getpas.delete()
        return JsonResponse({'status':1})
        # return redirect("Home")
    else:
        return JsonResponse({'status':0})

# EDIT STATIC PAGE SHOW :
def edit_static_page(request,slug):
    if 'id' in request.session:
        getpage = Static_page.objects.get(slug=slug)
        form = Static_pageForm(instance=getpage)
        disc =  {
            'title': getpage.title,
            'getpage':getpage,
            'form' :form,
        }
        return render(request,'swooee/edit_static_page.html',disc)
    else:
        return redirect('login')

# EDIT PAGE CONTAINS :
def edit_page(request,slug):
    if  'id' in request.session:
        getpage = Static_page.objects.get(slug=slug)
        form = Static_pageForm(request.POST or None, instance=getpage)
        if form.is_valid():
            form = form.save(commit=False)
            if 'Image' in request.FILES:
                form.Image = request.FILES['Image']
            form.save()
            getpage.slug = getpage.title
            getpage.status = request.POST['radiobtn'] if request.POST['radiobtn'] else productdata.getpage
            getpage.save()
            return redirect('allstaticpage')
    else:
        return redirect('login')
    
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
            usr_em = User.objects.filter(email=email)
            if len(usr_em) > 0:
                messages.warning(request, 'Email Is Already Use')
                return redirect('adduserpage')
            else:
                users = User.objects.create(
                    username = usrname,
                    email = email,
                    slug = slug,
                    first_name = fname,
                    last_name = lname,
                    password = passwrd,
                    Image = image,
                    created_at = date1,
                    updated_at = date1,
                )
                users.save()
                # Email sending
                if chek == '1':
                    current_site = get_current_site(request)
                    mail_subject = 'Activate 🛎️ your account From Swooee.'
                    message = render_to_string('head_foot/email.html', {
                                'user': email,
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
        getuser = User.objects.get(slug=slug)
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
        usrdata = User.objects.get(slug=slug)
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
        

        user1 = User.objects.filter(email=email)  
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
                            'user': email,
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
        getpas = User.objects.get(pk=id)
        getpas.delete()
        return JsonResponse({'status':1})
        # return redirect("Home")
    else:
        return JsonResponse({'status':0})

# All Banners Show:
def all_banner_page(request):
    if 'id' in request.session:
        banners = Banner.objects.all()
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
        form = BannerForm()
        disc =  {
            'title': 'Corona Admin | Add Banners',
            'form' : form,
        }
        return render(request,'swooee/form_banner.html',disc)
    else:
        return redirect('login')

# Added Banner Query :
def add_banner(request):
    if 'id' in request.session:
        if request.method == "POST":
            form = BannerForm(data=request.POST)
            if form.is_valid():
                form = form.save(commit=False)
            if 'Image' in request.FILES:
                form.Image = request.FILES['Image']
            form.save()
            return redirect('allbannerpage')
    else:
        return redirect('login')       
        
# Edit Page For Banner :
def edit_banner_page(request,slug):
    if 'id' in request.session:
        getbnr = Banner.objects.get(slug=slug)
        form = BannerForm(request.POST or None, instance=getbnr)
        disc =  {
            'title': getbnr.short_title,
            'bnr':getbnr,
            'form' : form
        }
        return render(request,'swooee/edit_banner_page.html',disc)
    else:
        return redirect('login')

# Update Banner Function:
def edit_banner(request,slug):
    try:
        if 'id' in request.session:
            getbnr = Banner.objects.get(slug=slug)
            form = BannerForm(request.POST or None, instance=getbnr)
            if form.is_valid():
                form = form.save(commit=False)
            if 'Image' in request.FILES:
                form.Image = request.FILES['Image']
            form.save()
            getbnr.slug = getbnr.short_title
            getbnr.status = request.POST['radiobtn'] if request.POST['radiobtn'] else productdata.getbnr
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
        getpas = Banner.objects.get(pk=id)
        getpas.delete()
        return JsonResponse({'status':1})
        # return redirect("Home")
    else:
        return JsonResponse({'status':0})

# Next One
