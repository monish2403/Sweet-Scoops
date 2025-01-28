from django.core.management.base import BaseCommand
from website.models import products

class Command(BaseCommand):
    help = 'distribute a product'

    def handle(self, *args, **kwargs):

        name = [
            'Vannilla Classis',
            'Rich Chololate'
            'Rocky Road',
            'Mint Chocolate Chip',
            'Rocky Road'
        ]
        img_url = [
            'https://images.unsplash.com/photo-1570197571499-166b36435e9f',
            'https://images.unsplash.com/photo-1563805042-7684c019e1cb',
            'https://images.unsplash.com/photo-1574145682253-1f082b650373',
            'https://images.unsplash.com/photo-1567272596258-0c64d7897d89',
            'https://images.unsplash.com/photo-1574145682253-1f082b650373'
        ]
        quantity = [
            500,
            250,
            500,
            250,
            500
        ]
        stock_status = [
            'instock',
            'outofStock',
            'instock',
            'outofstock',
            'instock'
        ]
        price = [
            250,
            180,
            250,
            180,
            250
        ]

        for name,img_url,quantity,stock_status,price in zip(name,img_url,quantity,stock_status,price):
            products.objects.create(name=name,img_url=img_url,quantity=quantity,stock_status=stock_status,price=price)
        self.stdout.write(self.style.SUCCESS('Successfully created product'))