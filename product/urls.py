from django.urls import path,include
from . import views

app_name = 'Product'
urlpatterns = [
    path('', views.ProductClass.as_view(), name='products'),
    path('create/', views.CreateProduct.as_view(), name='create-product'),
    path('add/', views.CreateProduct.as_view(), name='add-product'),
    path('delete/<int:id>/', views.DeleteProduct.as_view(), name='delete-product'),
    path('update/<int:id>/', views.UpdateProduct.as_view(), name='update-product'),
    path('detail/<int:id>/', views.DetailProduct.as_view(), name='detail-product'),
    path('updateProductData/<int:id>/', views.UpdateProduct.as_view(), name='update-product-post'),
    path('search/<str:name>', views.SearchProduct.as_view(), name='get-product-search'),

    path('category/<int:id>/', views.category_search, name='category_search'),
    path('category/', views.CategoryClass.as_view(), name='categoryes'),
    path('createCategory/', views.CreateCategory.as_view(), name='create-category'),
    path('addCategory/', views.CreateCategory.as_view(), name='add-category'),
    path('deleteCategory/<int:id>/', views.DeleteCategory.as_view(), name='delete-category'),
    path('updateCategory/<int:id>/', views.UpdateCategory.as_view(), name='update-category'),
    path('updateCategoryData/<int:id>/', views.UpdateCategory.as_view(), name='update-category-post'),

    path('variation/', views.VariationClass.as_view(), name='variations'),
    path('createVariation/', views.CreateVariation.as_view(), name='create-variation'),
    path('addVariation/', views.CreateVariation.as_view(), name='add-variation'),
    path('deleteVariation/<int:id>/', views.DeleteVariation.as_view(), name='delete-variation'),
    path('updateVariation/<int:id>/', views.UpdateVariation.as_view(), name='update-variation'),
    path('updateVariationData/<int:id>/', views.UpdateVariation.as_view(), name='update-variation-post'),



    path("addCart/<int:id>/", views.AddCart, name='addCart'),
    path("cart/", views.Cart, name='cart'),
    path("DeleteCart/<int:id>/", views.DeleteCart, name='delete-item-cart'),

    path('addmessage/', views.CreateMessage.as_view(), name='add_message'),

    ]
