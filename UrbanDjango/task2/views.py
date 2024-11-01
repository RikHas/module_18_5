from django.shortcuts import render


# Create your views here.
def class_template(requset):
    return render(requset, 'second_task/class_template.html')


def func_template(requset):
    return render(requset, 'second_task/func_template.html')
