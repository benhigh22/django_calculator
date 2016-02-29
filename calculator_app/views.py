from django.shortcuts import render


def index_view(request):
    if request.method == "POST":
        answer=0
        first_number = float(request.POST.get('first_number'))
        operator = request.POST.get('operator')
        second_number = float(request.POST.get('second_number'))

        if first_number and second_number:
            if operator == "+":
                answer = (first_number + second_number)

            elif operator == "-":
                answer = (first_number - second_number)

            elif operator == "*":
                answer = (first_number * second_number)

            elif operator == "/":
                answer = (first_number / second_number)

        return render(request, 'index_view.html', {'answer': answer})
    else:
        return render(request, 'index_view.html')