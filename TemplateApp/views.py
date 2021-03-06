from django.shortcuts import render

# Create your views here.
def index(request):
  val = 'Value!!'
  return render(request,'TemplateApp/index.html',context={'value':'hello','val':val})

def home(request,first_name,last_name):
  my_name = first_name + last_name
  favorites_mangas = ['NARUTO','ONE PIECE','ATTACK ON TAITAN']
  my_info = {
    'name': 'poo3',
    'age': '25'
  }
  status = 20
  return render(request,'TemplateApp/home.html',context={
    'my_name': my_name,
    'favorites_mangas': favorites_mangas,
    'my_info': my_info,
    'status': status
  })

def sample1(request):
  return render(request,"sample1.html")

def sample2(request):
  return render(request,"sample2.html")

def sample(request):
  name = 'yamada ichiro'
  height = 177.5
  weight = 72
  bmi = weight / (height/100)**2
  page_url = 'ホームページ: https://www.google.com'
  favorite_fruits = [
    'Apple','Grape','Lemon'
  ]
  msg = """hello
  my name is
  ichiro
  """
  msg2 = '1234567890'
  return render(request,"sample.html",context={
    'name': name,
    'bmi': bmi,
    'page_url': page_url,
    'fruits': favorite_fruits,
    'msg': msg,
    'msg2': msg2
  })
  
class Country:
  
  def __init__(self,name,population,capital):
    self.name = name
    self.population = population
    self.capital = capital

def sample3(request):
  country = Country('Japan',10000,'Tokyo')
  return render(request,"sample3.html",context={
    'country': country
  })