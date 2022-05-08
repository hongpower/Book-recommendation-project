import datetime
from haystack import indexes
from book_it_up.models import Book, BookGrade, Review
from django.contrib import admin

#
class BookIndex(indexes.SearchIndex, indexes.Indexable):
    # 모든 index 모델은 꼭 한개의 document=True인 필드가 필요. 어떤게 primary field인지 확인
    # text라는 필드 네임은 신경안써도 ㄱㅊ. 그냥 convention임
    # use_template는 data template 활용가능케 해줌.
    text = indexes.CharField(document=True, use_template=True, template_name='search/book_text.txt')
    book_id = indexes.CharField(model_attr='book_id')
    title = indexes.CharField(model_attr='title')
    cover = indexes.CharField(model_attr='cover', null=True)
    author = indexes.CharField(model_attr='author', null=True)
    publisher = indexes.CharField(model_attr='publisher', null=True)
    price = indexes.CharField(model_attr='price', null=True)
    pubdate = indexes.CharField(model_attr='pubdate', null=True)
    category = indexes.CharField(model_attr='category', null=True)

    # 자동완성 기능 :
    # EdgeNgram 에서 바꿈
    content_auto = indexes.NgramField(model_attr="title")

    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all().order_by('-pubdate')
        #return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

    """
    def prepare_review(self, obj):
        return Review.review_id(obj)
        # return BookGrade.review_cnt(obj)
    """

    """"
    def prepare(self, object):
        self.prepared_data = super(BookIndex, self).prepare(object)

        pre_data = get_book_grade(id=object.book_id)
        self.prepared_data['book_id'] = pre_data.book_id

        return self.prepared_data
    """

