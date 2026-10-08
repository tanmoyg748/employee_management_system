from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Employee

def employee_list(request: HttpRequest) -> HttpResponse:
    employees = Employee.objects.all()

    return render(
        request,
        "employees/employee_list.html",
        {"employees": employees}
    )

def employee_add(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        salary = request.POST.get("salary")

        Employee.objects.create(
            name=name,
            email=email,
            salary=salary
        )

        return redirect("employee_list")

    return render(
        request,
        "employees/employee_form.html"
    )

def employee_detail(request: HttpRequest, id: int) -> HttpResponse:
    employee = get_object_or_404(Employee, id=id)

    return render(
        request,
        "employees/employee_detail.html",
        {"employee": employee}
    )

def employee_edit(request: HttpRequest, id: int) -> HttpResponse:
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.name = request.POST.get("name")
        employee.email = request.POST.get("email")
        employee.salary = request.POST.get("salary")

        employee.save()

        return redirect("employee_list")

    return render(
        request,
        "employees/employee_edit.html",
        {"employee": employee}
    )

@require_POST
def employee_delete(request: HttpRequest, id: int):
    employee = get_object_or_404(Employee, id=id)

    employee.delete()

    return JsonResponse({
        "success": True,
        "message": "Employee deleted successfully."
    })