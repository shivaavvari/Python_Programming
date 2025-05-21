from fpdf import FPDF, XPos, YPos
from pathlib import Path
import cv2
from PIL import Image


class PDF(FPDF):
    def header(self):
        self.image(r'D:\inligntech\Generate_PDF_with_Python\image.jpg', 10, 8, 33)
        self.set_font("helvetica", 'B', 16)
        self.cell(80)
        self.cell(90, 10, "Python Programming Projects", border=1, align="C")
        self.ln(40)  # line break

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", 'I', 16)
        self.cell(0, 10, f"Page {self.page_no()} / {{nb}} ", align="C")

    def chapter_title(self, num, label):
        self.set_font("helvetica", 'B', 16)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, f"Chapter {num}:{label}", 0,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L", fill=True)
        self.ln(10)

    def file_contents(self, file):
        self.set_font("helvetica", 'I', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, f"Files :{file}", 0,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        self.ln(10)

    def chapter_image(self, image):

        self.image(image, keep_aspect_ratio=True, dims=(450, 450))
        self.set_font("helvetica", 'I', 16)
        self.cell(0, 10, f"Image :{image}", 0,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(10)
    def chapter_image2(self, image,file):

        self.image(image, keep_aspect_ratio=True, dims=(450, 450))
        self.set_font("helvetica", 'I', 16)
        self.cell(0, 10, f"Image :{file}", 0,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(10)


    def chapter_body(self, body):
        self.set_font("helvetica", 'I', 16)
        self.multi_cell(0, 10, body)
        self.ln(10)


pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.write(10, "Python Programming Projects \n", wrapmode="WORD")
pdf.write(10, "A. Shiva Kiran \n", wrapmode="WORD")
pdf.write(10, "inligntech \n", wrapmode="WORD")


pdf.add_page()
pdf.write(10, "List of Projects \n", wrapmode="WORD")
pdf.set_font("helvetica", 'B', 16)
pth = Path('D://inligntech')
count = 1
for dir in pth.iterdir():
    if dir.is_dir() and dir.name != '.git':
        pdf.chapter_title(count, dir.name)

        for file in dir.iterdir():
            if file.is_file() and file.name.endswith('.py'):
                pdf.file_contents(file.name)
        count += 1
list_of_dirs = [dir.name for dir in pth.iterdir()if dir.is_dir()
                and dir.name != '.git']
pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(1, list_of_dirs[0])
Description = """This is the project description.
The basic idea of this project is to convert text into audio file
"""

pdf.chapter_body(Description)
pdf.chapter_image(r'D:\inligntech\AudiotoText\demo_tkinter.PNG')
Libraries = """
The libraries used in this project are:
1. gTTS
2. os
3. tkinter

The gTTS library is used to convert text into audio file.
The os library is used to play the audio file.
The tkinter library is used to create the GUI for the project.
"""
pdf.chapter_body(Libraries)
code1 = """
1)The code used in this project is:
from gtts import gTTS
import os 


text="LOL this is really funny"
output = gTTS(text=text,lang="en",slow=False)
output.save('output.mp3')

os.system("start output.mp3")

"""
pdf.chapter_body(code1)

explanation = """
This code is used to convert the text file into audio file.
The text is read and stored in the variable text."""
pdf.chapter_body(explanation)


code2 = """
2)The code used in this project is:
from gtts import gTTS
import os

text =open("demo.txt","r",encoding="utf-8").read()
language="hi"
output =gTTS(text,lang=language,slow=False)
output.save('fileoutput.mp3')
os.system('start fileoutput.mp3')
"""

pdf.chapter_body(code2)
explanation = """
This code is used to convert the text file into audio file.
The text file is opened in read mode and the content is read and 
stored in the variable text.
"""

pdf.chapter_body(explanation)

code3 = """
3)The code used in this project is:
from gtts import gTTS
import os
from tkinter import *



root = Tk()
canvas = Canvas(root,width=400,height=400)
canvas.pack()

def textToSpeech():
    text = entry.get()
    language="en"
    output = gTTS(text=text,lang=language,slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")


entry = Entry(root)
canvas.create_window(200,180,window=entry)
button = Button(text="Start",command=textToSpeech )
canvas.create_window(200,230,window=button)

root.mainloop()
"""
pdf.chapter_body(code3)
explanation3 = """
This code is used to convert the text file into audio file.
the text is read from the entry box and a text to speech function 
is used to convert the text into audio file.  
"""
pdf.chapter_body(explanation3)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(2, list_of_dirs[1])

pdf.chapter_image(
    r'D:\inligntech\Building_RestAPI_Django_python_framework\movieapi.PNG')
pdf.chapter_image(
    r'D:\inligntech\Building_RestAPI_Django_python_framework\api_admin.PNG')

Description = """
This is the project description.
Building_RestAPI_Django_python_framework . 
This is the backend for the React Frontend.
The basic idea of this project is to create a REST API using Django Rest Framework.
The Django Rest Framework is a powerful toolkit for building Web APIs.  
Please install the required libraries using the command:
pip install -r requirements.txt

1)create a Django project
django-admin startproject mysite
2)create a myapp
django-admin startapp myapp
3)Register the movie app in the settings.py file
4)create a movie model
from django.db import models
# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.name
    images = models.ImageField(upload_to = 'Images',
                default="Images/None/sampleImg.jpg")
    name = models.CharField(max_length=100)
    description= models.CharField(max_length=200)
    ratings = models.FloatField()

5)Register the movie model in the admin.py file
from django.contrib import admin
from .models import Movie
# Register your models here.
admin.site.register(Movie)
6)create a movieapi
7)Register the movieapi app in the settings.py file
8)create a movieapi serializer 
from myapp.models import Movie
from rest_framework import serializers 

class MovieSerializer(serializers.ModelSerializer):
    images = serializers.ImageField(max_length = None, use_url=True)
    class Meta:
        model = Movie
        fields =['name','description','ratings','images']
9) create the urls.py for the movieapi app
from django.contrib import admin
from django.urls import path, include
from .views import MovieAPIView,MovieDetail
urlpatterns = [
   path('',MovieAPIView.as_view()),
   path('<int:pk>',MovieDetail.as_view()),
]
10)create the views.py for the movieapi app
from django.shortcuts import render
from rest_framework import generics
from myapp.models import Movie
from .serializers import MovieSerializer
# Create your views here.
class MovieAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
11)your installed apps should look like this:
INSTALLED_APPS = [
    'corsheaders',
    'movieapi',
    'rest_framework',
    'myapp',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
12)your middleware should look like this:
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
13) your CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://localhost:8000',
    
) 
14)setup th media root in the settings.py file
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
15)setup the static root in the settings.py file
STATIC_URL = '/static/'
15)your urls.py file should look like this:
from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path('movieapi/',include('movieapi.urls'))
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

We can run the server using the command:
python manage.py runserver
16)The server will run on the port 8000
17)The API will be available at the following URL:
http://localhost:8000/movieapi/
Now we can create a react frontend for this API.
it will consume the API and display the data in a user friendly way.    
18)The react frontend will be available at the following URL:
http://localhost:3000/

"""
pdf.chapter_image(
    r'D:\inligntech\Building_RestAPI_Django_python_framework\movie_detail.PNG')

pdf.chapter_body(Description)
Libraries = """The libraries used in this project are:
asgiref
Django
django-cors-headers
djangorestframework
pillow
sqlparse
tzdata

The asgiref library is used to run the Django server.
The Django library is used to create the Django project.
The django-cors-headers library is used to allow cross-origin requests.
The djangorestframework library is used to create the REST API.
The pillow library is used to create the images.
The sqlparse library is used to parse the SQL queries.
The tzdata library is used to set the timezone.

"""
pdf.chapter_body(Libraries)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(3, list_of_dirs[2])
pdf.chapter_image(
    r'D:\inligntech\Building_RestAPI_React_Frontend\start_node.PNG')
pdf.chapter_image(
    r'D:\inligntech\Building_RestAPI_React_Frontend\start_node1.PNG')
pdf.chapter_image(
    r'D:\inligntech\Building_RestAPI_React_Frontend\react_frontend.PNG')

Description = """this is the project description
we have created a react frontend for the Django Rest API.
The react frontend is created using the create-react-app command.
we did yarn install to install the required libraries.
we can start the app using the command:
yarn start
The app will run on the port 3000.
The API will be available at the following URL:
http://localhost:3000
In the src folder of the myapp react app 
we have created a file called App.js
The code in the App.js file is as follows:  

import logo from './logo.svg';
import './App.css';

import React from 'react';
import axios  from 'axios';



class App extends React.Component {
  state= {
    movies: [],
  };
  componentDidMount(){

    this.getMovies()
  }
  getMovies()
  {
    axios
    .get("http://localhost:8000/movieapi/")
    .then((res)=>{this.setState({movies: res.data})})
    .catch((error)=> {console.log(error);});
  }
  
  render(){
    return (
    <div className="App">
     {this.state.movies.map((movie)=>(

      <div key={movie.id}>
        <img src={movie.images}></img>
        <h1>{movie.name}</h1>
        <h2>{movie.description}</h2>
        <h3>{movie.ratings}</h3>
        
      </div>

     ))}
    </div>
  );
}
}
export default App;

we importes the axios library to make the API calls.
we created a class called App and in the constructor 
we created a state called movies.
we created a function called getMovies 
which will make the API call to the Django Rest API.

the styling for the react app is done using the App.css file.
The code in the App.css file is as follows: 
.App {
  text-align: center;
}

.App-logo {
  height: 40vmin;
  pointer-events: none;
}

@media (prefers-reduced-motion: no-preference) {
  .App-logo {
    animation: App-logo-spin infinite 20s linear;
  }
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
}

@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}


"""

pdf.chapter_body(Description)
Libraries = """The libraries used in this project are:

1)react
2)axios

react is used to create the react app.
axios is used to make the API calls.
"""
pdf.chapter_body(Libraries)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(4, list_of_dirs[3])
Description = """This is the project description.
The basic idea of this project is to create a calculator using tkinter.
"""
pdf.chapter_body(Description)
pdf.chapter_image(r'D:\inligntech\Calculator_Tkinter\calculator.PNG')
code = """ The code used in this project is:

from tkinter import *
import ast

root = Tk()
i=0
def get_number(num):
    global i
    display.insert(i, num)
    i+=1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length

def clear_all():
    display.delete(0,END)

def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string,mode='eval')
        result = eval(compile(node,"<string>",mode='eval'))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def undo():
    entire_string = display.get()
    if len(entire_string)>0:
        entire_string = entire_string[:-1]
        clear_all()
        display.insert(0,entire_string)
    else:
        clear_all()
        display.insert(0,"Error")

display =Entry(root)
display.grid(row=1,columnspan=6)
numbers = [ 1,2,3,4,5,6,7,8,9]
counter =0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root,text=button_text,width=3,
                        height=2, command = lambda text=button_text: get_number(text))    
        button.grid(row=x+2,column=y)
        counter +=1

button =Button(root,text=0,width=3,height=2, command= lambda : get_number(0))
button.grid(row=5,column=1)


count=0
operations = ['+', '-', '*', '/','*3.14',"%","(","**", ")","**2"]
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root,text=operations[count],
                            width=3,height=2,
                            command= lambda text=operations[count]: get_operation(text))
            count +=1
            button.grid(row=x+2,column=y+3)
        
button =Button(root,text="AC",width=3,
                height=2,command=clear_all).grid(row=5,column=0)
button =Button(root,text="=",width=3,
                height=2,command=calculate).grid(row=5,column=2)
button =Button(root,text="<-",width=3,
                height=2,command=undo).grid(row=5,column=4)



root.mainloop()

"""
pdf.chapter_body(code)
explanation = """This code is used to create a calculator using tkinter.
The tkinter library is used to create the GUI for the project.
The ast library is used to parse the expression and evaluate it.
The eval function is used to evaluate the expression.
The get_number function is used to get the number 
    from the button and insert it in the entry box.
The get_operation function is used to get the 
    operation from the button and insert it in the entry box.
The clear_all function is used to clear the entry box.
The calculate function is used to evaluate the expression 
    and display the result in the entry box.
The undo function is used to delete the last character from the entry box.
"""
pdf.chapter_body(explanation)

Libraries = """The libraries used in this project are:
1)tkinter
2)ast

The tkinter library is used to create the GUI for the project.
The ast library is used to parse the expression and evaluate it.

"""
pdf.chapter_body(Libraries)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(5, list_of_dirs[4])

pdf.chapter_image(
    r'D:\inligntech\Chat_app_Socket_Networking_programming\cs_tool.PNG')
Description = """This is the project description.
We have created a simple chat application using socket programming.
The client will send the message to the server 
    and the server will send the message to all the clients.
we create the server using the socket library.
we created a simple chat application using tkinter.


"""

pdf.chapter_body(Description)
code = """The code used in this project is:
server.py

import socket
from tkinter import *


s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.connect((HOST_NAME,PORT))

def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0,END)
    s.send(bytes(message, "utf-8"))
    receive(listbox)

def receive(listbox):
    message_from_server = s.recv(50)
    listbox.insert('end',"Server  :" + message_from_server.decode('utf-8'))




root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()


button = Button(root,text="Send",command=lambda :send(listbox,entry))
button.pack(side=BOTTOM)

rbutton = Button(root,text="Receive",command=lambda :receive(listbox))
rbutton.pack(side=BOTTOM)
root.title("client")

root.mainloop()

"""

Description = """
This code is used to create a simple chat application using socket programming.    

"""
pdf.chapter_body(code)
pdf.chapter_body(Description)

code2 = """The code used in this project is:
client.py
import socket
from tkinter import *


s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.connect((HOST_NAME,PORT))

def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0,END)
    s.send(bytes(message, "utf-8"))
    receive(listbox)

def receive(listbox):
    message_from_server = s.recv(50)
    listbox.insert('end',"Server  :" + message_from_server.decode('utf-8'))




root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()


button = Button(root,text="Send",command=lambda :send(listbox,entry))
button.pack(side=BOTTOM)

rbutton = Button(root,text="Receive",command=lambda :receive(listbox))
rbutton.pack(side=BOTTOM)
root.title("client")

root.mainloop()

"""
Description = """This code is used to create a 
simple chat application using socket programming.
The client will send the message to the server 
and the server will send the message to all the clients.
"""
pdf.chapter_body(code2)
pdf.chapter_body(Description)

code_layout = """The layout of the app is as follows:
from tkinter import *
import socket

root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root,text="Send",command=lambda :send(listbox,entry))
button.pack(side=BOTTOM)

rbutton = Button(root,text="Receive",command=lambda :receive(listbox))
rbutton.pack(side=BOTTOM)
root.mainloop()

"""



Description = """
This code is used to create a simple chat application using socket programming.
The client will send the message to the server and 
the server will send the message to all the clients.
"""
pdf.chapter_body(code_layout)
pdf.chapter_body(Description)

Libraries = """The libraries used in this project are:
1)socket
2)tkinter
The socket library is used to create the server and client.
The tkinter library is used to create the GUI for the project.
"""
pdf.chapter_body(Libraries)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(6, list_of_dirs[5])
pdf.chapter_image(r'D:\inligntech\Compress\compress.PNG')

Description = """This is the project description.   
The basic idea of this project is to compress and decompress the files.
The compress_file function is used to compress the file.
The decompress_file function is used to decompress the file.
"""
pdf.chapter_body(Description)

code = """The code used in this project is:
import zlib, base64 

def compress_file(input_file, output_file):
    data =  open(input_file, "r").read()
    data_bytes = bytes(data,'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(output_file, "w")
    compressed_file.write(decoded_data)
    compressed_file.close()

def decompress_file(input_file, output_file):
    compressed_data = open(input_file, "r").read()
    data_bytes = compressed_data.encode('utf-8')
    compressed_data = base64.b64decode(data_bytes)
    decompressed_data = zlib.decompress(compressed_data)
    decompressed_file = open(output_file, "w")
    decompressed_file.write(decompressed_data.decode('utf-8'))
    decompressed_file.close()


"""

pdf.chapter_body(code)
Description = """This code is used to compress and decompress the files.
The compress_file function is used to compress the file.
The decompress_file function is used to decompress the file.
"""
pdf.chapter_body(Description)
Description = """create a gui for the project using tkinter."""
pdf.chapter_body(Description)
code2 = """The code used in this project is:
import tkinter as tk
from compressmodule import compress_file, decompress_file

def compression(input_file, output_file):
    compress_file(input_file, output_file)
    
def decompression(input_file, output_file):
    decompress_file(input_file, output_file)


window = tk.Tk()
window.title("Compression Enginge")
window.geometry("400x300")


input_entry = tk.Entry(window)
output_entry = tk.Entry(window)
input_label = tk.Label(window, text="File to be Compressed")
ouput_label = tk.Label(window, text="Name of the Compressed File")
compressed_button = tk.Button(window, 
                              text="Compress",
                              command=lambda : compression(input_entry.get(), output_entry.get()))
compressed_label = tk.Label(window,text="File to be DeCompressed")
compressed_entry = tk.Entry(window)
decompressed_label = tk.Label(window,text="Name of the  DeCompressed File")
decompressed_entry = tk.Entry(window)
decompressed_button = tk.Button(window, text="DeCompress",
                                command=lambda : decompression(compressed_entry.get(), decompressed_entry.get()))

input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
ouput_label.grid(row=1, column=0)
output_entry.grid(row=1, column=1)
compressed_button.grid(row=2,column=1)
compressed_label.grid(row=3, column=0)
compressed_entry.grid(row=3, column=1)
decompressed_label.grid(row=4, column=0)
decompressed_entry.grid(row=4, column=1)
decompressed_button.grid(row=5,column=1)

window.mainloop()


"""
pdf.chapter_body(code2)
Description = """ gui with filedialog"""
code3 = """The code used in this project is:
import tkinter as tk
from compressmodule import compress_file, decompress_file
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", 
                                          filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    return filename 
    


def compression(input_file, output_file):
    compress_file(input_file, output_file)
    
def decompression(input_file, output_file):
    decompress_file(input_file, output_file)


window = tk.Tk()
window.title("Compression Enginge")
window.geometry("400x300")



compressed_button = tk.Button(window, text="Compress",command=lambda : compression(open_file(), "compress_ouput1.txt"))
decompressed_button = tk.Button(window, text="DeCompress",command=lambda : decompression(open_file(), "decompress_output1.txt"))

compressed_button.grid(row=2,column=1)
decompressed_button.grid(row=5,column=1)

window.mainloop()


"""
pdf.chapter_body(Description)
pdf.chapter_body(code3)


libraries = """The libraries used in this project are:
1)zlib
2)base64
3)tkinter
4)compressmodule
The zlib library is used to compress and decompress the files.
The base64 library is used to encode and decode the data.
The tkinter library is used to create the GUI for the project.
"""

pdf.chapter_body(libraries)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(7, list_of_dirs[6])

Description = """This is the project description.
The basic idea of this project is to create a credit card validator.
The code is used to validate the credit card number.
"""
pdf.chapter_body(Description)
code = """The code used in this project is:
card_no ="5610591081018250"
number = list(card_no)
odd_sum=0
double_list=[]
for (idx, val)  in enumerate(number):
    if idx % 2 != 0:
       odd_sum += int(val)    
    else:   
        double_list.append(int(val)*2)
double_string =""    
for x in double_list:
    double_string += str(x)
#converting a string to a list 
double_list = list(double_string)    
even_sum=0
for x in double_list:
    even_sum += int(x)
net_sum = odd_sum + even_sum  
if net_sum % 10 == 0:
    print("Valid card")
else:   
    print("Invalid card")   
"""

pdf.chapter_body(code)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(8, list_of_dirs[7])
pdf.chapter_image(r'D:\inligntech\CRUD_Commandline\crud.PNG')

Description = """This is the project description.
The basic idea of this project is to create a CRUD application using command line.
The code is used to create a CRUD application using command line.
The code is used to create a database and perform the CRUD operations on the database.
"""
pdf.chapter_body(Description)
code = """The code used in this project is:
import json 
import os 

def create_user():
    while True:
        
        if  os.path.exists("data.json"):
            add_user = input("Do you want to add a user? (yes/no): ")
            if add_user.lower() == "yes":
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                city = input("Enter your city: ")
                data = {"name": name,   
                        "age": age,
                        "city": city}
                
                with open("data.json", 'r') as file:
                        present_data = json.load(file)
                present_data.append(data)
                with open("data.json", "w") as file:
                    json.dump(present_data, file)

                print("User created successfully")
                print("The updated data is: ")  
                print(present_data)
            else:
                print("User not created")
                with open("data.json", 'r') as file:
                        present_data = json.load(file)
                print(present_data)
                break
        else:
            print("File does not exist")    
def update_user():
    while True:
        if os.path.exists("data.json"):
            with open("data.json", 'r') as file:
                present_data = json.load(file)
            print("The present data is: ")
            print(present_data)
            update_user = input("Do you want to update a user? (yes/no): ")
            if update_user.lower() == "yes":
                name = input("Enter the name of the user you want to update: ")
                for i in present_data:
                    if i["name"] == name:
                        i["age"] = int(input("Enter the new age: "))
                        i["city"] = input("Enter the new city: ")
                        with open("data.json", "w") as file:
                            json.dump(present_data, file)
                        print("User updated successfully")
                        print("The updated data is: ")  
                        print(present_data)
                        break
               
            else:
                print("User not found")
                break
        else:
            print("File does not exist")
            break

def delete_user():
    while True:
        if os.path.exists("data.json"):
            with open("data.json", 'r') as file:
                present_data = json.load(file)
            print("The present data is: ")
            print(present_data)
            delete_user = input("Do you want to delete a user? (yes/no): ")
            if delete_user.lower() == "yes":
                name = input("Enter the name of the user you want to delete: ")
                for i in present_data:
                    if i["name"] == name:
                        present_data.remove(i)
                        with open("data.json", "w") as file:
                            json.dump(present_data, file)
                        print("User deleted successfully")
                        print("The updated data is: ")  
                        print(present_data)
                        break
            else:
                print("User not found")
                break
        else:
            print("File does not exist")
            break

def read_user():
    while True:
        if os.path.exists("data.json"):
            with open("data.json", 'r') as file:
                present_data = json.load(file)  
            print("The present data is: ")
            print(present_data) 
            break
        else:    
            print("File does not exist")
            break

def user_management():
    try:
        while True:
            print("1. Create user")
            print("2. Update user")
            print("3. Delete user")
            print("4. Read user")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                create_user()
            elif choice == 2:
                update_user()
            elif choice == 3:
                delete_user()
            elif choice == 4:
                read_user()
            elif choice == 5:
                break
            else:
                print("Invalid choice") 
    except ValueError:
        print("Invalid input")

user_management()



"""
pdf.chapter_body(code)
libraries = """The libraries used in this project are:
1)json
2)os
The json library is used to create the json file.
The os library is used to create the file.  

"""
pdf.chapter_body(libraries)

Description = """This is the project description.
we can create, update, delete and read the user data command line.
we saved the data in a json file.
"""
pdf.chapter_body(Description)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(9, list_of_dirs[8])
pdf.chapter_image(
    r'D:\inligntech\CRUD_Databases_Student_management_system\crud_mysql.PNG')

pdf.chapter_image(
    r'D:\inligntech\CRUD_Databases_Student_management_system\crud_mssqlserver.PNG')
pdf.chapter_image(
    r'D:\inligntech\CRUD_Databases_Student_management_system\crud_mssqlserver_tkinter.PNG')
pdf.chapter_image(
    r'D:\inligntech\CRUD_Databases_Student_management_system\crud_mysql_tkinter.PNG')


Description = """This is the project description.
The basic idea of this project is to create a CRUD application using mysql and mssqlserver. 
"""
pdf.chapter_body(Description)
code = """
The code used for connecting mysqldb is:
import MySQLdb

def create_table():
  db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
  cursor =db.cursor()
  cursor.execute("create table students(id int primary key AUTO_INCREMENT,name varchar(100),address varchar(500),age int,number int);")
  print("Table created successfully")
  db.commit()
  db.close()

def insert_data():
    name=input("Enter name:")
    address=input("Enter address:")
    age=input("Enter age:")
    number = input("Enter number:")
    db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
    cursor =db.cursor()
    cursor.execute("Insert into   students(name ,address ,age ,number) values(%s,%s,%s,%s)",(name,address,age,number))
    print("data added successfully")
    db.commit()
    db.close()

def update_data():
    db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
    cursor =db.cursor()
    student_id =input("Please enter the student_id to be updated?")
    fields = {
        "1":("name","Please enter the new name?"),
        "2":("address","Please enter the new address"),
        "3":("age","Please enter the new age"),
        "4":("number","Please enter the new number"),

    }

    for keys in fields:
        print(f"{keys} : {fields[keys][0]}")
        
    
    selected_choice = input("Enter the selection to be updated")
    
    if selected_choice in fields:
      field_choice, prompt = fields[selected_choice][0],fields[selected_choice][1]
      new_choice = input(prompt)

      sql =f"update students set {field_choice}=%s where id =%s"
      cursor.execute(sql,(new_choice,student_id))
      print(f"{field_choice} updated successfully")
    else:
      print("invalid field choice ")  
       
    db.commit()
    db.close()

def delete_data():
    db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
    cursor =db.cursor()
    
    student_id = input("Enter id of the student to be deleted:")
    cursor.execute("select *  from  students where id=%s ",(student_id,))
    
    student =cursor.fetchone()
    
    if student:
        print(f"Student to be deleted: ID {student[0]},Name: {student[1]}, Address= {student[2]}, Number ={student[3]} ")
        choice = input("Do you want to delete the student (yes/no)")
        if choice.lower()=="yes":
            cursor.execute("delete from students where id=%s",(student_id,))
            print("Data updated succesfully")
       
            

        else:
            print("Deletion cancelled") 
            
    else:         
        print("data not updated")
    
    db.commit()
    db.close()
    
    

def read_data():
    
    db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
    cursor =db.cursor()
    cursor.execute("select * from students;")
    result = cursor.fetchall()
   

    for student in result:
        print(f" ID {student[0]},Name: {student[1]}, Address= {student[2]}, Number ={student[3]} ")
     
    print("data printed   successfully")
    db.commit()  
    db.close()    
while True:
    print("welcome to the Student database management system")
    print("1. Create a Table") 
    print("2. Insert the data")
    print("3. Read the data")
    print("4. Update the data")   
    print("5. Delete the data")
    print("6. Exit the system")

    choice = input("Enter your choice (1-6)")
    if choice =="1":
        create_table()
    elif choice =="2":
        insert_data()
    elif choice =="3":
        read_data()
    elif choice =="4":
        update_data()
    elif choice =="5":
        delete_data()
    elif choice =="6":
        break
    else:
        print("Enter a valid choice")        

2) The code used for connecting mssqlserver is:
import pyodbc

def create_table():
    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    cursor.execute("create table students(id int identity(1,1) primary key,name varchar(100),address varchar(500),age int,number int);")
    print("Table created  successfully")
    cursor.commit()  
    conn.close()    

def insert_data():
    name=   input("Enter name:")
    address=input("Enter address:")
    age=    input("Enter age:")
    number= input("Enter number:")

    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    cursor.execute("Insert into   students(name ,address ,age ,number) values(?,?,?,?)",(name,address,age,number))
    print("data added   successfully")
    cursor.commit()  
    conn.close()    

def read_data():
    
    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    cursor.execute("select * from students;")
    result = cursor.fetchall()
   

    for student in result:
        print(f" ID {student[0]},Name: {student[1]}, Address= {student[2]}, Number ={student[3]} ")
     
    print("data printed   successfully")
    cursor.commit()  
    conn.close()    


def update_data():
    
    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    
    student_id = input("Enter id of the student to be updated:")
    fields = {

        "1":['name','Please enter the new name'],
        "2":['address','Please enter the new address'],
        "3":['age','Please enter the new age'],
        "4":['number','Please enter the new number'],
    }
    
    print("Enter the field you want to update")
    for key in fields:
        print(f" {key}:{fields[key][0]}")

    field_choice = input("Enter the field you want to update:")
    if field_choice in fields:
        field_name,prompt = fields[field_choice]
        new_value = input(prompt)
        sql = f"update students set {field_name}=? where id=? "
        cursor.execute(sql,(new_value,student_id))
        print(f"{field_name} update successfully")
    else:
        print("Invalid field choice")    
    cursor.commit()  
    conn.close()    

def delete_data():
   
    
    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    student_id = input("Enter id of the student to be deleted:")
    cursor.execute("select *  from  students where id=? ",(student_id,))
    
    student =cursor.fetchone()
    
    if student:
        print(f"Student to be deleted: ID {student[0]},Name: {student[1]}, Address= {student[2]}, Number ={student[3]} ")
        choice = input("Do you want to delete the student (yes/no)")
        if choice.lower()=="yes":
            cursor.execute("delete from students where id=?",(student_id,))
            print("Data updated succesfully")
            cursor.commit()  
            conn.close()    

        else:
            print("Deletion cancelled")
            conn.close()    
   
    else:         
        print("data not updated")
        conn.close()
    
   
while True:
    print("welcome to the Student database management system")
    print("1. Create a Table") 
    print("2. Insert the data")
    print("3. Read the data")
    print("4. Update the data")   
    print("5. Delete the data")
    print("6. Exit the system")

    choice = input("Enter your choice (1-6)")
    if choice =="1":
        create_table()
    elif choice =="2":
        insert_data()
    elif choice =="3":
        read_data()
    elif choice =="4":
        update_data()
    elif choice =="5":
        delete_data()
    elif choice =="6":
        break
    else:
        print("Enter a valid choice")            

"""
pdf.chapter_body(code)

Description = """
To create a GUI for the project we used tkinter.
The code is used to create a GUI for the project.
1) The code used for connecting mysqldb is:
from  tkinter  import *
import MySQLdb
from tkinter import ttk # for label frame , treeframe, Tree
from tkinter import messagebox


def run_query(query,parameters=()):
    db =MySQLdb.connect(
      user="root",
      password="shiva",
      database="mysqldb4")
    cursor =db.cursor()
    cursor.execute(query,parameters)
   
    query_result = []
    try:
        if query.lower().startswith("select"):
            query_result =cursor.fetchall()
            return query_result
            db.commit()        
        else:
            db.commit()    
    except Exception as e:
        messagebox.showerror("Database error",str(e))
    finally:
        cursor.close()
        db.close()


def refresh_treeview():
    
    for item in tree.get_children():
        tree.delete(item)
    records = run_query("select * from students;",)

    for record in records:
        tree.insert("",END,values=record)

def insert_data():
    query ="insert into students(name,address,age,number) values(%s,%s,%s,%s);"
    parameters = (name_entry.get(),address_entry.get(),age_entry.get(),phone_entry.get())
    run_query(query,parameters)
    messagebox.showinfo("information","the students info is updated")
    refresh_treeview()

def delete_data():
    selected_item = tree.selection()[0]
    id=tree.item(selected_item)['values'][0]
    query ="Delete  from students  where id=%s"
    parameters = (id,)
    run_query(query,parameters)
    messagebox.showinfo("information","the students info is deleted")
    refresh_treeview()

def update_data():
    selected_item = tree.selection()[0]
    id=tree.item(selected_item)['values'][0]
    query ="update students set name=%s, address=%s, age=%s,number=%s where id=%s"
    parameters = (name_entry.get(),address_entry.get(),age_entry.get(),phone_entry.get(),id)
    
    run_query(query,parameters)
    messagebox.showinfo("information","the students info is Updated")
    refresh_treeview()


def create_table():

    query ="create table if not exists students(id int primary key auto_increment, name varchar(30), address varchar(50),age int, number int);"
    parameters = ()
    run_query(query,parameters)
    messagebox.showinfo("information","the students table exists")
    refresh_treeview()


root = Tk()
root.title("Student Management System")

label_frame = LabelFrame(root,text="Students")
label_frame.grid(row=0, column=0,padx=10,pady=10)
Label(label_frame,text="Name :").grid(row=0,column=0,padx=5,pady=5)

name_entry = Entry(label_frame)
name_entry.grid(row=0,column=1,pady=10)
Label(label_frame,text="address :").grid(row=1,column=0,padx=5,pady=5)

address_entry = Entry(label_frame)
address_entry.grid(row=1,column=1,pady=10)
Label(label_frame,text="Age :").grid(row=2,column=0,padx=5,pady=5)


age_entry = Entry(label_frame)
age_entry.grid(row=2,column=1,pady=10)
Label(label_frame,text="Phone number :").grid(row=3,column=0,padx=5,pady=5)


phone_entry = Entry(label_frame)
phone_entry.grid(row=3,column=1,pady=10)

function_frame= Frame(root)
function_frame.grid(row=1,column=0,pady=5,padx=5)
Button(function_frame,text="Create Table",command=create_table).grid(row=0,column=0,pady=10,padx=5)
Button(function_frame,text="Insert Table",command=insert_data).grid(row=0,column=1,pady=10,padx=5)
Button(function_frame,text="Update Table",command=update_data).grid(row=0,column=2,pady=10,padx=5)
Button(function_frame,text="Delete Table",command=delete_data).grid(row=0,column=3,pady=10,padx=5)

tree_frame =Frame(root)
tree_frame.grid(row=2,column=0,pady=5,padx=5)
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)
tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set, selectmode="browse")

tree.pack()
tree_scroll.config(command=tree.yview)

tree['columns'] = ('id','name','address','age','number')
tree.column("#0",width=0,stretch=NO)
tree.column("id",anchor=CENTER,width=80)
tree.column("name",anchor=CENTER,width=120)
tree.column("address",anchor=CENTER,width=80)
tree.column("age",anchor=CENTER,width=80)
tree.column("number",anchor=CENTER,width=120)

tree.heading("id",text="ID",anchor=CENTER)
tree.heading("name",text="Name",anchor=CENTER)
tree.heading("address",text="Address",anchor=CENTER)
tree.heading("age",text="age",anchor=CENTER)
tree.heading("number",text="Phone number",anchor=CENTER)


refresh_treeview()


root.mainloop()


2) The code used for connecting mssqlserver in a tkinter app is:

from tkinter import * 
from tkinter import ttk
import pyodbc
from tkinter import messagebox



def run_query(query,parameters=()):
    conn= pyodbc.connect(Trusted_connection='yes',driver='{sql server}',server='DESKTOP-3RB0IMS\SQLEXPRESS',database='master')   
    cursor = conn.cursor()
    query_result = None
    try:
        cursor.execute(query,parameters)
        if query.lower().startswith("select"):
            query_result = cursor.fetchall()
            return query_result
        conn.commit()
    except Exception as e:
        messagebox.showerror("Database Error",str(e))
    finally:
        cursor.close()
        conn.close()    
def refresh_treeview():
    for item in tree.get_children():
        tree.delete(item)
    records = run_query("select * from students",)
    for record in records:
        
        tree.insert('',END,values=list(record))

def insert_data():
    query =   "Insert into   students(name ,address ,age ,number) values(?,?,?,?)"
    parameters = (name_entry.get(),address_entry.get(),age_entry.get(),phone_entry.get())
    run_query(query,parameters)
    messagebox.showinfo("Information","Data inserted successfuly")
    refresh_treeview()


def delete_data():
    selected_item = tree.selection()[0]
    id = tree.item(selected_item)['values'][0]
    query="delete from students where id =?"
    parameters=(id,)
    run_query(query,parameters)
    messagebox.showinfo("Information","Data deleted successfuly")
    refresh_treeview()

def update_data():
    selected_item = tree.selection()[0]
    id = tree.item(selected_item)['values'][0]
    query = "update students set name=?, address=?, age=?, number=? where id =?"
    parameters = (name_entry.get(),address_entry.get(),age_entry.get(),phone_entry.get(),id)
    run_query(query,parameters)
     
    messagebox.showinfo("Information","Data updated successfuly")
    refresh_treeview()
def create_table():
    query = "if not exists (select * from sysobjects where name='students' and xtype='U') create table students(id int identity(1,1) primary key,name varchar(100),address varchar(500),age int,number int);"
    run_query(query)
    messagebox.showinfo("information","Table created  successfully")
    refresh_treeview()
root = Tk()
root.title("Student Management system")

frame=LabelFrame(root,text="Student Data")
frame.grid(row=0,column=0,padx=10,pady=10,sticky="ew")

Label(frame,text="Name: ").grid(row=0,column=0,padx=2,sticky="ew")
name_entry = Entry(frame)
name_entry.grid(row=0, column =1 , pady=2,stick="ew")
Label(frame,text="Address: ").grid(row=1,column=0,padx=2,sticky="ew")
address_entry = Entry(frame)
address_entry.grid(row=1, column =1 , pady=2,stick="ew")
Label(frame,text="Age: ").grid(row=2,column=0,padx=2,sticky="ew")
age_entry = Entry(frame)
age_entry.grid(row=2, column =1 , pady=2,stick="ew")
Label(frame,text="Phone number: ").grid(row=3,column=0,padx=2,sticky="ew")
phone_entry = Entry(frame)
phone_entry.grid(row=3, column =1 , pady=2,stick="ew")

button_frame =Frame(root)
button_frame.grid(row=1,column=0,pady=5,sticky="ew")

Button(button_frame, text="Create Table",command=create_table).grid(row=0,column=0,padx=5)
Button(button_frame, text="Add data ",command=insert_data).grid(row=0,column=1,padx=5)

Button(button_frame, text="Update data",command=update_data).grid(row=0,column=2,padx=5)
Button(button_frame, text="Delete data",command=delete_data).grid(row=0,column=3,padx=5)

tree_frame = Frame(root)
tree_frame.grid(row=2,column=0,padx=10,sticky="nsew")

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
tree.pack()
tree_scroll.config(command = tree.yview)

tree['columns'] =("id","name","address", "age","number")
tree.column("#0",width=0,stretch=NO)
tree.column("id",anchor=CENTER,width=80)
tree.column("name",anchor=CENTER,width=120)
tree.column("address",anchor=CENTER,width=120)
tree.column("age",anchor=CENTER,width=80)
tree.column("number",anchor=CENTER,width=120)


tree.heading("id",text="ID",anchor=CENTER)
tree.heading("name",text="Name",anchor=CENTER)
tree.heading("address",text="Address",anchor=CENTER)
tree.heading("age",text="Age",anchor=CENTER)
tree.heading("number",text="Phone number",anchor=CENTER)


refresh_treeview()
root.mainloop()
"""
pdf.chapter_body(code)

libraries = """The libraries used in this project are:
1)pyodbc
2)tkinter
3)ttk
4)MySQLdb
5)os

The pyodbc library is used to connect to the mssqlserver.
The tkinter library is used to create the GUI for the project.
The ttk library is used to create the treeview for the project.
The MySQLdb library is used to connect to the mysql database.
The os library is used to create the file.  
"""
pdf.chapter_body(libraries)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(10, list_of_dirs[9])
pdf.chapter_image(r'D:\inligntech\CRUD_pyqt6\crud_pyqt6.PNG')

Description = """This is the project description.
The basic idea of this project is to create a CRUD application using pyqt6.
"""

pdf.chapter_body(Description)

code = """The code used in this project is:
from PyQt6.QtWidgets  import  QVBoxLayout,QMenu,QMessageBox,QToolBar,QPushButton,QSpinBox,QLineEdit,QFormLayout,QMainWindow, QDockWidget,QWidget, QApplication,QLabel,QTableWidget,QTableWidgetItem, QListWidget,QHBoxLayout, QListWidgetItem
from PyQt6.QtGui import QPixmap ,QAction,QIcon 
from PyQt6.QtCore import Qt ,QSize 
import sys
import warnings
import sqlite3
warnings.filterwarnings("ignore", category=DeprecationWarning)
#CRUD, create, read , update , delete
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("products.db")
        self.create_table()
        self.initUI()

    def load_data(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM  products')
        products = cursor.fetchall()
        self.table_widget.setRowCount(len(products))
        for row, product in enumerate(products):
            for column, value in enumerate(product):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, column,item) 
       
        
        
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(""
                        CREATE TABLE IF NOT EXISTS products ( \
                        id INTEGER PRIMARY KEY AUTOINCREMENT,\
                        name TEXT,\
                        price INTEGER,\
                        description TEXT) \
                       "")
        self.conn.commit()        
        
    def initUI(self):
        self.setGeometry(0,0,700,500)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.table_widget = QTableWidget(self)

        layout.addWidget(self.table_widget)

        
        self.table_widget.setColumnCount(4)

        self.table_widget.setHorizontalHeaderLabels(["ID","NAME","PRICE","DESCRIPTION"])


        #
        self.load_data()

        self.name_edit = QLineEdit(self)
        self.price_edit = QLineEdit(self)
        self.description_edit = QLineEdit(self)

        layout.addWidget(QLabel("Name :"))
        layout.addWidget(self.name_edit)

        layout.addWidget(QLabel("Price :"))
        layout.addWidget(self.price_edit)
        
        layout.addWidget(QLabel("Description :"))
        layout.addWidget(self.description_edit)

        
        add_button = QPushButton("Add Product",self)
        layout.addWidget(add_button)
        add_button.clicked.connect(self.add_product)

        delete_button = QPushButton("Delete Product",self)
        layout.addWidget(delete_button)
        delete_button.clicked.connect(self.delete_product)

        update_button = QPushButton("Update Product",self)
        layout.addWidget(update_button)
        update_button.clicked.connect(self.update_product)



    def add_product(self):
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()
        #new_product = {
        #   'name':name,'price':price,'description':description
        #
        #self.products.append(new_product)
        ##creating the table
        #row_position = len(self.products)-1 
        #self.table_widget.insertRow(row_position)
        #for col,value in enumerate(new_product.values()):
        #    item = QTableWidgetItem(str(value))
        #    self.table_widget.setItem(row_position,col,item)
        # Adding new product to the database 
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO products(name , price , description) VALUES(?,?,?)',(name,price,description))
        self.conn.commit()     
        self.load_data()

        self.name_edit.clear()
        self.price_edit.clear()
        self.description_edit.clear()



    def delete_product(self):
        current_row = self.table_widget.currentRow()
        if current_row<0 or current_row>= self.table_widget.rowCount():
            return QMessageBox.warning("Warning","No row Selected")
        product_id = self.table_widget.item(current_row,0).text()   
        response = QMessageBox.question(self,"Delete Product","Do you want to delete the product",QMessageBox.StandardButton.Yes |QMessageBox.StandardButton.No)
        if response == QMessageBox.StandardButton.Yes:
            #self.table_widget.removeRow(current_row)
            #del self.products[current_row]
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM products where id = ?',(product_id))
            self.conn.commit()     
            self.load_data()


    def update_product(self):
        current_row = self.table_widget.currentRow()
        if current_row<0 or current_row>= self.table_widget.rowCount():
            return QMessageBox.warning("Warning","No row Selected")
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()
        product_id = self.table_widget.item(current_row,0).text()   
        cursor = self.conn.cursor()
        cursor.execute('UPDATE products  SET name=?, price=?, description=? WHERE id=?',(name,price,description,product_id))
        self.conn.commit()     
        self.load_data()

      # updated_product = {
      #     'name':name,'price':price,'description':description
      # }
      # self.products[current_row] = updated_product
      # for col,value in enumerate(updated_product.values()):
      #     item = QTableWidgetItem(str(value))
      #     self.table_widget.setItem(current_row,col,item)




    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
"""
pdf.chapter_body(code)
libraries = """The libraries used in this project are:
1)PyQt6.QtWidgets
2)PyQt6.Qtcore
3)PyQt6.QtCore
4)sqlite3
The PyQt6 library is used to create the GUI for the project.
The sqlite3 library is used to create the database for the project.
The PyQt6.QtWidgets library is used to create the widgets for the project.
The PyQt6.QtCore library is used to create the core functionality for the project.
"""

pdf.chapter_body(libraries)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(11, list_of_dirs[10])
pdf.chapter_image(r'D:\inligntech\Custom_Color_Picker\color_picker.PNG')

Description = """This is the project description.
The basic idea of this project is to create a color picker using python.
"""

code = """The code used in this project is:
from PyQt6.QtWidgets  import QColorDialog,QMainWindow, QWidget, QApplication,QSlider, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QAction,QColor
from PyQt6.QtCore import Qt

import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
 
        self.setGeometry(0,0,700,500)
        self.red_slider = QSlider(Qt.Orientation.Horizontal)
        self.green_slider = QSlider(Qt.Orientation.Horizontal)
        self.blue_slider = QSlider(Qt.Orientation.Horizontal)

        for slider in [self.red_slider,self.green_slider,self.blue_slider]:
             slider.setRange(0,255)
             slider.setValue(255)
             slider.setTickPosition(QSlider.TickPosition.TicksBelow)
             slider.setTickInterval(25)


        self.red_label = QLabel("Red: ")

        self.green_label = QLabel("Green: ")

        self.blue_label = QLabel("Blue: ")

        self.red_value_label = QLabel("255")
        
        self.green_value_label = QLabel("255") 
        
        self.blue_value_label = QLabel("255")
        
        
        

        #creating a layout for main window
        layout = QVBoxLayout(self)
        
        sliders_layout = QVBoxLayout() 
        for label, slider, value_label in zip([self.red_label,self.green_label,self.blue_label],
                 [self.red_slider,self.green_slider,self.blue_slider],
                 [self.red_value_label,self.green_value_label,self.blue_value_label]
                       ):
                slider_layout = QHBoxLayout()
                slider_layout.addWidget(label)
                slider_layout.addWidget(slider)
                slider_layout.addWidget(value_label)
                sliders_layout.addLayout(slider_layout)
        
        
        layout.addLayout(sliders_layout)
        # creating a label to preview colors
        self.color_preview = QLabel()
        color_layout = QVBoxLayout()
        color_layout.addWidget(self.color_preview)
        color_layout.addStretch()
        layout.addLayout(color_layout)

        # connecting sliders to the methods
        self.red_slider.valueChanged.connect(self.update_color)
        self.green_slider.valueChanged.connect(self.update_color)
        self.blue_slider.valueChanged.connect(self.update_color)
        
        #Setting the initial value of Color
        self.color="#ffffff"
        self.color_preview.setStyleSheet(f"background-color:{self.color}")
        
        
        
        self.final_color_label= QLabel("Final Color: #ffffff")
        final_color_layout = QHBoxLayout()
        final_color_layout.addWidget(self.final_color_label)
        layout.addLayout(final_color_layout)
        
    def update_color(self):
        red = self.red_slider.value()
        self.red_value_label.setText(str(red))
        green = self.green_slider.value()
        self.green_value_label.setText(str(green))
        blue = self.blue_slider.value()
        self.blue_value_label.setText(str(blue))
        self.color = QColor(red,green,blue)
        self.color_preview.setStyleSheet(f"background-color:{self.color.name()}")
        self.final_color_label.setText(str(self.color.name()))
                 
    def show_color_dialog(self,event):
        print("Method triggered")
        if event.button() == Qt.MouseButton.LeftButton:
            color_dialog =QColorDialog(self.color,self)
            color_dialog.colorSelected.connect(self.set_color)
            color_dialog.exec()
    def set_color(self,color):
        self.color = color
        self.red_slider.value(color.red)
        self.green_slider.value(color.green)
        self.blue_slider.value(color.blue)
        self.update_color()


app = QApplication(sys.argv)

window = Window()
window.show()
app.exec()
"""

pdf.chapter_body(code)
libraries = """The libraries used in this project are:
1)PyQt6.QtWidgets
2)PyQt6.QtCore
3)PyQt6.QtGui
4)sys
5)os
The PyQt6 library is used to create the GUI for the project.
The sys library is used to create the system for the project.
The os library is used to create the file.  
"""

pdf.chapter_body(libraries)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(12, list_of_dirs[11])
pdf.chapter_image(r'D:\inligntech\CvGenerator_app\cvgenerator.PNG')


Description = """This is the project description.
The basic idea of this project is to create a CV generator using python.
the project is used to create a CV using the information provided by the user.
We build a tkinter application
"""
pdf.chapter_body(Description)
code = """The code used in this project is:
from tkinter import *
import pyqrcode
from fpdf import FPDF
from tkinter import messagebox


class PDFCV(FPDF):  
    def header(self):
        self.image("mywebsite.png", 10, 8, 33, title="Portfolio Site")
    
    def footer(self):
        pass
    def generate_cv(self,name,email,phone_number,address,skills,work_experience,education,about_me):
        self.add_page()
        self.ln(20)        
        
        #display name 
        self.set_font("helvetica","B", size=26)
        self.cell(0,10,name, new_x='LMARGIN', new_y="NEXT", align='C')
        
        #Adding contact information 
        self.set_font("helvetica","B", size=12)
        self.cell(0,10,"Contact Information", new_x='LMARGIN', new_y="NEXT", align='L')
        
        
        self.set_font("helvetica","B", size=10)
        self.cell(0,10,"Email : {}".format(email), new_x='LMARGIN', new_y="NEXT", )
        self.cell(0,10,"Phone : {}".format(phone_number), new_x='LMARGIN', new_y="NEXT", )
        self.cell(0,10,"Address : {}".format(address), new_x='LMARGIN', new_y="NEXT", )
        
        #display skills 
        self.ln(20)        
        self.set_font("helvetica","B", size=12)
        self.cell(0,10,"Skills", new_x='LMARGIN', new_y="NEXT", align='L')
        
        self.set_font("helvetica","B", size=10)
        for skill in skills:
            self.cell(0,5,"- {}".format(skill), new_x='LMARGIN', new_y="NEXT" )

        #display experience
        self.ln(20)        
        self.set_font("helvetica","B", size=12)
        self.cell(0,10,"Experience", new_x='LMARGIN', new_y="NEXT", align='L')
        
        self.set_font("helvetica","B", size=10)
        
        for experience in work_experience:
            self.cell(0,5,"{} : {}".format(experience['title'],experience['description']), new_x='LMARGIN', new_y="NEXT" )

        #display education
        self.ln(20)        
        self.set_font("helvetica","B", size=12)
        self.cell(0,10,"Education", new_x='LMARGIN', new_y="NEXT", align='L')
        
        self.set_font("helvetica","B", size=10)
      
        for education_item in education:
            self.cell(0,5,"{} : {}".format(education_item['degree'],education_item['university']), new_x='LMARGIN', new_y="NEXT" )
        
        
        #display about me
        self.ln(20)        
        self.set_font("helvetica","B", size=12)
        self.cell(0,10,"About Me", new_x='LMARGIN', new_y="NEXT", align='L')
        
        self.set_font("helvetica","B", size=10)
      
        self.multi_cell(0,5,about_me)


        self.output("cv.pdf")

        

def generate_cv_pdf():
    name = entry_name.get()
    email = entry_email.get()   
    phone_number = entry_phone.get()
    address = entry_address.get()
    website = entry_website.get()
    skills =entry_skills.get("1.0",END).strip().split("\n")
    work_experience =[]
    education = []

    work_experience_lines =entry_experience.get("1.0",END).strip().split("\n")
    for line in work_experience_lines:
        title , description = line.split(":")
        work_experience.append({"title": title.strip(), "description" : description.strip()})   
    print(work_experience)
    education_lines = entry_education.get("1.0",END).strip().split("\n")
    for line  in education_lines:
        degree , university = line.split(":")
        education.append({"degree": degree.strip(), "university" : university.strip()})

    about_me =entry_about_me.get("1.0",END)
    # create QR code 
    qrcode = pyqrcode.create(website)
    qrcode.png("mywebsite.png", scale=6)

    if not name or not email or not phone_number or not address  \
        or not website or not education or not work_experience or not skills:
        messagebox.showerror("Error", "Please fill all fields")
        return
    cv = PDFCV()
    cv.generate_cv(name,email,phone_number,address,skills,work_experience,education,about_me)


    
window = Tk()
window.title("CV Generator")

label_name = Label(window, text="Name: ")
label_name.pack()

entry_name = Entry(window)
entry_name.pack()

label_email = Label(window, text="Email: ")
label_email.pack()

entry_email = Entry(window)
entry_email.pack()

label_phone = Label(window, text="Phone: ")
label_phone.pack()

entry_phone = Entry(window)
entry_phone.pack()

label_address = Label(window, text="Address: ")
label_address.pack()

entry_address = Entry(window)
entry_address.pack()

label_website = Label(window, text="Website: ")
label_website.pack()

entry_website = Entry(window)
entry_website.pack()

label_skills = Label(window,text="Skills Enter a skill per line")
label_skills.pack() 
entry_skills = Text(window, height=5) 
entry_skills.pack() 

label_education = Label(window,text="Education (Enter one  per line Degree)")
label_education.pack() 
entry_education = Text(window, height=5) 
entry_education.pack() 

label_experience = Label(window,text="Work Experience (Enter one  per line in format)")
label_experience.pack() 
entry_experience = Text(window, height=5) 
entry_experience.pack() 


label_about_me = Label(window,text="About ME ")
label_about_me.pack() 
entry_about_me = Text(window, height=5) 
entry_about_me.pack() 

button_generate = Button(window, text="Generate CV", command=generate_cv_pdf)
button_generate.pack()

window.mainloop()

"""
pdf.chapter_body(code)

libraries = """The libraries used in this project are:
1)tkinter
2)pyqrcode
3)fpdf
4)os
5)sys
The tkinter library is used to create the GUI for the project.
The pyqrcode library is used to create the QR code for the project.
The fpdf library is used to create the PDF for the project.
The os library is used to create the file.
The sys library is used to create the system for the project.
"""
pdf.chapter_body(libraries)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(13, list_of_dirs[12])
for file in Path(r'D:\inligntech\Data Analysis Project\pdf').iterdir():
    if file.is_file() and file.suffix == ".jpg":
        pdf.chapter_image2(file,file.stem)


pdf.output("Sample.pdf")
