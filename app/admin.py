from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Mine)
admin.site.register(Investments)
admin.site.register(FrontPageInfo)
admin.site.register(InvestmentCompliance)
admin.site.register(ConsultationCompliance)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(MiningTrends)
admin.site.register(ConsultancyTiesCategory)
admin.site.register(ConsultancyTiesDetails)


admin.site.register(Post)
admin.site.register(Comment)



class ChatMessageAdmin(admin.ModelAdmin):
    list_editable = ['is_read', 'message']
    list_display = ['user','sender', 'reciever', 'is_read', 'message']

admin.site.register( ChatMessage,ChatMessageAdmin)
admin.site.register( Profile)
admin.site.register( PremiumModel)
