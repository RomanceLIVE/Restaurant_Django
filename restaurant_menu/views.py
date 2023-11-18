from django.shortcuts import render
from django.views import generic
from .models import Item, CATEGORY


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")  # the - will reverse the order
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = CATEGORY
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
