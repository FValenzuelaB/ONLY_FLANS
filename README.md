# ONLY_FLANS

Para gestionar imagenes en un proyecto se debe:

1. pip install pillow

2. En settings agregar:
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

3. En urls.py del proyecto agregar:
if settings.DEBUG:
from django.conf import settings
from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)