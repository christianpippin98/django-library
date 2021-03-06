from django.urls import include, path
from .views import *


app_name = "libraryapp"

urlpatterns = [
    path('librarians/', librarian_list, name='librarians'),
    path('libraries/', library_list, name='libraries'),
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('book/form', book_form, name='book_form'),
    path('library/form', library_form, name='library_form'),
    path('books/<int:book_id>/', book_details, name='book'),
]