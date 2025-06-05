from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import product_list, product_create, product_update, product_delete

urlpatterns = [
    path("", product_list, name="product_list"),                  # shows index_list.html
    path("add/", product_create, name="product_create"),          # shows index.html (form)
    path("update/<int:product_id>/", product_update, name="product_update"),
    path("delete/<int:product_id>/", product_delete, name="product_delete"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)