from django.contrib import admin
from .models import Category, Department, Complaint


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
    )

    search_fields = (
        'name',
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
    )

    search_fields = (
        'name',
    )


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'user',
        'category',
        'department',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'category',
        'department',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
        'address',
        'user__username',
    )

    list_editable = (
        'department',
        'status',
    )

    readonly_fields = (
        'user',
        'created_at',
        'updated_at',
    )

    ordering = (
        '-created_at',
    )