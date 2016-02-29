from django.shortcuts import render


def index_view(request):
    try:
        if request.method == "POST":
            answer=0
            operator = request.POST.get('operator')
            first_number = float(request.POST.get('first_number'))
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

            return render(request, 'index_view.html', {'answer': answer, 'first_number': first_number,
                                                       'second_number': second_number, 'operator': operator})
        else:
            return render(request, 'index_view.html')
    except (ValueError, TypeError):
        answer = "Sorry, your input must be numbers. Try again."
        return render(request, 'index_view.html', {'answer': answer})
