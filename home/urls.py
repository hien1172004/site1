from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # Token
    path("api/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    # Book
    path("book/edit", EditBookView.as_view(), name="book-edit"),
    path("book/delete", DeleteBookView.as_view(), name="book-delete"),
    path("book/search", SearchBooksView.as_view(), name="book-search"),
    path("book/add", AddBookView.as_view(), name="book-add"),
    # Manager
    path("user/login", LoginView.as_view(), name="login"),
    path("user/password-set", ChangePasswordView.as_view(), name="change-password"),
    # Student
    path("student/detail", StudentDetailView.as_view(), name="student-detail"),
    path("student/add", StudentAddView.as_view(), name="student-add"),
    path("student/edit", StudentEditView.as_view(), name="student-edit"),
    path("student/delete", StudentDeleteView.as_view(), name="student-delete"),
    path("student/search", StudentSearchView.as_view(), name="student-search"),
    # --LIBRARY LOG--
    path("lib/check-in", CheckInView.as_view(), name="check_in"),
    path("lib/check-out", CheckOutView.as_view(), name="check_out"),
    path("lib/inlibrary", GetStudentInLibraryView.as_view(), name="student-in-library"),
    path("lib/countinday", LibraryLogCountInDayView.as_view(), name="count_in_day"),
    # --BOOK TRANSACTION--
    path("trans/add", BookTransactionAddView.as_view(), name="add_book_transaction"),
    path(
        "trans/search",
        BookTransactionSearchView.as_view(),
        name="search_book_transactions",
    ),
    path(
        "trans/return",
        BookTransactionReturnView.as_view(),
        name="update-transaction-status",
    ),
    path("trans/expried", GetExpriedBookView.as_view(), name="expried_book"),
    path("trans/count", ExpiredBooksCountView.as_view(), name="count_expried"),
    # ----CATEGORY
    path("category/add", CategoryAddView.as_view(), name="add_category"),
    path("category/edit", CategoryEditview.as_view(), name="edit_category"),
    path("category/delete", CatergoryDeleteView.as_view(), name="delete_category"),
    path("category/all", CategoryAllView.as_view(), name="all_category"),
]
