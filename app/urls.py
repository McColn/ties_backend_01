from django.urls import path, include
from rest_framework import routers
from . import views
from .views import (UserInfoAPIView, CustomUserCreateView,
                    CustomAuthTokenView, CustomUserUpdateView,
                    CustomUserDeleteView, CustomUserListView, LogoutAPIView,
                    InvestmentViewSet, FrontPageInfoViewSet, InvestmentComplianceViewSet,
                    ConsultationComplianceViewSet, ItemViewSet, OrderViewSet,
                    MiningTrendsViewSet, SMSMessageViewSet, PostListCreateAPIView,
                    CommentListCreateAPIView, ChangePasswordView, UserEditTwoViewSet,MyInbox,
                    ConsultancyTiesCategoryViewSet, ConsultancyTiesDetailsViewSet,SendMessages, GetMessages,
                    SearchItem, SearchUser, SevenDayMiningViewSet, PremiumView)

router = routers.DefaultRouter()
router.register(r'investments', InvestmentViewSet)
router.register(r'frontPageInfo', FrontPageInfoViewSet)
router.register(r'investmentCompliance', InvestmentComplianceViewSet)
router.register(r'consultationCompliance', ConsultationComplianceViewSet)
router.register(r'item', ItemViewSet)
router.register(r'order', OrderViewSet)
router.register(r'miningTrends', MiningTrendsViewSet)
router.register(r'messages', SMSMessageViewSet)
router.register(r'posts', PostListCreateAPIView)
router.register(r'comments', CommentListCreateAPIView)
router.register(r'userUpdate', UserEditTwoViewSet)
router.register(r'consultancyTiesCategory', ConsultancyTiesCategoryViewSet)
router.register(r'consultancyTiesDetails', ConsultancyTiesDetailsViewSet)
router.register(r'sms', SendMessages)
router.register(r'premier', PremiumView)

urlpatterns = [
    # Your other URL patterns
    path('api/', include(router.urls)),

    path('', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('investment/', views.investment, name='investment'),
    path('investmentDetail/<int:id>/', views.investmentDetail, name='investmentDetail'),
    path('investmentAdd/', views.investmentAdd, name='investmentAdd'),
    path('investmentEdit/<int:id>/', views.investmentEdit, name='investmentEdit'),
    path('investmentDelete/<int:id>/', views.investmentDelete, name='investmentDelete'),
    path('investmentCompliance/', views.investmentCompliance, name='investmentCompliance'),
    path('investmentComplianceAdd/', views.investmentComplianceAdd, name='investmentComplianceAdd'),
    path('investmentComplianceEdit/<int:id>/', views.investmentComplianceEdit, name='investmentComplianceEdit'),
    path('investmentComplianceDelete/<int:id>/', views.investmentComplianceDelete, name='investmentComplianceDelete'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('marketAdd/', views.marketAdd, name='marketAdd'),
    path('mineral/', views.mineral, name='mineral'),
    path('marketEdit/<int:id>/', views.marketEdit, name='marketEdit'),
    path('marketDescription/<int:id>/', views.marketDescription, name='marketDescription'),
    path('marketDelete/<int:id>/', views.marketDelete, name='marketDelete'),
    path('consultationCompliance/', views.consultationCompliance, name='consultationCompliance'),
    path('consultationComplianceAdd/', views.consultationComplianceAdd, name='consultationComplianceAdd'),
    path('consultationComplianceEdit/<int:id>/', views.consultationComplianceEdit, name='consultationComplianceEdit'),
    path('consultationComplianceDelete/<int:id>/', views.consultationComplianceDelete, name='consultationComplianceDelete'),
    path('orders/', views.orders, name='orders'),
    path('miningTrends/', views.miningTrends, name='miningTrends'),
    path('miningTrendsAdd/', views.miningTrendsAdd, name='miningTrendsAdd'),

    path('user-info/', UserInfoAPIView.as_view(), name='user-info'),
    path('api/register/', CustomUserCreateView.as_view(), name='create_user'),
    path('api/login/', CustomAuthTokenView.as_view(), name='login'),
    path('api/update-user/<int:pk>/', CustomUserUpdateView.as_view(), name='update-user'),
    path('api/delete-user/<int:pk>/', CustomUserDeleteView.as_view(), name='delete_user'),
    path('api/list-user/', CustomUserListView.as_view(), name='list_user'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),

    # Chat/Text Messaging Functionality
    path('my-inbox/', MyInbox.as_view(), name='my-inbox'),
    path('messages/<int:sender_id>/<int:receiver_id>/', GetMessages.as_view(), name='get_messages'),
    # path("send-messages/", views.SendMessages.as_view()),

    # Get profile
    path("profile/<int:pk>/", views.ProfileDetail.as_view()),
    path('search/', SearchUser.as_view(), name='search_user'),
    path('searchItem/', SearchItem.as_view(), name='search_item'),
    

    # firebase authentification
    

    path('api/sevenDayTrends/', SevenDayMiningViewSet.as_view(), name='sevenDayTrends'),
]

