from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def test(request):
    # info={'name':"jayendra",'age':20}
    # return render(request,'index2.html',info)
    return render(request, 'index2.html')

def process(request):
    info_data=request.POST.get('fname')
    return HttpResponse(info_data)


def analyze(request):
    info_text=request.POST.get('text',"dummy")
    remove_punc=request.POST.get('removepunc','off')
    full_caps=request.POST.get('fullcaps','off')
    new_line=request.POST.get('newline','off')
    space_remover=request.POST.get('space','off')
    character_count=request.POST.get('character','off')

    if full_caps=='on':
        result=""
        result=info_text.upper()
        output={'ans':result}
        return render(request,'result.html',output)

    if space_remover=='on':
        result=""
        l1=[]
        for i in range(0,len(info_text)):
            if(info_text[i]!=" "):
                l1.append(info_text[i])
                result=''.join(l1)
        output = {'ans': result}
        return render(request, 'result.html', output)

    if character_count=='on':
        result = 0
        for char in info_text:
            result += 1
        output = {'ans': result}
        return render(request, 'result.html', output)

    if new_line=='on':
        result=""
        l1=[]
        for i in range(0,len(info_text)):
            if(info_text[i]!="\n"):
                l1.append(info_text[i])
                result=''.join(l1)

        output = {'ans': result}
        return render(request, 'result.html', output)

    if remove_punc=='on':
        l2 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '<', '>',
              '?', '/', ':', '.', ";", "'", ',']

        result = ""
        l1 = []
        for i in range(0, len(info_text)):
            if (info_text[i] != " "):
                l1.append(info_text[i])
        for k in range(0, len(info_text)):
            for i in (l2):
                if (i in l1):
                    l1.remove(i)
                result=''.join(l1)
        output = {'ans': result}
        return render(request, 'result.html', output)