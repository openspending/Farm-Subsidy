from django.contrib.gis import admin
from models import Recipient, SchemeType
#
# # class FeedsAdmin(admin.ModelAdmin):
# #   list_display  = ('title','url', 'is_active', 'category',)
# #   list_filter = ('category','is_active',)
# #
# # class FeedItemsAdmin(admin.ModelAdmin):
# #   list_display  = ('title','url', 'tags','feed',)
#
# from treebeard.admin import TreeAdmin
#
# class LocationAdmin(TreeAdmin):
#     prepopulated_fields = {"slug": ("name",)}
#


class RecipientAdmin(admin.ModelAdmin):
    search_fields = ['=globalrecipientid']
    actions = ['remove_from_index']

    def remove_from_index(self, request, queryset):
        from haystack import connections as haystack_connections

        for recipient in queryset:
            for using in haystack_connections.connections_info.keys():
                backend = haystack_connections[using].get_backend()
                backend.remove(recipient)

        self.message_user(request, "Removed from search index")
    remove_from_index.short_description = "Remove from search index"

admin.site.register(Recipient, RecipientAdmin)
admin.site.register(SchemeType)

# # admin.site.register(FeedItems, FeedItemsAdmin)
# # admin.site.register(FeedCategories)
