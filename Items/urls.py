from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Display_all_products, Display_specific_product, Search_product_Tag, Display_all_Reviews, Make_a_review, Search_products_category, Search_products_subcategory, Search_products

urlpatterns = [

    path('display-products', Display_all_products.as_view(), name='display-products' ),
    path('product/<int:pk>', Display_specific_product.as_view(), name='products' ),
    path('review', Make_a_review.as_view(), name='review' ),
    path('display-reviews/<int:pk>', Display_all_Reviews.as_view(), name='display-review' ),
    path('search/category/', Search_products_category.as_view(), name='search-category' ),
    path('search/subcategory/', Search_products_subcategory.as_view(), name='search-subcategory' ),
    path('search/', Search_products.as_view(), name='search' ),
    path('product-tag/', Search_product_Tag.as_view(), name='search' ),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)