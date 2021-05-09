from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('products/', products, name="products"),
    path('products/<int:pk>/', product_page, name="product_page"),
    path('sign-in/', sign_in, name="sign-in"),
    path('sign-out/', sign_out, name="sign-out"),
    path('register/', reg, name="register")
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
