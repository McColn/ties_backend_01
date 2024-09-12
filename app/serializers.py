# serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate, update_session_auth_hash
from .models import ( Item, CustomUser, Investments, FrontPageInfo, 
                     InvestmentCompliance, ConsultationCompliance, Order, 
                     OrderItem, Category, MiningTrends, Message,Profile, 
                     ChatMessage, Comment, Post, ConsultancyTiesCategory, 
                     ConsultancyTiesDetails, PremiumModel 
                     )
from django.contrib.auth.hashers import check_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    image = serializers.ImageField(allow_null=True, required=False) 

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name','role','phone','image')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email','first_name', 'last_name','image')

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        user = self.context['request'].user
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        # Check if the old password is correct
        if not user.check_password(old_password):
            raise serializers.ValidationError({'old_password': 'Incorrect old password.'})

        # Check if new password and confirm password match
        if new_password != confirm_password:
            raise serializers.ValidationError({'confirm_password': 'New password and confirm password do not match.'})

        return data

    def save(self):
        user = self.context['request'].user
        new_password = self.validated_data['new_password']
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(self.context['request'], user)


class InvestmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = [
                    'id','projectName','owner','resources',
                    'resourcesSummary','areaCovered','licenceType','licenceNumber',
                    'physicalLocation','mapLocation','image','levelInvestment',
                    'projectStatus','studiesDone','modeOfInvestment','contact','attachments'
                  ]

class FrontPageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontPageInfo
        fields = ['id','image','body']

class InvestmentComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentCompliance
        fields = '__all__'

class ConsultationComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationCompliance
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Item
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    price = serializers.ReadOnlyField(source='item.price')
    item_name = serializers.ReadOnlyField(source='item.title')
    image = serializers.ReadOnlyField(source='item.image.url')

    class Meta:
        model = OrderItem
        fields = ['id','user', 'item', 'quantity', 'price', 'item_name', 'image']


class MiningTrendsSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='mine_name.name')
    class Meta:
        model = MiningTrends
        fields = ['mine_name','local_cost','international_cost','title','period']


class SMSMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'





class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content','created_at']

class PostSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True, read_only=True)
    # author = UserSerializer(many=False)
    author_image = serializers.ReadOnlyField(source='author.image')

    class Meta:
        model = Post
        fields = ['id', 'content', 'author','author_image','created_at','image']


class ConsultancyTiesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultancyTiesCategory
        fields = '__all__'

class ConsultancyTiesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultancyTiesDetails
        fields = '__all__'



# ##########################################################

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [ 'id',  'user',  'full_name' ]

class MessageSerializer(serializers.ModelSerializer):
    reciever_profile = ProfileSerializer(read_only=True)
    sender_profile = ProfileSerializer(read_only=True)
    reciever_name = serializers.ReadOnlyField(source='reciever.username')
    sender_name = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = ChatMessage
        fields = ['id','sender', 'reciever', 'reciever_profile', 'sender_profile' ,'message', 'is_read', 'date','reciever_name','sender_name']


class MiningTrendsSerializer1(serializers.ModelSerializer):
    class Meta:
        model = MiningTrends
        fields = ['local_cost','period']


from datetime import datetime, timedelta

class LocalCostWithDayLabelSerializer(serializers.Serializer):
    local_cost = serializers.FloatField()
    day_label = serializers.CharField()


class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumModel
        fields = ['user','is_premium']