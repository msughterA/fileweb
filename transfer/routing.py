from django.urls import re_path
from .consumers import FileReceiveSocket

# counsumer routing pattern would reside here
websocket_urlpatterns = [
    re_path(
        r"ws/filereceive/(?P<userId>[0-9]+)/(?P<deviceId>[0-9]+)/(?P<fileId>[0-9]+)$",
        FileReceiveSocket
        # r"ws/filesend/(?P<userId>[0-9]+)/(?P<deviceId>[0-9]+)/(?P<fileId>[0-9]+)/(?P<pointer>[0-9]+)/$",
    ),
]
