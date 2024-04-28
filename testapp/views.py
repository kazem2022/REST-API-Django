from django.shortcuts import render, redirect
import requests
import json



def student_list(request):
    response = requests.get("http://127.0.0.1:8000/myapp/students_list").json()
    context = {
        "students":response
    }
    return render(request, 'testapp/students_list.html', context=context)

def student_save(request):
    instance = {
        "name": "alllllli",
        "family": "allllllipour",
        "code": "1000003"
    }
    jsondata = json.dumps(instance)
    headers = {'content-type':"application/json"}
    response = requests.post("http://127.0.0.1:8000/myapp/student_save/", data=jsondata, headers=headers)
    if response.status_code == 200:
        # Print the response content if the request was successful
        print(response.json())
    else:
        print('POST request failed with status code:', response.status_code)
    return redirect(student_list)