from django.urls import path,include
from . import views

urlpatterns = [
    path('admin-index/',views.home,name='home'),
    path('',views.login,name='login'),
    path('login_admin/',views.login_admin,name='loginuser'),
    path('logout/',views.logout_admin,name='logout'),
    path('product_page/',views.productpage,name='productpage'),
    path('user_page/',views.adduserpage,name='adduserpage'),
    path('add_user/',views.adduser,name='adduser'),
    path('category_page/',views.categorypage,name='categorypage'),
    path('subcategory_page/',views.subcategorypage,name='subcategorypage'),
    path('childcategory_page/',views.childcategorypage,name='childcategorypage'),
    path('add_category/',views.add_category,name='addcategory'),
    path('all_Product/',views.all_products,name='allProduct'),
    path('all_user_page/',views.all_user,name='alluser'),
    path('add_product/',views.add_product,name='addproduct'),
    path('all_category/',views.all_cat,name='allCat'),
    path('all_banners/',views.all_banner_page,name='allbannerpage'),
    path('banners_add/',views.add_banner_page,name='addbannerpage'),
    path('added_banner/',views.add_banner,name='addedbanner'),
    
    path('banners_page/<str:slug>/edit/',views.edit_banner_page,name='editbannerpage'),
    path('category_page/<str:slug>/edit/',views.edit_cat_page,name='editcatpage'),
    path('edited_category/<str:slug>/',views.edit_category,name='editcats'),
    path('product_page/<str:slug>/edit/',views.edit_product_page,name='editpropage'),
    path('edited_product/<str:slug>/',views.edit_product,name='editproduct'),
    path('static_page/<str:slug>/edit/',views.edit_static_page,name='editstaticpage'),
    path('edited_Page/<str:slug>/',views.edit_page,name='editpage'),
    path('edited_banner/<str:slug>/',views.edit_banner,name='editedbanner'),
    path('edited_User/<str:slug>/',views.edit_user,name='editeduser'),
    path('edit_user_page/<str:slug>/',views.edit_userpage,name='editupage'),
    path('delete_categoty/',views.delete_cat,name='deleteCat'),
    path('delete_product/',views.delete_product,name='deleteproduct'),
    path('delete_banner/',views.delete_banner,name='deletebanner'),
    path('delete_page/',views.delete_page,name='deletepage'),
    path('delete_user/',views.delete_user,name='deleteuser'),
    
    path('add_page/',views.staticpage,name='static'),
    
    path('static_page_added/',views.add_static_page,name='staticpage'),
    path('all_static_page/',views.view_static_page,name='allstaticpage'),
    
]



