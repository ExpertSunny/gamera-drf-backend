from django.urls import path, include
from api.views import gameDetails, gameList, tourneyDetails, tourneyList, slideList

urlpatterns = [
    path('games/', gameList, name='games-list'),
    path('games/<int:pk>', gameDetails, name='game-details'),
    path('tourneys/', tourneyList, name='tourney-list'),
    path('slides/', slideList, name='slide-list'),
    path('tourneys/<int:pk>', tourneyDetails, name='tourney-details'),
    # path(r'auth/', include('knox.urls')),
    # path(r'auth/login', LoginAPI.as_view(), name="login"),
    # path(r'auth/logout', knox_views.LogoutView.as_view(), name='logout')
    # path(r'auth/login', LoginAPI.as_view())
]
