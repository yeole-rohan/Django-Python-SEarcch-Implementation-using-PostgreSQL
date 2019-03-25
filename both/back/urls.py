from django.urls import path
from .views import home\
	#address

urlpatterns = [
	path('home/', home, name='home'),
	# path('address/',address, name = 'address')
]
