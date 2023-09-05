from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPassWordChangeForm, MyPasswordResetForm, MySetPasswordForm
from ecommerce.settings import DEBUG

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),


    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPassWordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),
    path('mobile/<slug:data>/<slug:sort>', views.mobile, name='mobiledatasort'),
    
    path('tablet/', views.tablet, name='tablet'),
    path('tablet/<slug:data>/', views.tablet, name='tabletdata'),
    path('tablet/<slug:data>/<slug:sort>', views.tablet, name='tabletdatasort'),
    
    path('watch/', views.watch, name='watch'),
    path('watch/<slug:data>/', views.watch, name='mwatchdata'),
    path('watch/<slug:data>/<slug:sort>', views.watch, name='watchdatasort'),
    
    path('bud/', views.bud, name='bud'),
    path('bud/<slug:data>/', views.bud, name='buddata'),
    path('bud/<slug:data>/<slug:sort>', views.bud, name='buddatasort'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]