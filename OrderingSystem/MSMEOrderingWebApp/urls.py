from django.urls import path
from . import views

urlpatterns = [
    path('Login/', views.login_view, name='login'),
    path('Logout/', views.logout_view, name='logout'),
    path('UserRegistration/', views.register_user, name='register_user'),

    path('BusinessDashboard/', views.dashboard, name='dashboard'),
    path('ManageInventory/', views.inventory, name='inventory'),

    path('Point-of-Sale/', views.pos, name='pos'),
    path('Point-of-Sale/Cart/', views.pos_cart_view, name='pos_cart'),

    path('Delivery/', views.delivery, name='delivery'),
    path('Reviews/', views.reviews, name='reviews'),
    path('RegisteredUsers/', views.users, name='users'),

    path('Settings/', views.settings, name='settings'),
    path('settings/online-payment/', views.online_payment_details, name='online_payment_details'),
    path('settings/change-password/', views.change_password, name='change_password'),

    path('BusinessNotifications/', views.business_notifications, name='business_notifications'),

    path('CustomerHomepage/', views.customer_home, name='customer_home'),
    path('CustomerReviews/', views.customer_reviews, name='customer_reviews'),
    path('CustomerCart/', views.customer_cart, name='customer_cart'),
    path('CustomerCheckout/', views.customer_checkout, name='customer_checkout'),
    path('CustomerNotifications/', views.customer_notifications, name='customer_notifications'),
    path('CustomerProfile/', views.customer_profile, name='customer_profile'),

    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit-price/', views.edit_product_price, name='edit_product_price'),
    path('toggle-availability/<int:product_id>/', views.toggle_availability, name='toggle_availability'),


]
