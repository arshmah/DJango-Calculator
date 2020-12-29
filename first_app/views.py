
#from django.shortcuts import render
#def add(request):
    #data = {"first_name":"Arshmah", "country":"Pakistan"}
    #return render(request,'cal.html', data)

#def sum(request):
    #ad1 = int(request.GET.get("ad1"))
    #ad2 = int(request.GET.get("ad2"))

    #final = {"result": ad1 + ad2}
    #return render(request,'cal.html',final)

from django.shortcuts import render
from django.http import HttpResponse
#Python code

def index(request):
    return render(request,'index.html')

def calculate(request):
    result = {"ans":''}
    try:

        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2'))
        operator = request.GET.get('operator')
        #result = {"ans": " "}

        if operator == '+':
            result['ans']= num1 + num2
            

        elif operator == '-':
            result['ans'] = num1 - num2
            

        elif operator == '*':
            result['ans'] = num1 * num2

        elif operator == '/':
            result['ans'] = num1 / num2

        elif operator == '//':
            result['ans'] = num1 // num2

        elif operator == '**':
            #num1.append(num1*num1) = num2

            result['ans'] = num1**num2

    except Exception as a:
        result['ans'] = str(a)

    return render(request,'index.html',result)
        
"""def exponent(request):
    results = {'answer': ''}
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    operator = request.GET.get('operator')
    if operator == '**':
        num1.append(num1*num1) = num2
        results['answer'] = num1

    #except Exception as a:
       # result['ans'] = str(a)

    return render(request,'index.html',results)
"""

