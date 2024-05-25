from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome")
def contact(request):
    return HttpResponse("contact")

def home(request):
    return render(request,'home.html',{'name':'nitesh'})

def expression(request):
    textarea = request.GET['textarea']
    val = request.GET['text']
    if val=='info':
        return render(request,'home.html',{'title':'Information','result':textarea})

    elif val=='count':
        data = textarea.split()
        length = len(data)
        return render(request,'home.html',{'title':'Word Count','result':length})
    elif val=='frequency':
        dict1 = {}
        data = textarea.split()
        for i in data:
            count = data.count(i)
            dict1[i]=count
        return render(request,'home.html',{'title':'Word Count Frequency','result':dict1})    
    elif val=='upper':
        data = textarea.upper()
        return render(request,'home.html',{'title':'Upper Case','result':data})
    elif val=='punctuation':
        list1 = ""
        for i in textarea:
            if i !=',' and i !='?' and i!='[' and i!=']' and i!='}' and i!='{' and i!='.' and i!='/' and i!='\\' and i!='%' and i!='$':
                list1 = list1+i
            
        return render(request,'show_result.html',{'title':'Remove Punctuation','result':list1})            
    elif val=='space':
        textarea.strip()
        return render(request,'show_result.html',{'title':'Remove Extra Space','result':textarea})





