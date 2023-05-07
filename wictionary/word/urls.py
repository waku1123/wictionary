from rest_framework import routers

from apis import WordViewSet

router = routers.DefaultRouter()
router.register("words", WordViewSet)
