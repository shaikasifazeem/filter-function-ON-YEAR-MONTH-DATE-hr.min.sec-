from django.shortcuts import render

# Create your views here.

def insert_student(request):
    # # d={'data':'hello this is new page for fillter'}
    # import datetime
    # t=datetime.datetime.now()
    # d={'t':t}

    import datetime
    t=datetime.datetime.now()
    d={'data':'hai this is FILTER functions '}
    d={'data':'HAI HOw aRe YoU','t':t,'c':0}
    d={'t':t}



    

    return render(request,'insert_student.html',d)