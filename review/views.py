from rest_framework.views import APIView
from rest_framework.views import Response
from .models import Review
from .serialize import ReviewDetailSerializer, ProductDetailSerializer, CustomerDetailSerializer


class ReviewProduct(APIView):
    @staticmethod
    def get(request, pk):
        queryset = Review.get_by_product_id(pk)
        return Response(ReviewDetailSerializer(queryset, many=True).data)


class ReviewCustomer(APIView):
    @staticmethod
    def get(request, pk):
        queryset = Review.get_by_customer_id(pk)
        return Response(ReviewDetailSerializer(queryset, many=True).data)


class ReviewProductWithStar(APIView):
    @staticmethod
    def get(request, pk, star):
        queryset = Review.get_by_product_id_and_rating(pk, star)
        return Response(ReviewDetailSerializer(queryset, many=True).data)


class ReviewPopularItems(APIView):
    @staticmethod
    def get(request, N, start_date, end_date):
        res = list()
        queryset = Review.get_most_reviewed_items(N, start_date, end_date)
        for i in range(len(queryset)):
            res.append(ProductDetailSerializer(queryset[i], many=True).data)
        return Response(res)


class ReviewProductiveAuthors(APIView):
    @staticmethod
    def get(request, N, start_date, end_date):
        res = list()
        queryset = Review.get_most_productive_authors(N, start_date, end_date)
        for i in range(len(queryset)):
            res.append(CustomerDetailSerializer(queryset[i], many=True).data)
        return Response(res)


class ReviewBestItems(APIView):
    @staticmethod
    def get(request, N):
        res = list()
        queryset = Review.get_best_products(N)
        for i in range(len(queryset)):
            res.append(ProductDetailSerializer(queryset[i], many=True).data)
        return Response(res)


class ReviewBestAuthors(APIView):
    @staticmethod
    def get(request, N, start_date, end_date):
        res = list()
        queryset = Review.get_user_by_reviews_stars(N, start_date, end_date, 4, 5)
        for i in range(len(queryset)):
            res.append(CustomerDetailSerializer(queryset[i], many=True).data)
        return Response(res)


class ReviewWorstAuthors(APIView):
    @staticmethod
    def get(request, N, start_date, end_date):
        res = list()
        queryset = Review.get_user_by_reviews_stars(N, start_date, end_date, 1, 2)
        for i in range(len(queryset)):
            res.append(CustomerDetailSerializer(queryset[i], many=True).data)
        return Response(res)
