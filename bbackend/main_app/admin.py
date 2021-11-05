from .models import *
from django.contrib import admin


@admin.register(NavigationDisplay)
class NavigationDisplayAdmin(admin.ModelAdmin):
    search_fields = ('description', 'value',)
    list_display = ('description', 'deep', 'value', 'parent', 'text',
                    'set_buttons', 'text_mode', 'content')

    def set_buttons(self, obj):
        return ', '.join([p.name for p in obj.buttons.all()])

    set_buttons.short_description = 'список кнопок'


@admin.register(NavigationButtons)
class NavigationButtonsAdmin(admin.ModelAdmin):
    list_display = ('name', 'action_click_display', 'description', 'value')
    search_fields = ('name', 'value')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', )
    search_fields = ('name',)
    list_filter = ('category',)


@admin.register(ContentCategory)
class ContentCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)
