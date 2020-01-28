from django.urls import path
from slack.views import Listen

urlpatterns=[

    path('listen', Listen.as_view(), name='listen'),
]