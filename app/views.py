# views.py
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, serializers
from rest_framework import status
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ( CustomUser,Investments,FrontPageInfo, InvestmentCompliance,
                     ConsultationCompliance, Item, Order, OrderItem, MiningTrends, Message,
                       Profile, ChatMessage, Post, Comment, ConsultancyTiesDetails, ConsultancyTiesCategory )
from .serializers import ( InvestmentsSerializer,FrontPageInfoSerializer,
                          InvestmentComplianceSerializer, ConsultationComplianceSerializer,
                          ItemSerializer, OrderSerializer, MiningTrendsSerializer,
                          SMSMessageSerializer, ProfileSerializer, MessageSerializer,
                          PostSerializer,CommentSerializer, ChangePasswordSerializer, UserEditSerializer,
                           ConsultancyTiesDetailsSerializer, ConsultancyTiesCategorySerializer )
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


from django.db.models import OuterRef, Subquery
from django.db.models import Q

from .forms import *


def base(request):
    return render(request,'app/base.html')



def investment(request):
    x = Investments.objects.all()
    context = {
        'x':x,
    }
    return render(request,'app/investment.html',context)

def investmentDetail(request,id):
    x = Investments.objects.get(id=id)
    context = {
        'x':x,
    }
    return render(request,'app/investmentDetail.html',context)

def investmentAdd(request):
    if request.method == 'POST':
        form = InvestmentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('investment')
    else:
        form = InvestmentsForm()
    context = {
        'form':form,
    }
    return render(request,'app/investmentAdd.html',context)

def investmentEdit(request,id):
    s = Investments.objects.get(id=id)
    form = InvestmentsForm(instance=s)
    if request.method=='POST':
        form = InvestmentsForm(request.POST,request.FILES,instance=s)
        if form.is_valid():
            form.save()

            return redirect('investment')
    context = {
            'form':form,
            's':s
         }

    return render(request,'app/investmentEdit.html',context)

def investmentDelete(request,id):
    x = get_object_or_404(Investments,id=id)
    x.delete()
    return redirect('investment')

def investmentCompliance(request):
    x = InvestmentCompliance.objects.all()
    context = {
        'x':x,
    }
    return render(request,'app/investmentCompliance.html',context)

def investmentComplianceAdd(request):
    if request.method == 'POST':
        form = InvestmentComplianceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('investmentCompliance')
    else:
        form = InvestmentComplianceForm()
    context = {
        'form':form,
    }
    return render(request,'app/investmentComplianceAdd.html',context)

def investmentComplianceEdit(request,id):
    s = InvestmentCompliance.objects.get(id=id)
    form = InvestmentComplianceForm(instance=s)
    if request.method=='POST':
        form = InvestmentComplianceForm(request.POST,request.FILES,instance=s)
        if form.is_valid():
            form.save()

            return redirect('investmentCompliance')
    context = {
            'form':form,
            's':s
         }

    return render(request,'app/investmentComplianceEdit.html',context)

def investmentComplianceDelete(request,id):
    x = get_object_or_404(InvestmentCompliance,id=id)
    x.delete()
    return redirect('investmentCompliance')

def marketplace(request):
    product = 'item'
    x = Item.objects.filter(category__name=product)
    context = {
        'x':x,
    }
    return render(request,'app/marketplace.html',context)

def mineral(request):
    product = 'mine'
    x = Item.objects.filter(category__name=product)
    context = {
        'x':x,
    }
    return render(request,'app/mineral.html',context)

def marketAdd(request):
    category = Category.objects.all()
    user = request.user  # Retrieve the logged-in user directly
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = user  # Set the user for the item
            item.save()
            return redirect('marketplace')
    else:
        form = ItemForm()
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'app/marketAdd.html', context)

def marketDescription(request,id):
    item = Item.objects.get(id=id)
    context = {
        'item':item,
    }
    return render(request,'app/marketDescription.html',context)

def marketEdit(request,id):
    category = Category.objects.all()
    s = Item.objects.get(id=id)
    form = ItemForm(instance=s)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=s)
        if form.is_valid():
            try:
                form.save()
                return redirect('marketplace')
            except Exception as e:
                print(f"Error updating item: {e}")
                # Optionally, add some error message to the context to show on the form
        else:
            print("Form is not valid")
    context = {
            'form':form,
            's':s,
            'category':category
         }

    return render(request,'app/marketEdit.html',context)

def marketDelete(request,id):
    x = get_object_or_404(Item,id=id)
    x.delete()
    return redirect('marketplace')

def consultationCompliance(request):
    categories = ConsultancyTiesCategory.objects.all()
    x = ConsultancyTiesDetails.objects.all()
    context = {
        'categories':categories,
        'x':x,
    }
    return render(request,'app/consultationCompliance.html',context)

def consultationComplianceCategoryAdd(request):
    if request.method == 'POST':
        form = ConsultancyTiesCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('consultationCompliance')
    else:
        form = ConsultancyTiesCategoryForm()
    context = {
        'form':form,
    }
    return render(request,'app/consultationComplianceCategoryAdd.html',context)

def consultationComplianceAdd(request):
    category = ConsultancyTiesCategory.objects.all()
    if request.method == 'POST':
        form = ConsultationComplianceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('consultationCompliance')
    else:
        form = ConsultationComplianceForm()
    context = {
        'form':form,
        'category':category,
    }
    return render(request,'app/consultationComplianceAdd.html',context)

def consultationComplianceEdit(request,id):

    s = ConsultationCompliance.objects.get(id=id)
    form = ConsultationComplianceForm(instance=s)
    if request.method=='POST':
        form = ConsultationComplianceForm(request.POST,request.FILES,instance=s)
        if form.is_valid():
            form.save()

            return redirect('consultationCompliance')
    context = {
            'form':form,
            's':s
         }

    return render(request,'app/consultationComplianceEdit.html',context)

def consultationComplianceDelete(request,id):
    x = get_object_or_404(ConsultationCompliance,id=id)
    x.delete()
    return redirect('investmentCompliance')

from datetime import timedelta
today = timezone.now().date()

def home(request):
    today = timezone.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    orders_this_week = Order.objects.filter(start_date__range=[start_of_week, end_of_week])
    orders_count_per_day = {day: 0 for day in range(7)}

    for order in orders_this_week:
        day_of_week = order.start_date.weekday()
        orders_count_per_day[day_of_week] += 1

    investment_count = Investments.objects.count()
    system_user_count = CustomUser.objects.count()
    system_users = CustomUser.objects.all().order_by('-id')[:3]
    latest_orders = Order.objects.all().order_by('-id')[:3]
    item_count = Item.objects.count()
    today_orders_count = Order.objects.filter(Q(ordered_date__date=today)).count()
    premium_users = CustomUser.objects.filter(is_premium=True).order_by('-id')[:3]

    context = {
        'investment_count': investment_count,
        'system_user_count': system_user_count,
        'system_users': system_users,
        'premium_users': premium_users,
        'item_count': item_count,
        'today_orders_count': today_orders_count,
        'latest_orders': latest_orders,
        'orders_count_per_day': [orders_count_per_day[day] for day in range(7)],
    }

    return render(request, 'app/home.html', context)

def orders(request):
    x = OrderItem.objects.all()
    context = {
        'x':x
    }
    return render(request,'app/orders.html',context)

def miningTrends(request):
    x = MiningTrends.objects.all().order_by('-period')
    context = {
        'x': x
    }
    return render(request, 'app/miningTrends.html', context)

def miningTrendsAdd(request):
    category = Mine.objects.all()
    if request.method == 'POST':
        form = MiningTrendsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('miningTrends')
    else:
        form = MiningTrendsForm()
    context = {
        'form':form,
        'category':category,
    }
    return render(request,'app/miningTrendsAdd.html',context)

class UserInfoAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user_info = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role,
            'image': user.image.url if user.image else None,
            # Add more fields as needed
        }
        return JsonResponse(user_info)

    def put(self, request):
        user = request.user
        data = request.data
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.AllowAny,)

class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserEditSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)


class CustomUserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)

class CustomUserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        logged_in_user = self.request.user
        queryset = CustomUser.objects.exclude(id=logged_in_user.id)
        return queryset

class CustomAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            # Get or create the Token instance for the user
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key})
        except Exception as e:
            # Log the exception or handle it based on your requirements
            return Response({'detail': f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Delete the authentication token
        try:
            request.auth.delete()
        except AttributeError:
            # Handle the case where no token is found
            pass

        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)



class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investments.objects.all()
    serializer_class = InvestmentsSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)


class FrontPageInfoViewSet(viewsets.ModelViewSet):
    queryset = FrontPageInfo.objects.all()
    serializer_class = FrontPageInfoSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)

class InvestmentComplianceViewSet(viewsets.ModelViewSet):
    queryset = InvestmentCompliance.objects.all()
    serializer_class = InvestmentComplianceSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)


class ConsultationComplianceViewSet(viewsets.ModelViewSet):
    queryset = ConsultationCompliance.objects.all()
    serializer_class = ConsultationComplianceSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)
    # permission_classes = [IsAuthenticated]  # Require authentication

    def perform_create(self, serializer):
        # Set the uploaded_by field to the current authenticated user
        serializer.save(uploaded_by=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        item = self.request.data.get('item')
        user = self.request.user
        quantity = self.request.data.get('quantity', 1)  # Default quantity to 1 if not provided

        try:
            item = Item.objects.get(pk=item)
        except Item.DoesNotExist:
            raise serializers.ValidationError("Invalid item ID")

        # Check if the item already exists in the user's cart
        existing_order_item = OrderItem.objects.filter(user=user, item=item).first()

        if existing_order_item:
            # If the item exists, update the quantity using partial_update
            partial_serializer = OrderSerializer(
                existing_order_item,
                data={'quantity': existing_order_item.quantity + quantity},
                partial=True
            )
            partial_serializer.is_valid(raise_exception=True)  # Validate the serializer
            partial_serializer.save()  # Save the updated quantity
            return Response(partial_serializer.data, status=status.HTTP_200_OK)
        else:
            # If the item doesn't exist, create a new order item
            serializer.save(user=user, item=item, quantity=quantity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class OrderDeleteAPIView(APIView):
    def delete(self, request, order_id):
        try:
            order = OrderItem.objects.get(pk=order_id)
            order.delete()
            return Response({"message": "Order deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except OrderItem.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MiningTrendsViewSet(viewsets.ModelViewSet):
    queryset = MiningTrends.objects.filter(period=timezone.now().date())
    serializer_class = MiningTrendsSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)


class SMSMessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = SMSMessageSerializer


class PostListCreateAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentListCreateAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the post ID from the request query parameters
        post_id = self.request.query_params.get('post')

        # Filter comments based on post ID if provided
        if post_id:
            return Comment.objects.filter(post=post_id)
        else:
        # Return empty queryset if no post ID is provided (optional)
            return Comment.objects.none()

    def perform_create(self, serializer):
        # Assuming 'post' is the field name sent from the frontend
        post = self.request.data.get('post')
        author = self.request.user
        content = self.request.data.get('content')

        # Validate 'comment' and retrieve the corresponding post
        try:
            post = Post.objects.get(id=post)
        except Post.DoesNotExist:
            raise serializers.ValidationError("Invalid post ID")

        # Create the comment item with the validated data
        serializer.save(post=post, author=author, content=content)


class UserEditTwoViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserEditSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)


class ConsultancyTiesDetailsViewSet(viewsets.ModelViewSet):
    queryset = ConsultancyTiesDetails.objects.all()
    serializer_class = ConsultancyTiesDetailsSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        clicked_id = int(self.request.query_params.get('id'))
        gst = ConsultancyTiesCategory.objects.get(id=clicked_id)
        queryset = ConsultancyTiesDetails.objects.filter(category__id=gst.id).distinct()
        return queryset

class ConsultancyTiesCategoryViewSet(viewsets.ModelViewSet):
    queryset = ConsultancyTiesCategory.objects.all()
    serializer_class = ConsultancyTiesCategorySerializer
    authentication_classes = [TokenAuthentication]




#########################################################################
from django.db.models import OuterRef, Subquery
from django.db.models import Q
from .models import *
from .serializers import *


# Chat APp
class MyInbox(generics.ListAPIView):
    serializer_class = MessageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id 

        messages = ChatMessage.objects.filter(
            Q(sender=user_id) | Q(reciever=user_id)
        ).order_by("-id")
        
        return messages
    

class GetMessages(generics.ListAPIView):
    serializer_class = MessageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        sender_id = self.kwargs['sender_id']
        reciever_id = self.kwargs['reciever_id']
        messages = ChatMessage.objects.filter(sender__in=[sender_id, reciever_id], reciever__in=[sender_id, reciever_id])
        return messages

    
# class SendMessages(generics.CreateAPIView):
#     serializer_class = MessageSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated] 

class SendMessages(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        clicked_id = int(self.request.query_params.get('id'))
        user_id = CustomUser.objects.get(id=clicked_id)
        print(clicked_id)

        user = self.request.user
        message = self.request.data.get('message')
        serializer.save(user=user, sender=user, reciever=user_id, message=message)
    
    def get_queryset(self):
        clicked_id = int(self.request.query_params.get('id'))
        gst = CustomUser.objects.get(id=clicked_id)
        user = self.request.user
        queryset = ChatMessage.objects.filter(
            Q(sender__id=gst.id, reciever=user) | Q(sender=user, reciever__id=gst.id)
        ).distinct()
        return queryset
    



class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated] 

class SearchUser(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def list(self, request, *args, **kwargs):
        username = request.query_params.get('username', '')
        logged_in_user = request.user

        users = CustomUser.objects.filter(
            Q(username__icontains=username) |
            Q(first_name__icontains=username) |
            Q(last_name__icontains=username) |
            Q(email__icontains=username)
        ).exclude(id=logged_in_user.id)

        if not users.exists():
            return Response(
                {"detail": "No users found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
    

class SearchItem(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def list(self, request, *args, **kwargs):
        title = request.query_params.get('title', '')
        # logged_in_user = request.user

        items = Item.objects.filter(
            Q(title__icontains=title) |
            Q(description__icontains=title) |
            Q(location__icontains=title)
        )

        if not items.exists():
            return Response(
                {"detail": "No items found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)
    





# firebase authentification
def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate (username=username,password = password1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Bad Authenticate')
            return redirect('signin')
    return render(request, 'app/signin.html')

def signout(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('signin')
    return render(request, 'app/signout.html')


# get an mines update for last 7 days
class UpdatesViewSet(viewsets.ModelViewSet):
    queryset = MiningTrends.objects.all()
    serializer_class = MiningTrendsSerializer1



from .serializers import LocalCostWithDayLabelSerializer
from collections import defaultdict

class SevenDayMiningViewSet(generics.ListAPIView):
    serializer_class = LocalCostWithDayLabelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        today = timezone.now().date()  # Use date() to strip the time part
        seven_days_ago = today - timedelta(days=7)

        # Fetch records from the last 7 days with the title "Gold"
        records = MiningTrends.objects.filter(period__gte=seven_days_ago, mine_name__name="Gold").order_by('period')

        # Initialize a dictionary to store local_cost for each day
        day_costs = defaultdict(lambda: 0)

        # Populate the dictionary with the actual data
        for record in records:
            delta = (today - record.period).days
            day_label = f"Day {7 - delta}"
            day_costs[day_label] = record.local_cost

        # Create a list of data for the past 7 days
        result = []
        for i in range(7):
            day_label = f"Day {7 - i}"
            result.append({'local_cost': day_costs[day_label], 'day_label': day_label})

        return result
    

class PremiumView(viewsets.ModelViewSet):
    queryset = PremiumModel.objects.all()
    serializer_class = PremiumSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        is_premium = self.request.data.get('is_premium')
        serializer.save(user=user, is_premium=is_premium)