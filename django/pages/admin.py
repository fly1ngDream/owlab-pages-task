from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import Page, VersionsThread


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    change_form_template = 'admin/page_change_form.djhtml'

    list_display = ('id', 'title', 'versions_thread', 'version', 'is_current', )
    readonly_fields = ('id', 'versions_thread', 'version', 'is_current', )
    list_filter = ('versions_thread', 'version', 'is_current', )
    search_fields = ('title', )

    def response_change(self, request, obj):
        if "_make-current" in request.POST:
            obj.make_current()
            self.message_user(request, "This page version is current now")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)

@admin.register(VersionsThread)
class VersionsThreadAdmin(admin.ModelAdmin):
    list_display = ('id', )
    readonly_fields = ('id', )
