from django.db import models
from rest_framework import serializers

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=300, unique=True)
    city = models.CharField(max_length=300)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        pass


class Author(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def set_new_rating(self, value):
        self.rating = value
        self.save()

    def books_count(self):
        return self.books.count()


class PublishedBook(models.Manager):
    def get_queryset(self):
        return self.filter(is_published=True)

    def filter_by_name(self, name_pattern):
        return self.filter(name__contains=name_pattern)


class NotPublishedBook(models.Manager):
    def get_queryset(self):
        return self.filter(is_published=False)


def valid_num_pages(value):
    if not(10 >= value >= 5000):
        raise serializers.ValidationError('invalid num of pages')


class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    num_pages = models.IntegerField(default=0,
                                    validators=[valid_num_pages])
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='books')
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE,
                                  related_name='books')

    objects = models.Manager()
    published_books = PublishedBook()
    not_published_books = NotPublishedBook()

    @classmethod
    def top_ten(cls):
        return cls.objects.all()[:10]

    @staticmethod
    def cmp_books(book1, book2):
        return book1.price > book2.price
