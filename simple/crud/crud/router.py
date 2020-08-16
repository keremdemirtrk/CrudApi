from simplecrud.viewsets import BookViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('BookModel', BookViewset)
