from website.models import reviews
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a review'

    def handle(self, *args, **kwargs):

        name = [
            'JOSEPH VIJAY',
            'TRISHA KRISHNAN',
            'VJ SIDDHU'
        ]

        img_url = [
            'https://th.bing.com/th/id/OIP.zJFA3xA5mT_0X2TYQNGbswHaJ4?rs=1&pid=ImgDetMain',
            'https://th.bing.com/th/id/OIP.hIzY_afZZ0ZYmVG46Px8-gHaNK?rs=1&pid=ImgDetMain',
            'https://www.filmibeat.com/img/popcorn/profile_photos/vj-siddhu-20190614104016-44416.jpg'
        ]

        review = [
            "The best ice cream I've ever had! Their chocolate fudge brownie is absolutely divine. The service is always friendly and the place is super clean.",
            "I love this place! The ice cream is amazing and the service is always top notch. The staff is always friendly and the place is always clean.",
            "I absolutely love this place! The ice cream is delicious and the service is super friendly. The staff is always there to help and the place is always clean."
        ]
        position =[
            'Regulat Customer',
            'Ice Cream Enthusiast',
            'Verified Customer'
        ]

        for name,img_url,review,position in zip(name,img_url,review,position):
            reviews.objects.create(name=name,img_url=img_url,review=review,position=position)
        self.stdout.write(self.style.SUCCESS('Successfully created review'))
        