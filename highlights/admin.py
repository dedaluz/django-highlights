from django.contrib import admin
from highlights.models import Highlight, HighlightGroup
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

class HighlightInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = Highlight
    fields = ('title', 'position', 'image', 'status', )
    # define the sortable
    sortable_field_name = "position"
    extra = 0

class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {"slug": ("name",)} 
    
    inlines = [HighlightInlineAdmin]

class HighlightAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for FeaturedSlide"""

    def thumbnail(self, obj):
           im = get_thumbnail(obj.image, '60x60', format='PNG', quality=99)
           return u"<img src='%s'>" % im.url
    thumbnail.allow_tags = True
    
    prepopulated_fields = {"slug": ("title",)}   
    list_display = ('title', 'position', 'status', 'thumbnail',)
    pass
        

admin.site.register(HighlightGroup, SliderAdmin)
admin.site.register(Highlight, HighlightAdmin)
