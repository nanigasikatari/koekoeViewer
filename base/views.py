from django.shortcuts import render, get_object_or_404, redirect
from .models import Address
import lxml.html
import requests
from bs4 import BeautifulSoup

def start_page(request):
    return render(request, 'base/start_page.html', {})

def url_list_1(request):
    addresss=Address.objects.filter(star=1)
    return render(request, 'base/url_list_1.html', {'addresss':addresss})

def url_list_2(request):
    addresss=Address.objects.filter(star=2)
    return render(request, 'base/url_list_2.html', {'addresss':addresss})

def url_list_3(request):
    addresss=Address.objects.filter(star=3)
    return render(request, 'base/url_list_3.html', {'addresss':addresss})


def star_shine0(request, url_number):
    address = get_object_or_404(Address, number=url_number)
    address.delete()
    return redirect('star', url_number=url_number)


def star_shine1(request, url_number):
    address = get_object_or_404(Address, number=url_number)
    address.starshine1()
    return redirect('star', url_number=url_number)


def star_shine2(request, url_number):
    address = get_object_or_404(Address, number=url_number)
    address.starshine2()
    return redirect('star', url_number=url_number)


def star_shine3(request, url_number):
    address = get_object_or_404(Address, number=url_number)
    address.starshine3()
    return redirect('star', url_number=url_number)


def star(request, url_number):
    if Address.objects.filter(number=url_number).exists():
        star = get_object_or_404(Address, number=url_number).star
    else :
        star="無し"
    context = {"url_number": url_number,"star":star}
    return render(request, 'base/star.html', context)

def new_star(request, url_number):
    new_star = Address.objects.create(
        url="https://koe-koe.com/detail.php?n="+str(url_number), number=url_number, star=1, title=url_number)
    return redirect('star', url_number=url_number)

def women_list(request,pk) :
    prev_number = pk-1
    next_number = pk+1

    if pk==1 :
        url = "https://koe-koe.com/list.php?g=1&g2=0"
        a=10
    else :
        url="https://koe-koe.com/list.php?g=1&g2=0&p="+str(pk)
        a=11
    response = requests.get(url)
    html = response.text.encode(response.encoding)
    soup = BeautifulSoup(html, "lxml")

    posts=[]
    for list_number in range(0, 10) :
        url_number = soup.find_all("a")[a+list_number*2].get("href")[-6:]
        mp3_url = "http://file.koe-koe.com/sound/upload/" + str(url_number) + ".mp3"

        x = []
        for y in soup.find_all("a")[a+list_number*2].get("title").lstrip("「").rstrip("」の投稿").split("(女性)/"):
            x.append(y)
        contributor = x[0]
        title = x[1]

        link_url = "https://koe-koe.com/" + soup.find_all("a")[a+list_number*2].get("href")
        link_response = requests.get(link_url)
        link_html = link_response.text.encode(link_response.encoding)
        link_soup = BeautifulSoup(link_html, "lxml")

        soup2 = link_soup.find_all("p")[1]
        for script in soup2(["script", "style"]):
            script.decompose()
        text = soup2.get_text()
        lines = [line.strip() for line in text.splitlines()]
        comment = "\n".join(line for line in lines if line)

        post = {"title": title, "contributor": contributor,
                "comment": comment, "mp3_url": mp3_url, "list_number_all": (pk-1)*10+(list_number+1),
                "link_url": link_url, "url_number": url_number}
        posts.append(post)

    context = {"posts": posts, "page_number": pk,
               "prev_number": prev_number, "next_number": next_number}
    return render(request, 'base/women_list.html', context )

def test1(request):
    aaa="aaa"
    bbb="bbb"
    context={"aaa":aaa,"bbb":bbb}
    return render(request, 'base/test1.html', context)

def test2(request,aaa,bbb):
    return render(request, 'base/test2.html', {"aaa": aaa,"bbb":bbb})


def test3(request):
    url = "http://monopocket.jp/blog/html/1091/"
    response = requests.get(url)
    html = response.text.encode(response.encoding)
    soup = BeautifulSoup(html, "lxml")
    title=soup.find_all("p")[1].string
    context = {"title": title}
    return render(request, 'base/test3.html', context)
