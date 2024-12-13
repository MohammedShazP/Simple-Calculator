from django.shortcuts import render, redirect


# Create your views here.

# Created a function to do the calculations
def calculation(n1, n2, n3, n4, opr):
    result = ""
    try:
        if opr == "addition":
            if len(n3) == 0 and len(n4) == 0:
                result = float(n1) + float(n2)
            elif len(n3) == 0:
                result = float(n1) + float(n2) + float(n4)
            elif len(n4) == 0:
                result = float(n1) + float(n2) + float(n3)
            else:
                result = float(n1) + float(n2) + float(n3) + float(n4)

        elif opr == "subtraction":
            if len(n3) == 0 and len(n4) == 0:
                result = float(n1) - float(n2)
            elif len(n3) == 0:
                result = float(n1) - float(n2) - float(n4)
            elif len(n4) == 0:
                result = float(n1) - float(n2) - float(n3)
            else:
                result = float(n1) - float(n2) - float(n3) - float(n4)
        elif opr == "multiplication":
            if len(n3) == 0 and len(n4) == 0:
                result = float(n1) * float(n2)
            elif len(n3) == 0:
                result = float(n1) * float(n2) * float(n4)
            elif len(n4) == 0:
                result = float(n1) * float(n2) * float(n3)
            else:
                result = float(n1) * float(n2) * float(n3) * float(n4)
        elif opr == "division":
            try:
                if len(n3) == 0 and len(n4) == 0:
                    result = float(n1) / float(n2)
                elif len(n3) == 0:
                    result = float(n1) / float(n2) / float(n4)
                elif len(n4) == 0:
                    result = float(n1) / float(n2) / float(n3)
                else:
                    result = float(n1) / float(n2) / float(n3) / float(n4)
            except ZeroDivisionError as z_error:
                result = "Division using zeros is not allowed."
    except ValueError as v_error:
        result = "Input should be number."

    return result


def home(request):
    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        num3 = request.POST.get("num3")
        num4 = request.POST.get("num4")

        operator = request.POST.get("operator")
        result = calculation(num1, num2, num3, num4, operator)
        context = {"result": result}

        return render(request, "operations/calculate.html", context)

    return render(request, "operations/home.html")
