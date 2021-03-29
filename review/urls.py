from django.urls import path

from . import views

urlpatterns = [
    path("product/index=<str:pk>/", views.ReviewProduct.as_view()),
    path("customer/index=<str:pk>/", views.ReviewCustomer.as_view()),
    path("product/index=<str:pk>/star=<int:star>", views.ReviewProductWithStar.as_view()),
    path("popularproducts/number=<int:N>/start=<str:start_date>/end=<str:end_date>", views.ReviewPopularItems.as_view()),
    path("productiveauthors/number=<int:N>/start=<str:start_date>/end=<str:end_date>", views.ReviewProductiveAuthors.as_view()),
    path("bestproducts/number=<int:N>", views.ReviewBestItems.as_view()),
    path("backers/number=<int:N>/start=<str:start_date>/end=<str:end_date>", views.ReviewBestAuthors.as_view()),
    path("haters/number=<int:N>/start=<str:start_date>/end=<str:end_date>", views.ReviewWorstAuthors.as_view())

]