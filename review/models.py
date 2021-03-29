from django.db import models
import datetime
import pytz
utc = pytz.UTC


class Review(models.Model):

    customer_id = models.TextField("customer_id")
    review_id = models.TextField("review_id")
    product_id = models.TextField("product_id")
    review_data = models.DateTimeField("Review Date")
    review_star = models.IntegerField("review_star")
    review_title = models.TextField("review_title")

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_by_product_id(cls, product_id):
        tasks = Review.objects.filter(product_id=product_id)
        return tasks

    @classmethod
    def get_by_customer_id(cls, customer_id):
        tasks = Review.objects.filter(customer_id=customer_id)
        return tasks

    @classmethod
    def get_by_product_id_and_rating(cls, product_id, rating):
        tasks = Review.objects.filter(product_id=product_id, review_star=rating)
        return tasks

    @classmethod
    def get_most_reviewed_items(cls, N, start_date, end_date):
        res = list()
        d = dict()
        json_res = list()
        product_ids = list()
        for filed in Review.objects.all():
            if datetime.datetime.strptime(start_date, "%Y-%m-%d").replace(tzinfo=utc) <= filed.review_data \
                    <= datetime.datetime.strptime(end_date, "%Y-%m-%d").replace(tzinfo=utc):
                if filed.product_id not in product_ids:
                    t = len(Review.get_by_product_id(filed.product_id))
                    product_ids.append(filed.product_id)
                else:
                    continue
                if t in [key for key in d.keys()]:
                    lst = d[t]
                    lst.append(filed)
                    d[t] = lst
                else:
                    lst = list()
                    lst.append(filed)
                    d[t] = lst
        keys = [key for key in d.keys()]
        keys.sort()
        keys = keys[::-1]
        for i in range(len(keys)):
            for j in range(len(d[keys[i]])):
                if len(res) == N:
                    break
                else:
                    res.append(d[keys[i]][j].product_id)
        for j in range(len(res)):
            json_res.append(Product.get_product(res[j]))
        return json_res

    @classmethod
    def get_most_productive_authors(cls, N, start_date, end_date):
        res = list()
        d = dict()
        authors_ids = list()
        json_res = list()
        for filed in Review.objects.all():
            if datetime.datetime.strptime(start_date, "%Y-%m-%d").replace(tzinfo=utc) <= filed.review_data\
                    <= datetime.datetime.strptime(end_date, "%Y-%m-%d").replace(tzinfo=utc):
                if filed.customer_id not in authors_ids:
                    t = len(Review.get_by_customer_id(filed.customer_id))
                    authors_ids.append(filed.customer_id)
                else:
                    continue
                if t in [key for key in d.keys()]:
                    lst = d[t]
                    lst.append(filed)
                    d[t] = lst
                else:
                    lst = list()
                    lst.append(filed)
                    d[t] = lst
        keys = [key for key in d.keys()]
        keys.sort()
        keys = keys[::-1]
        for i in range(len(keys)):
            for j in range(len(d[keys[i]])):
                if len(res) == N:
                    break
                else:
                    res.append(d[keys[i]][j].customer_id)
        for j in range(len(res)):
            json_res.append(Customer.get_customer(res[j]))
        print(json_res)
        return json_res

    @classmethod
    def get_best_products(cls, N):
        res = list()
        json_res = list()
        best_ids = list()
        loser_ids = list()
        for field in Review.objects.all():
            if field.review_star == 5:
                best_ids.append(field.product_id)
            else:
                loser_ids.append(field.product_id)
        for i in range(len(loser_ids)):
            if loser_ids[i] in best_ids:
                best_ids.remove(loser_ids[i])
        for j in range(len(best_ids)):
            if len(res) == N:
                break
            else:
                res.append(best_ids[j])
        for k in range(len(res)):
            json_res.append(Product.get_product(res[k]))
        return json_res

    @classmethod
    def get_user_by_reviews_stars(cls, N, start_date, end_date, begin, end):
        d = dict()
        res = list()
        json_res = list()
        for field in Review.objects.all():
            if datetime.datetime.strptime(start_date, "%Y-%m-%d").replace(tzinfo=utc) <= field.review_data \
                    <= datetime.datetime.strptime(end_date, "%Y-%m-%d").replace(tzinfo=utc):
                if field.review_star == begin or field.review_star == end:
                    if field.customer_id not in d:
                        d[field.customer_id] = 1
                    else:
                        d[field.customer_id] += 1
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
        keys = [key for key in d.keys()]
        for i in range(len(keys)):
            if len(res) == N:
                break
            else:
                res.append(keys[i])
        for k in range(len(res)):
            json_res.append(Customer.get_customer(res[k]))
        return json_res


class Product(models.Model):
    product_id = models.TextField("product_id")
    product_title = models.TextField("product_title")
    product_category = models.TextField("product_category")
    total_votes = models.IntegerField("total_votes")

    def __str__(self):
        return str(self.product_title)

    @staticmethod
    def get_product(get_id):
        tasks = Product.objects.filter(product_id=get_id)
        return tasks


class Customer(models.Model):
    customer_id = models.TextField("customer_id")
    marketplace = models.TextField("marketplace")

    def __str__(self):
        return str(self.customer_id)

    @staticmethod
    def get_customer(get_id):
        tasks = Customer.objects.filter(customer_id=get_id)
        return tasks
