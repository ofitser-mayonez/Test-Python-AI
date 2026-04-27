from django.contrib import admin

from api.models import Athenaeum, Book, BookAthenaeum

admin.site.register(Book)
admin.site.register(Athenaeum)
admin.site.register(BookAthenaeum)
