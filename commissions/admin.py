from django.contrib import admin
from .models import Product, Commissions

# Register your models here.
class CommissionsAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer_name', 'date', 'media',)
    list_filter = ('product', 'date',)
    search_fields = ('product__name', 'details',)
 
    class Meta:
        model = Commissions
 
 
admin.site.register(Commissions, CommissionsAdmin)
admin.site.register(Product)
