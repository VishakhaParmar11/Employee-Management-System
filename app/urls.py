from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.EmployeeInsertPage,name="emppage"),
    path("insertpage/",views.InsertEmpData,name="insertpage"),
    path("displaydata/",views.ShowEmployeeData,name="displaydata"),
    path("editpage/<int:pk>",views.EditPage,name="editpage"),
    path("updateinfo/<int:pk>",views.UpdateInfo,name="updateinfo"),
    path("deletedata/<int:pk>",views.DeleteData,name="deletedata"),
]