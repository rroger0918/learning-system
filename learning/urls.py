from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^$',views.home),   
    url(r'^register/',views.register),
    url(r'^login/',views.User_login),
    url(r'^personal/',views.personal),
    url(r'^logout/',views.User_logout),
    url(r'^reset',views.reset_password),   
    url(r'^coursestart/',views.coursestart),
    url(r'^class1/',views.class1), 
    url(r'^lesson0/',views.lesson0),
    url(r'^lesson1_1/',views.lesson_1),
    url(r'^lesson1_2/',views.lesson_2),
    url(r'^lesson1_3/',views.lesson_3),
    url(r'^lesson2_1/',views.lesson_4),
    url(r'^lesson2_2/',views.lesson_5),
    url(r'^lesson2_3/',views.lesson_6),
    url(r'^lesson2_4/',views.lesson_7),
    url(r'^lesson2_5/',views.lesson_8),
    url(r'^lesson3_1/',views.lesson_9),
    url(r'^lesson3_2/',views.lesson_10),
    url(r'^lesson3_3/',views.lesson_11),
    url(r'^lesson3_4/',views.lesson_12),
    url(r'^lesson3_5/',views.lesson_16),
    url(r'^lesson4_1/',views.lesson_13),
    url(r'^lesson4_2/',views.lesson_14),
    url(r'^lesson4_3/',views.lesson_15),



    

	# url(r'^post2/$', views.post2), #資料新增，資料作驗證

	# url(r'^delete/(\d+)/$', views.delete),
	
	# url(r'^edit/(\d+)/$', views.edit), # 由 瀏覽器 開啟
	# url(r'^edit/(\d+)/(\w+)$', views.edit), # 由 edit.html 按 送出 鈕

	# url(r'^edit2/(\d+)/(\w+)$', views.edit2),
	# url(r'^postform/$', views.postform), # 表單驗證
  
  

  

]




