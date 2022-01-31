"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from shop_backend import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.ProductListAPIView.as_view()),
    path('api/v1/products/<int:id>/', views.ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/products/review/<int:id>/', views.ReviewAPIView.as_view()),
    path('api/v1/products/tags/<int:id>/', views.TagsAPIView.as_view()),
    path('api/v1/login/', user_views.LoginAPIView.as_view()),
    path('api/v1/register/', user_views.RegisterAPIView.as_view()),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


# path('api/v1/products/', views.product_list_view),
    # path('api/v1/products/<int:id>/', views.product_detail_view),
    # path('api/v1/products/review/', views.get_review),
    # path('api/v1/products/tags/', views.get_tags),
    # path('api/v1/login/', user_views.login),
    # path('api/v1/register/', user_views.register),
