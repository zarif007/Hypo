from django.shortcuts import render,redirect
from django.http import HttpResponse
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
import requests

# Create your views here.
def First(request):
    return render(request,'index.html')

url=''


# ---------------For downloading Notes---------------
def downloadingNotes(request):
    try:
        global url
        url=request.GET.get("url")
        vid=url
        r=requests.get(vid)
        sc=r.text
        title=re.findall("title=\"[^\"]*\"",sc)
        main_title=title[1][7:len(title[1])-1]
        main_title= main_title.replace('|', '')
        print(main_title)
        c=0
        p=0
        id=""
        for i in range(0,len(vid)):
            if(vid[i]=='='):
                p+=1
                break
        if(p!=0):
            for i in range(0,len(vid)):
                if(vid[i]=='='):
                    for k in range(i+1,len(vid)):
                        if(vid!='='):
                            id=id+vid[k]
                        else:
                            c=c+1
                            break
                if(c>0):
                        break
        else:
            id=vid[17:len(vid)]  

        count1=0
        try:
            data=yta.get_transcript(id)

            trascript=' '
            for value in data:
                for key,val in value.items():
                    if key=='text':
                        trascript+=val

            l=trascript.splitlines()
            final="".join(l)
            try:
                file=open("[Script] {}.word".format(main_title),'w')
                file.write(final)
                file.close()
            except:
                file=open("[Script] {}.word".format("Random Tilte"),'w')
                file.write(final)
                file.close()
            count1=1

        except:
            count1=2

        if(count1==1):
            return render(request,'success.html')
        else:
            return render(request,'fail.html')
        

    except:
        return render(request,'fail.html')

    

# -----------Viewing note Downloading site-----------
def downnotes(request):
    return render(request,'downnotes.html')



# ---------------For downloading Audio---------------
def downloadingaudio(request):
    try:
        global url
        url=request.GET.get("url")
        ytd="[Audio] "+YouTube(url).streams.first().download()
        print(ytd)
        count=0
        try:
            YouTube(url).streams.filter(only_audio=True).first().download()
            count=1
        except:
            count=2

        if(count==1):
            return render(request,'success.html')
        else:
            return render(request,'fail.html')
            
    except:
        return render(request,'fail.html')


# -----------Viewing note Downloading site-----------
def downaudio(request):
    return render(request,'downaudio.html')



def downloadingVideo(request):
    try:
        global url
        url=request.GET.get("url")
        ytd="[Video] "+YouTube(url).streams.first().download()
        print(ytd)
        count=0
        try:
            YouTube(url).streams.filter(progressive=True).first().download()
            count=1
        except:
            count=2

        if(count==1):
            return render(request,'success.html')
        else:
            return render(request,'fail.html')
            
    except:
        return render(request,'fail.html')


def downvideo(request):
    return render(request,'downvideo.html')


# ------------returning Home page-------------
def Back2HP(request):
    return redirect('home')