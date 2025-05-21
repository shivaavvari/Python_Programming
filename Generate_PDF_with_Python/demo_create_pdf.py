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

    def chapter_image2(self, image, file):

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


code=""" 
The code used for connecting mysqldb is
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
        pdf.chapter_image2(file, file.stem)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(14, list_of_dirs[13])
pdf.chapter_image(r'D:\inligntech\Django_Booksite\booksite.PNG')
pdf.chapter_image(r'D:\inligntech\Django_Booksite\sqlite.PNG')

Description = """
This is the project description.
The basic idea of this project is to create a book site using django.
The project is used to create a book site using the information provided by the user.
We build a django application
we can add delete and update the book information.

"""
pdf.chapter_body(Description)
requirements = """
The libraries used in this project are:
1)asgiref
2)Django
3)pillow
4)sqlparse
5)tzdata

Asigref is used to create the asgi application for the project.
Django is used to create the web application for the project.
Pillow is used to create the image for the project.
Sqlparse is used to create the sql for the project.
Tzdata is used to create the timezone for the project.

"""
pdf.chapter_body(requirements)

code = """
The code used in this project is:

1) create a django project mysite
django-admin startproject mysite
2) create a django app myapp
python manage.py startapp myapp
3) create the media folder in the project directory to store the images
your settings.py file should look like this:
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL ='/media/'
4) create the static and templates folder in the app directory to 
    store the static files and templates
5)creat the models.py file in the myapp directory
from django.db import models

# Create your models here.
class Book(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    price = models.IntegerField()
    book_image = models.ImageField(default='default.jpg',upload_to='book_images/')
    
5) Register the model in the admin.py file
from django.contrib import admin
from .models import Book
# Register your models here.
admin.site.register(Book)

6)create the forms.py file in the myapp directory
from django import forms
from .models import Book 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =['name','desc','book_image','price']

7)create urls.py file in the myapp directory
from django.urls import path
from  . import  views

app_name = 'myapp'
urlpatterns = [
    path('',views.index,name="index"),
    #path('products/',views.products,name="Products"),
    #book1/2
    path('book/<int:book_id>/',views.detail,name='detail'),
    path('add/',views.add_book,name='add_book'),
    path('update/<int:id>/',views.update,name='update'),
     path('delete/<int:id>/',views.delete,name='delete')
]
8) create the views.py file in the myapp directory

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
# Create your views here.
def index(request):
    book_list = Book.objects.all()
    context={

        'book_list':book_list,
    }
    #return HttpResponse(book_list)
    return render(request,'myapp/index.html',context=context)

def detail(request,book_id):
    book =  Book.objects.get(id= book_id)
    #return HttpResponse("This is the requested book %s"%book_id)
    context={
        'book':book,
    }
    return render(request,'myapp/detail.html',context=context)

def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        
        desc = request.POST.get('desc',)
        
        price = request.POST.get('price',)
        
        book_image = request.FILES['book_image']

        book = Book(name=name,desc=desc,price=price,book_image=book_image)
        book.save()
    
    return render(request,'myapp/add_book.html')

def update(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None,request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'myapp/edit.html',context={'form':form,'book':book})

def delete(request, id):
    if request.method =='POST':
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')

10) create the urls.py file in the mysite directory
from django.contrib import admin
from django.urls import path , include
from . import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    
   
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
11) create the base.html file in the templates directory
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/
    dist/css/bootstrap.min.css" 
    integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" 
    crossorigin="anonymous">
   <link rel="stylesheet" href="{%  static 'myapp/style.css' %}">
    <title>Document</title>
</head>
<body>
   {% block body %}
   
   {% endblock  %}
</body>
</html>

12) run the server
python manage.py runserver

"""
pdf.chapter_body(code)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(15, list_of_dirs[14])
pdf.chapter_image(r'D:\inligntech\Django_todo_app\todo.PNG')
pdf.chapter_image(r'D:\inligntech\Django_todo_app\sqlite.PNG')

Description = """   
This is the project description.
The basic idea of this project is to create a todo app using django.
The project is used to create a todo app using the information provided by the user.
We build a django application
we can add delete and update the todo information.
"""

pdf.chapter_body(Description)
libraries = """The libraries used in this project are:

The libraries used in this project are:
1)asgiref
2)Django
3)sqlparse
4)tzdata

Asigref is used to create the asgi application for the project.
Django is used to create the web application for the project.
Sqlparse is used to create the sql for the project.
Tzdata is used to create the timezone for the project.

"""
pdf.chapter_body(libraries)

code = """
The code used in this project is:
1) Install the requirements
pip install -r requirements.txt
2) create a django project mysite
django-admin startproject mysite
3) create a django app myapp
python manage.py startapp myapp
4)create the static and templates folder in the app directory to 
  store the static files and templates
  static folder should contain the css and js files
5)create the models.py file in the myapp directory
from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    date = models.DateField(default=datetime.date.today())

    
6) Register the model in the admin.py file
from django.contrib import admin
from .models import Task
# Register your models here.
admin.site.register(Task)

7)create the forms.py file in the myapp directory
from .models import Task
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =['name','priority','date']

8)create the views.py file in the myapp directory
from django.shortcuts import render ,redirect
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView 
from django.views.generic.edit import DeleteView 
from django.urls import reverse_lazy

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name  = 'myapp/index.html'
    context_object_name = "task_list"

class TaskDetailView(DetailView):
    model = Task
    template_name  = 'myapp/detail.html'
    context_object_name = "task"

class TaskUpdateView(UpdateView):
    model = Task
    template_name  = 'myapp/update.html'
    context_object_name = "task"
    fields =('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name  = 'myapp/delete.html'
    success_url = reverse_lazy('cbvindex')

    

def index(request):
    task_list = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()
        return redirect('/')
    return render(request,'myapp/index.html',{'task_list':task_list})


def delete(request,taskid):
    task  =Task.objects.get(id =taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'myapp/delete.html',{'task':task})


def update(request,id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance = task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'myapp/edit.html',{'form':form,'task':task})

9)create the urls.py file in the project directory
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('',views.index,name="index"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('cbvindex/',views.TaskListView.as_view(),name='cbvindex'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name="cbvupdate"),
  path('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cbvdelete')
,]

10) After models have been create run the following command
python manage.py makemigrations
python manage.py migrate

11) create the base.html file in the templates directory

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
   <link rel="stylesheet" href="{%  static 'myapp/style.css' %}">
    <title>Document</title>
</head>
<body>
   {% block body %}
   
   {% endblock  %}
</body>
</html>

12) create superuser    
python manage.py createsuperuser

13) run the server

"""

pdf.chapter_body(code)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(16, list_of_dirs[15])
pdf.chapter_image(r'D:\inligntech\Flask-Site\books.PNG')
pdf.chapter_image(r'D:\inligntech\Flask-Site\addbook.PNG')
pdf.chapter_image(r'D:\inligntech\Flask-Site\updatebook.PNG')
pdf.chapter_image(r'D:\inligntech\Flask-Site\flasksite.PNG')
pdf.chapter_image(r'D:\inligntech\Flask-Site\start.PNG')


Description = """
create a flask site using python.
The project is used to create a book site using the information provided by the user.
We build a flask application
we can add delete and update the book information.
"""
pdf.chapter_body(Description)

code = """
1) install the requirements
2) we can start the flask site using the command
python app.py
3)We can add the book using the form provided in the site
4)We can update the book using the form provided in the site
5)We can delete the book using the form provided in the site
6)The data is stored in the sqlite database

7)The code used in this project is:
from flask import Flask ,request, render_template , redirect
from flask_sqlalchemy import SQLAlchemy
import os 

projet_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(projet_dir,"mydatabase.db"))



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db= SQLAlchemy(app)

class Book(db.Model):
    book = db.Column(db.String(100),unique=True,
                     nullable =True, primary_key=True)
    author = db.Column(db.String(100),
                     nullable =False)

@app.route('/updatebooks')
def updatebooks():
    books = Book.query.all()
    return render_template('updatebooks.html',books=books)

@app.route('/update',methods=['POST'])
def update():
    newname = request.form['newbook']
    oldname= request.form['oldbook']
    newauthor = request.form['newauthor']
    book = Book.query.filter_by(book=oldname).first()
    book.book = newname
    book.author = newauthor

    db.session.commit()

    return redirect('/books')


@app.route('/submitbook',methods=['POST'])
def submitbook():
    name = request.form['book']
    author = request.form['author']

    book = Book(book=name,author=author)
    db.session.add(book)
    db.session.commit()
    
    return redirect('/books')

@app.route('/addbook')
def addbook():
        
    return render_template('add_book.html')
@app.route('/delete',methods=['POST'])
def delete():
    book = request.form['oldb']
    book_1 = Book.query.filter_by(book=book).first()     
    db.session.delete(book_1)
    db.session.commit()
    return redirect('/books')
@app.route('/')
def index():
    #return 'this is the request made by th client %s' % request.headers
    return render_template('index.html')   


@app.route('/profile/<username>')
def profile(username):
    
    return render_template('profile.html',username=username, isActive =False)

@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html',books=books)

if __name__ =='__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)


create a base.html file in the templates directory

{% extends 'base.html' %}


    {% block body %}
<form action="/submitbook" method="post">
    <input type="text" name="book">
    <input type="text" name="author">

    <input type="submit">

    

</form>

    
    
    
    {% endblock %}
"""
pdf.chapter_body(code)

libraries = """ The libraries used in this project are:
1)Flask
2)Flask-SQLAlchemy
3)os
4)sqlite3

The Flask library is used to create the web application for the project.
The Flask-SQLAlchemy library is used to create the database for the project.
The os library is used to create the file.
The sqlite3 library is used to create the database for the project.
"""

pdf.chapter_body(libraries)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(17, list_of_dirs[16])
pdf.chapter_image(r'D:\inligntech\FlaskProject_ExpenseManager\expensemanager.PNG')
pdf.chapter_image(r'D:\inligntech\FlaskProject_ExpenseManager\viewexpense.PNG')

Description = """
create a Expense manager using python.
The project is used to create a Expense manager using the 
information provided by the user.
The user can make a list of expenses and can add the expenses to the list.
We build a flask application and the store the data in a sqlite database.
The website is created using bootstrap.
"""

pdf.chapter_body(Description)

libraries = """ The libraries used in this project are:
blinker
click
colorama
Flask
Flask-SQLAlchemy
greenlet
itsdangerous
Jinja2
MarkupSafe
SQLAlchemy
typing_extensions
Werkzeug

The Flask library is used to create the web application for the project.
The Flask-SQLAlchemy library is used to create the database for the project.
The os library is used to create the file.
The sqlite3 library is used to create the database for the project.
"""

pdf.chapter_body(libraries)

code = """
The code used in this project is:
from flask import Flask, render_template, request, redirect ,url_for
from flask_sqlalchemy import SQLAlchemy
import os 

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir,'mydatabase.db')
)



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.String(50),nullable=False)
    expensename = db.Column(db.String(50),nullable=False)
    amount = db.Column(db.Integer,nullable=False)
    category = db.Column(db.String(50),nullable=False)

@app.route('/expenses')
def expenses():
    expenses = Expense.query.all()
    total = 0
    t_business = 0
    t_other =0
    t_food = 0
    t_entertainment = 0
    for expense in expenses:
        total+= expense.amount
        if expense.category == "business":
            t_business += expense.amount
        elif expense.category == "other":
            t_other += expense.amount
        elif expense.category == "food":
            t_food += expense.amount
        elif expense.category == "entertainment":
            t_entertainment += expense.amount
            
    return render_template('expenses.html',expenses=expenses, 
                           total = total,
                           t_business= t_business,
                           t_other = t_other,
                           t_food =t_food,
                           t_entertainment = t_entertainment)


@app.route('/')
def add():
    return render_template('add.html')
@app.route('/addexpense',methods=['POST'])
def addexpense():
    date = request.form["date"]
    expensename =request.form["expensename"]
    amount = request.form['amount']
    category = request.form['category']
    expense =Expense(date=date,expensename=expensename,amount=amount,category=category)
    db.session.add(expense)
    db.session.commit()
    return redirect('/expenses')

@app.route('/delete/<int:id>')
def delete(id):
    expense = Expense.query.filter_by(id=id).first()
    db.session.delete(expense)
    db.session.commit()
    return redirect("/expenses")

@app.route('/updateexpense/<int:id>')
def updateexpense(id):
    expense =Expense.query.filter_by(id=id).first()
    return render_template('updateexpense.html',expense=expense)
    
@app.route('/edit',methods=['POST'])
def edit():
    date = request.form["date"]
    expensename =request.form["expensename"]
    amount = request.form['amount']
    category = request.form['category']
    id = request.form['id']
    expense =Expense.query.filter_by(id=id).first()
    expense.date =date   
    expense.category =category 
    expense.expensename =expensename   
    expense.amount = amount   
    
    db.session.commit()
    return redirect("/expenses")

    
@app.route('/addview',methods=["GET","POST"])
def addview():
    if request.method=="GET":
        expenses = Expense.query.all()
        total = 0
        t_business = 0
        t_other =0
        t_food = 0
        t_entertainment = 0
        for expense in expenses:
            total+= expense.amount
            if expense.category == "business":
                t_business += expense.amount
            elif expense.category == "other":
                t_other += expense.amount
            elif expense.category == "food":
                t_food += expense.amount
            elif expense.category == "entertainment":
                t_entertainment += expense.amount
    elif request.method=="POST":
        date = request.form["date"]
        expensename =request.form["expensename"]
        amount = request.form['amount']
        category = request.form['category']
        expense =Expense(date=date,expensename=expensename,amount=amount,category=category)
        db.session.add(expense)
        db.session.commit()
        return redirect('/addview')
            
    return render_template('addview.html',expenses=expenses, 
                           total = total,
                           t_business= t_business,
                           t_other = t_other,
                           t_food =t_food,
                           t_entertainment = t_entertainment)

    pass   


if __name__ == '__main__':
    app.run(debug=True)

"""

pdf.chapter_body(code)

description = """
1) Please install the requirements
2) run the app.py file at the terminal
3) The app will run on the localhost
4) The app will run on the port 5000
5) The base.html file is used to create the base template for the project
<!DOCTYPE html>
<html >
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.0.1/chart.min.js" integrity="sha512-2uu1jrAmW1A+SMwih5DAPqzFS2PI+OPw79OVLS4NJ6jGHQ/GmIVDDlWwz4KLO8DnoUmYdU8hTtFcp8je6zxbCg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ url_for('static',filename='style.css') }}">

<title>Document</title>

</head>
<body>

    <nav class="navbar navbar-expand-lg navbar-dark bg-danger">
        <a class="navbar-brand" href="#">Expense Manager </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <a class="nav-link" href="/">Add Expenses <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/expenses">View Expenses</a>
            </li>
         </ul>
        </div>
      </nav>
    {% block body %}


    {% endblock %}
</body>
</html>
5)We can add the expenses using the form provided in the site
we can view the expenses using the view expenses link
and we can delete the expenses using the delete link
6)The add.html file is used to create the add expenses form

"""
pdf.chapter_body(description)



pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(18, list_of_dirs[17])
Description = """
this is the project description. we aim to create a pdf using the fpdf library.
The project is used to create a pdf using the information provided by the user.
we can create pdf with csv files, text files and create links as well """

pdf.chapter_body(Description)

code = """
1)

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image(r'D:\inligntech\Generate_PDF_with_Python\logo.png', 10, 8, 33)
        self.set_font("helvetica", 'B', 16)
        self.cell(80)
        self.cell(40, 10, "Hello world", border=1, align="C")
        self.ln(40)  # line break

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", 'I', 16)
        self.cell(0, 10, f"Page {self.page_no()} / {{nb}} ", align="C")


pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
for i in range(1, 41):
    pdf.cell(60, 10, f'Printing Line number.{i}',
             new_x="LMARGIN", new_y="NEXT", align='C')
    # pdf.cell(0,10,f"Printing line number {i}",new_x="LMARGIN", new_y="TOP", align="L")


pdf.output("Sample.pdf")

2)
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", size=12)
        width = self.get_string_width(self.title) + 6
        self.set_x((210-width)/2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(200, 220, 255)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(width, 9, self.title, new_x="LMARGIN",
                  new_y="NEXT", align="C", fill=True)
        self.ln(10)  # line break

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "i", size=12)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, num, label):
        self.set_font("helvetica", "I", size=12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, f"chapter {num} : {label}",
                  new_x="LMARGIN", new_y="NEXT", align="L", fill=True)

    def chapter_body(self, file_path):
        with open(file_path, "rb") as f:
            txt = f.read().decode("latin-1")
        self.set_font("Times", size=12)
        self.ln(10)
        self.multi_cell(0, 5, txt)
        self.ln()  # line break
        self.set_font(style="I")
        self.cell(0, 5, "(End of excerpt)")

    def print_chapter(self, num, title, file_path):
        self.add_page()  # add a new page
        self.chapter_title(num, title)
        self.chapter_body(file_path)


pdf = PDF()
pdf.set_title("100 ways to learning programming")
pdf.set_author("Inlign Technologies")

pdf.print_chapter(1, "GETTING STARTED WITH PROGRAMMING",
                  "D:\inligntech\PDF\para.txt")
pdf.print_chapter(2, "WHICH PROGRAMMING LANGUAGE",
                  "D:\inligntech\PDF\para.txt")

pdf.output("Sample2.pdf")

3)
from fpdf import FPDF
from fpdf.fonts import FontFace
import csv

with open('D:\inligntech\Generate_PDF_with_Python\credit.csv', encoding='utf-8') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))
    data = [dat[2:8] for dat in data]
pdf = FPDF()
pdf.set_font("helvetica", size=14)
pdf.add_page()


pdf.set_draw_color(255, 0, 0)
pdf.set_line_width(0.3)
heading_style = FontFace(emphasis="BOLD", color=255, fill_color=(255, 100, 0))
with pdf.table(

    borders_layout="NO_HORIZONTAL_LINES",
    cell_fill_color=(224, 235, 255),
    line_height=6,
    width=160,
    headings_style=heading_style
) as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)
pdf.output('table.pdf')

4)
from fpdf import FPDF

pdf = FPDF()


pdf.add_page()
pdf.set_font("helvetica", size=20)
pdf.write(5, "To find out what new in the tutorial ")
pdf.set_font(style="U")
link = pdf.add_link(page=2)
pdf.write(5, "here", link=link)

# second page
pdf.add_page()
pdf.image("D:\inligntech\PDF\logo.png", 10, 10,
          50, 0, "", "https://www.google.com")
pdf.set_left_margin(60)
pdf.set_font_size(18)

pdf.write_html(""You can add any html text here<b>This is some bold text</b>
                   <h1>This is a heading</h1>
               <a href="https://www.google.com">Click here to go to Google </a>
               
               "")
pdf.output("Link.pdf")


"""
pdf.chapter_body(code)

requirements = """The libraries used in this project are:

1)fpdf
2)fpdf.fonts
3)csv
4)os
5)pyqrcode

The fpdf library is used to create the pdf for the project.
The fpdf.fonts library is used to create the fonts for the project.
The csv library is used to create the csv file for the project.
The os library is used to create the file.
The pyqrcode library is used to create the QR code for the project.
"""

pdf.chapter_body(requirements)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(19, list_of_dirs[19])
pdf.chapter_image(r'D:\inligntech\InvoiceGenerator_PDF\invoicegen.PNG')

Description = """
This is the project description.
We want to create a invoice generator using python for billing purpose.
The project is used to create a invoice using the information provided by the user.
We build a python application
we can add delete and update the invoice information.
"""

pdf.chapter_body(Description)

code = """
from tkinter import *
from fpdf import FPDF
invoice_item = []


def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    quantity = int(quantity_entry.get())
    price = medicines[selected_medicine]
    total_amount = price * quantity
    invoice_item.append((selected_medicine, quantity, price, total_amount))
    update_invoice_text()


def calculate_total():
    total = 0.0
    for item in invoice_item:
        total += item[3]
    return total


def update_invoice_text():
    invoice_text.delete(1.0, END)  # line 1, column 0
    for item in invoice_item:
        invoice_text.insert(
            END, f"Medicine{item[0]},Quanity{item[1]},Price{item[2]},Total {item[3]}\n")
    total_amount_entry.delete(0, END)
    total_amount_entry.insert(END, str(calculate_total()))


def generate_invoice():
    customer_name = customer_entry.get()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)
    pdf.cell(0, 10, text="Invoice", new_x='LMARGIN', new_y="NEXT", align='C')

    pdf.cell(0, 10, text=f"Customer {customer_name}",
             new_x='LMARGIN', new_y="NEXT", align='L')
    pdf.cell(0, 10, text="", new_x='LMARGIN', new_y="NEXT")

    for item in invoice_item:
        medicine_name, quantity, price, total = item

        pdf.cell(0, 10, text=f"Medicine : {medicine_name} , Quantity : {quantity}, Amount : {total}",
                 new_x='LMARGIN', new_y="NEXT", align='L')
    pdf.cell(0, 10, text="Total Amount :"+str(calculate_total()),
             new_x='LMARGIN', new_y="NEXT", align='L')
    pdf.cell(0, 10, text="", new_x='LMARGIN', new_y="NEXT")

    pdf.output("invoice.pdf")


window = Tk()
window.title("Invoice Generator")

medicines = {
    "Medicine A": 10.0,
    "Medicine B": 20.0,
    "Medicine C": 30.0,
    "Medicine D": 40.0,
}

medicine_label = Label(window, text="Medicine Name  ")
medicine_label.pack()
medicine_listbox = Listbox(window, selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END, medicine)
medicine_listbox.pack()


quantity_label = Label(window, text="Quantity")
quantity_entry = Entry(window)
quantity_label.pack()
quantity_entry.pack()

add_button = Button(window, text="Add Medicine: ", command=add_medicine)
add_button.pack()

total_amount_label = Label(window, text="Total amount")
total_amount_label.pack()


total_amount_entry = Entry(window)
total_amount_entry.pack()


customer_label = Label(window, text="Customer Name")
customer_label.pack()
customer_entry = Entry(window)
customer_entry.pack()

generate_button = Button(
    window, text="Generate Invoice", command=generate_invoice)
generate_button.pack()

invoice_text = Text(window, height=10, width=50)
invoice_text.pack()


window.mainloop()
"""

pdf.chapter_body(code)

libraries = """The libraries used in this project are:

1) tkinter
2) fpdf
3) os


The tkinter library is used to create the GUI for the project.
The fpdf library is used to create the pdf for the project.
The os library is used to create the file.
"""

pdf.chapter_body(libraries)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(20, list_of_dirs[20])
pdf.chapter_image(r'D:\inligntech\opencv\blue.jpg')

description = """
This is an opencv project.
This project helps us understand the opencv library.
we perform the image processing using the opencv library.
image thresholding is used to create a binary image from a grayscale image.
geometric transformation is used to create a new image from the original image.
image blurring is performed.
gaussian blurring is performed using the gaussian filter.
"""
pdf.chapter_body(description)

code = """
import cv2
#blurring Averaging
image = cv2.imread('train.jpeg',1)
blur=cv2.blur(image,(5,5),)
cv2.imshow('image',image)
cv2.imshow('image1',blur)
cv2.waitKey(10000)
cv2.destroyAllWindows()

2)import cv2
# mouse click events
def draw_circle(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
       cv2.circle(image,(x,y),100,(255,0,0),-1)

image =cv2.imread('lena.jpg',1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()


3)import cv2
#Gaussian filtering
image = cv2.imread('train.jpeg',1)
gaussian_blur=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('image',image)
cv2.imshow('blur',gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

4)import cv2
import numpy as np
#matrix = np.float32([[1,0,100],[0,1,100]])
image = cv2.imread('lena.jpg',0)
rows,cols = image.shape
rot_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),120,1)#rotation
new_image = cv2.warpAffine(image,rot_matrix,(rows,cols))
cv2.imshow('image',image)
cv2.imshow('image1',new_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

5)
import cv2
image = cv2.imread('lena.jpg',0)
resize = cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)

cv2.imshow('image',image)
cv2.imshow('image1',resize)
cv2.waitKey(10000)
cv2.destroyAllWindows()

6)

import cv2
import numpy as np
matrix = np.float32([[1,0,100],[0,1,100]])
image = cv2.imread('lena.jpg',0)
rows,cols = image.shape
new_image = cv2.warpAffine(image,matrix,(rows,cols))
cv2.imshow('image',image)
cv2.imshow('image1',new_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

7)

import cv2
import numpy as np

image = cv2.imread('gradient.png',0)
ret,thresh = cv2.threshold(image,80,255,cv2.THRESH_BINARY)

cv2.imshow('image',image)
cv2.imshow('image2',thresh)
cv2.waitKey(10000)
cv2.destroyAllWindows()

8)
import cv2
image = cv2.imread('D:\inligntech\opencv\lena.jpg',1)
a= image[0:100,0:100]
image[100:200,100:200] = a

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()



9)
import cv2
#manipulating pixels
image = cv2.imread("lena.jpg",1)
image[100,100] =(255,255,255)
print(image[100,100])
cv2.imshow('image',image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

#size of the image
print(image.shape)


10)
import numpy as np
import cv2
image = cv2.imread('blue.jpg',1)

#object tracking

new_image= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('image',new_image)


low_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(new_image,low_blue,upper_blue)
cv2.imshow('mask',mask)

res =cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('res',res)

blue = np.uint8([[[255,0,0]]])
hsv_blue= cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
print(hsv_blue)
cv2.waitKey(10000)
cv2.destroyAllWindows()

11)
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _,frame= cap.read()

    # object tracking

    new_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('image', new_image)

    low_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(new_image, low_blue, upper_blue)
    #cv2.imshow('mask', mask)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('res', res)
    k= cv2.waitKey(5) & 0xff
    if k==27:
        break
cv2.waitKey(10000)
cv2.destroyAllWindows()


12)
import cv2
import numpy as np


image = cv2.imread('train.jpeg',1)
matrix = np.ones((5,5),dtype=np.float32)/25
new_image = cv2.filter2D(image,-1,matrix)

cv2.imshow('image',image)

cv2.imshow('image1',new_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

13)
#blurring
import cv2
import numpy as np


image = cv2.imread('train.jpeg',1)
matrix = np.ones((5,5),dtype=np.float32)/25
new_image = cv2.filter2D(image,-1,matrix)

cv2.imshow('image',image)

cv2.imshow('image1',new_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

14)

import cv2
#how to draw shapes on images

image = cv2.imread('lena.jpg',1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(0,0),(400,400),(0,255,0),5)
cv2.circle(image,(250,250),100,(0,0,255),-1)
cv2.putText(image,"Hello  Mountains",(100,100),
            cv2.FONT_ITALIC,2,(255,255,255),cv2.LINE_AA)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


15)
#adaptive thresholding
import cv2
import numpy as np
#Simple thresholding 1 value for entire image
#adaptive mean , adaptive gaussian , global thresholding
#cv2.adaptivethreshold-> blocksize
#method  mean, threshold
#block size = neighborhood area
#constant - to be subtracted from mean
#mutiple thresholding values for different sections of an image

image = cv2.imread('sample.jpg',0)
ret,thresh = cv2.threshold(image,80,255,cv2.THRESH_BINARY)

cv2.imshow('image1',image)
cv2.imshow('image2',thresh)
cv2.waitKey(10000)
cv2.destroyAllWindows()

image = cv2.imread('sample.jpg',0)
thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,10)

cv2.imshow('image3',image)
cv2.imshow('image4',thresh)
cv2.waitKey(10000)
cv2.destroyAllWindows()

image = cv2.imread('sample.jpg',0)
thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)

cv2.imshow('image5',image)
cv2.imshow('image6',thresh)
cv2.waitKey(10000)
cv2.destroyAllWindows()

16)
import cv2

capture = cv2.VideoCapture(0)

while(True):
    ret,frame = capture.read(0)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

"""
libraries = """The libraries used in this project are:
1)cv2

opencv library is used to create the image processing for the project.

"""

pdf.chapter_body(libraries)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(21, list_of_dirs[21])
pdf.chapter_image(r'D:\inligntech\Password_Validator\password_val.png')

Description = """
This is a password validator project.
The project is used to create a password validator using the information provided by the user.
We build a python application
"""


pdf.chapter_body(Description)

code = """
from tkinter import * 
import bcrypt



def validate(password):
    hash = b'$2b$12$XvLQGsorO07xxiOk54dpbeApVZ9Om/uJTu/qXwgcNhu8uamESalIi'
    password =bytes(password,encoding='utf-8')

    if bcrypt.checkpw(password,hash):
        print("Login successful")
    else:
        print("invalid password")
root = Tk()
root.geometry("300x300")



password_entry = Entry(root)
password_entry.pack()

button = Button(root,text="Validate",command=lambda: validate(password_entry.get()))
button.pack()
root.mainloop()



2)import bcrypt

password = b"thisismypassword"
hashed = bcrypt.hashpw(password,bcrypt.gensalt())
print(hashed)

entered_password =input("enter password to login")
entered_password =bytes(entered_password,encoding='utf-8')

if bcrypt.checkpw(entered_password,hashed):
    print("Login successful")
else:
    print("invalid password")

"""

pdf.chapter_body(code)
libraries = """The libraries used in this project are:
1)tkinter
2)bcrypt

tkinter library is used to create the GUI for the project.
bcrypt library is used to create the password hashing for the project.
"""
pdf.chapter_body(libraries)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(22, list_of_dirs[22])
pdf.chapter_image(r'D:\inligntech\Pyqt_Calculator\pyqt_calc.png')

Description = """
This is a calculator project using pyqt6 library.
"""

pdf.chapter_body(Description)

code = """
from PyQt6.QtWidgets  import  QGridLayout, QHBoxLayout,QVBoxLayout,QWidget, QApplication,QLabel, QPushButton, QLineEdit, QCheckBox
from PyQt6.QtGui import QPixmap
import sys
from PyQt6.QtCore import Qt

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    

    def initUI(self):  
        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0,0,400,160)
       
        # adding label
        layout = QGridLayout()
        self.setLayout(layout)

        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        layout.addWidget(self.display,0,0,1,4)

        buttons = [QPushButton(str(i)) for i in range(10)]
        for i,button in enumerate(buttons):
        
            row , col = divmod(i,3)
            layout.addWidget(button, row+1, col)
        
        # Adding event handlers to buttons 
        for button in buttons:
            button.clicked.connect(self.number_button_click)

        operators = ['+', '-', '*', '/']
        operator_buttons = [QPushButton(op) for op in operators]
        for i,operator_button in enumerate(operator_buttons):
            layout.addWidget(operator_button, i+1, 3)
        for button in operator_buttons:
            button.clicked.connect(self.operator_button_click)
        
        
        
        self.equals_button = QPushButton("=")
        self.equals_button.clicked.connect(self.calculate)

        self.clear_button = QPushButton("C")
        self.clear_button.clicked.connect(self.clear)
    
        layout.addWidget(self.equals_button, 4, 1)
        layout.addWidget(self.clear_button, 4, 2)
    
    def number_button_click(self):
        digit  = self.sender().text()
        if self.current_input=="0":
            self.current_input = digit
        else:
            # not adding but appending as a string
            self.current_input = self.current_input + digit
        self.display.setText(self.current_input)
    
    def operator_button_click(self):
        operator = self.sender().text()
        if self.current_operator=="":
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input = "0"
        else:
            #calculate the result 
            self.calculate()
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input = "0"
    def calculate(self):
        if self.current_operator == "+":
            result = str(float(self.previous_input) + float(self.current_input))
        elif self.current_operator == "-":
            result = str(float(self.previous_input) - float(self.current_input))
        elif self.current_operator == "*":
            result = str(float(self.previous_input) * float(self.current_input))
        elif self.current_operator == "/":
            if self.current_input == "0":
                result="Erro4"
            else:
                result = str(float(self.previous_input) / float(self.current_input))
        
        else:
            result = str(self.current_input) 
        self.display.setText(str(result)) 
        self.current_input = result
        self.current_operator = ""
    def clear(self):
        self.current_operator = ""
        self.previous_input = ""
        self.current_input = "0"
        self.display.setText(self.current_input)

app = QApplication(sys.argv)
window = Window()

window.show()


sys.exit(app.exec())
"""

pdf.chapter_body(code)

libraries = """The libraries used in this project are:
1)PyQt6
2)sys
3)os
4)PyQt6.QtWidgets
5)PyQt6.QtGui
6)PyQt6.QtCore

The PyQt6 library is used to create the GUI for the project.

"""
pdf.chapter_body(libraries)


pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(23, list_of_dirs[23])
pdf.chapter_image(r'D:\inligntech\Pyqt_Database\pyqt_database.png')
pdf.chapter_image(r'D:\inligntech\Pyqt_Database\pyqt_database2.png')

Description = """
This is a database project using pyqt6 library.
"""

pdf.chapter_body(Description)

code = """

1)
from PyQt6.QtWidgets  import  QWidget, QApplication,QLabel, QListWidget,QHBoxLayout, QListWidgetItem
from PyQt6.QtGui import QPixmap
import sys

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0,0,700,500)
        fruits =['Apple','Mango','Orange','Banana','Pineapple']
        self.listwidget = QListWidget()
        self.listwidget.setAlternatingRowColors(True)
        
        for fruit in fruits:
            listitem = QListWidgetItem()
            listitem.setText(fruit)
            self.listwidget.addItem(listitem)


        self.layout =QHBoxLayout()
        self.layout.addWidget(self.listwidget)
        self.setLayout(self.layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

2)
from PyQt6.QtWidgets  import  QMenu,QMessageBox,QToolBar,QPushButton,QSpinBox,QLineEdit,QFormLayout,QMainWindow, QDockWidget,QWidget, QApplication,QLabel,QTableWidget,QTableWidgetItem, QListWidget,QHBoxLayout, QListWidgetItem
from PyQt6.QtGui import QPixmap ,QAction,QIcon 
from PyQt6.QtCore import Qt ,QSize 
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0,0,700,500)
        people =[
            {"First Name":"John","Last Name":"Doe","Age":21},
            {"First Name":"Rob","Last Name":"Ford","Age":31},
            {"First Name":"Bob","Last Name":"Tyson","Age":41},
    
            
        ]
        self.table_widget =  QTableWidget()
        self.table_widget.setRowCount(len(people))
        self.table_widget.setColumnCount(3)
        
        self.table_widget.setHorizontalHeaderLabels(people[0].keys())
        row = 0 
        for person in people:
            self.table_widget.setItem(row, 0 , QTableWidgetItem(person['First Name']))
            self.table_widget.setItem(row, 1 , QTableWidgetItem(person['Last Name']))
            self.table_widget.setItem(row, 2 , QTableWidgetItem(str(person['Age'])))


            row +=1

        dock = QDockWidget()
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea,dock)

        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.age = QSpinBox(form,minimum=18,maximum=60)

        layout.addRow("First Name",self.first_name)
        layout.addRow("First Name",self.last_name)
        layout.addRow("First Name",self.age)

        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_people)
        layout.addRow(add_button)
        


        dock.setWidget(form)

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        self.delete_action = QAction(QIcon("D:\inligntech\icons\delete.png"),"Delete ",self)
        self.delete_action.triggered.connect(self.delete)
        toolbar.addAction(self.delete_action)
        
        self.add_row_above = QAction("Add row above ",self)
        self.add_row_above.triggered.connect(self.addRowAbove)
        
        self.add_row_below = QAction("Add row below ",self)
        self.add_row_below.triggered.connect(self.addRowBelow)
        
        self.copy_action = QAction("Copy  ",self)
        self.copy_action.triggered.connect(self.copy)
        
        self.paste_action = QAction("Paste ",self)
        self.paste_action.triggered.connect(self.paste)
        
        
        
        
        self.setCentralWidget(self.table_widget)
    
    
    def delete(self):
        current_row = self.table_widget.currentRow()
        if current_row <0 :
            QMessageBox.warning(self,"No row Selected")
        
        button = QMessageBox.question(self,"Delete Row","Are you Sure, you want to Delete Row?",QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if button  == QMessageBox.StandardButton.Yes:
            self.table_widget.removeRow(current_row)

        

    def add_people(self):
        row = self.table_widget.rowCount()
        self.table_widget.insertRow(row)
        self.table_widget.setItem(row,0,QTableWidgetItem(self.first_name.text().strip()))
        self.table_widget.setItem(row,1,QTableWidgetItem(self.last_name.text().strip()))
        self.table_widget.setItem(row,2,QTableWidgetItem(self.age.text().strip()))

    def contextMenuEvent(self, event):
        context_menu = QMenu()
        context_menu.addAction(self.delete_action)
       
        context_menu.addAction(self.add_row_below)
        context_menu.addAction(self.add_row_above)
        context_menu.addAction(self.copy_action)
        context_menu.addAction(self.paste_action)
        
        
        context_menu.exec(event.globalPos())


    def addRowAbove(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.insertRow(current_row)

        
        
    def addRowBelow(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.insertRow(current_row+1)

    def copy(self):
        text     = self.table_widget.currentItem().text()
        self.item_text = text

    def paste(self):
        if self.item_text != None:
            row = self.table_widget.currentRow()
            column = self.table_widget.currentColumn()
            self.table_widget.setItem(row,column,QTableWidgetItem(self.item_text))            
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

"""

pdf.chapter_body(code)

libraries = """The libraries used in this project are:
1)PyQt6
2)PyQt6.QtWidgets
3)PyQt6.QtGui
4)PyQt6.QtCore


The PyQt6 library is used to create the GUI for the project.
The PyQt6.QtWidgets library is used to create the widgets for the project.
The PyQt6.QtGui library is used to create the GUI for the project.
The PyQt6.QtCore library is used to create the core for the project.
"""

pdf.chapter_body(libraries)



pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(24, list_of_dirs[24])
pdf.chapter_image(r'D:\inligntech\Pyqt_Paint\paint.png')
pdf.chapter_image(r'D:\inligntech\Pyqt_Paint\paint2.png')


Description = """
This is a paint project using pyqt6 library.
"""
pdf.chapter_body(Description)

code = """  
1)
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel ,QStatusBar,QToolBar ,QColorDialog,QFileDialog
from PyQt6.QtGui import QPixmap, QMouseEvent , QPainter ,QPen ,QColor , QAction ,QIcon
from PyQt6.QtCore import Qt ,QPoint, QRect,QSize 
#pyuic6 demo.ui -o form.py
import sys
import os

class Canvas(QLabel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent= parent
        self.initUI()
        
        
    def initUI(self):
        self.pixmap = QPixmap(400,400)
        self.pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self.pixmap)
        self.setMouseTracking(True)
        self.drawing = False
        self.last_mouse_position = QPoint()
        self.status_label = QLabel()
        self.eraser = False
        self.pen_color = Qt.GlobalColor.black
        self.pen_width =  1


    def mouseMoveEvent(self, event):
        mouse_position = event.pos()
        status_text= f"Mouse Coordinates are :{mouse_position.x(),mouse_position.y()}"
        self.status_label.setText(status_text)

        self.parent.statusBar.addWidget(self.status_label)
        if(event.buttons() & Qt.MouseButton.LeftButton) and self.drawing:
            self.draw(mouse_position)
        

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print(event.button())
            self.drawing = True
            self.last_mouse_position = event.pos()
            print("Left Click Position: "+ str(event.pos()))
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            
            self.drawing = False
            print("Mouse released at Position: "+ str(event.pos()))

    def draw(self,points):
        painter = QPainter(self.pixmap)
        pen = QPen(self.pen_color,self.pen_width)
           
        if self.eraser==False:

            painter.setPen(pen)
            painter.drawLine(self.last_mouse_position,points)
            self.last_mouse_position = points
        elif self.eraser==True:    
            eraser =QRect(points.x(),points.y(),12,12)
            painter.eraseRect(eraser)

        self.update()
    def paintEvent(self,event):
        painter = QPainter(self)
    
        target_rect = event.rect()
        painter.drawPixmap(target_rect,self.pixmap,target_rect)  
        painter.end()

    def selectTool(self,tool):
        if tool == "pencil":
            self.pen_width =2
            self.eraser= False
        elif tool == "marker":
            self.pen_width=4
            self.eraser= False
        elif tool == "color":
            
            self.eraser= False
            color=QColorDialog.getColor()
            self.pen_color = color
        elif tool == "eraser":
            self.eraser =True
    def new(self):
        self.pixmap.fill(Qt.GlobalColor.white)
        self.update()
    
    def save(self):
        file_name,_ = QFileDialog.getSaveFileName(self,"Save As",os.path.curdir+"sample.png","(*.png)")
        if file_name:
            self.pixmap.save(file_name,"png")
        
        
        

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0,0,400,400)
        self.setWindowTitle("Paint App")
    
    # creating Canvas 
        canvas =Canvas(self)
        self.setCentralWidget(canvas)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
    #Adding Toolbar
        tool_bar = QToolBar("Toolbar")
        tool_bar.setIconSize(QSize(24,24))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea,tool_bar)
        tool_bar.setMovable(False)


        pencil_act =  QAction(QIcon("icons/pencil.png"),"Pencil",tool_bar)
        pencil_act.triggered.connect(lambda: canvas.selectTool("pencil"))
       
        marker_act =  QAction(QIcon("icons/marker.png"),"Marker",tool_bar)
        marker_act.triggered.connect(lambda: canvas.selectTool("marker"))
       
        eraser_act =  QAction(QIcon("icons/eraser.png"),"Eraser",tool_bar)
        eraser_act.triggered.connect(lambda: canvas.selectTool("eraser"))
       
        color_act =  QAction(QIcon("icons/color.png"),"Color",tool_bar)
        color_act.triggered.connect(lambda: canvas.selectTool("color"))
        
        tool_bar.addAction(pencil_act)
        tool_bar.addAction(marker_act)
        tool_bar.addAction(eraser_act)
        tool_bar.addAction(color_act)
        
        self.new_action = QAction("New")
        self.new_action.triggered.connect(canvas.new)
        self.save_file_action = QAction("Save")
        self.save_file_action.triggered.connect(canvas.save) 
        self.quit_action = QAction("Exit")
        self.quit_action.triggered.connect(self.close)
        
        self.menuBar().setNativeMenuBar(False)
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.save_file_action)
        file_menu.addAction(self.quit_action)
        
        
app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()

2)
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtGui import QPixmap, QMouseEvent, QPainter, QPen
from PyQt6.QtCore import Qt, QPoint, QRect
import sys


class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap(400, 400)  # Set the size of the canvas
        self.pixmap.fill(Qt.GlobalColor.white)  # Fill the canvas with white color
        self.setPixmap(self.pixmap)  # Properly set the pixmap
        self.setMouseTracking(True)
        self.drawing = False
        self.last_mouse_position = QPoint()

    def mouseMoveEvent(self, event):
        mouse_position = event.pos()
        if (event.buttons() & Qt.MouseButton.LeftButton) and self.drawing:
            self.draw(mouse_position)
        print(mouse_position)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_mouse_position = event.pos()  # Initialize the last mouse position
            print("Left Click Position: " + str(event.pos()))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
            print("Mouse released at Position: " + str(event.pos()))

    def draw(self, points):
        painter = QPainter(self.pixmap)
        pen = QPen(Qt.GlobalColor.black, 5)  # Set pen color and width
        painter.setPen(pen)
        painter.drawLine(self.last_mouse_position, points)  # Draw a line from the last position to the current position
        self.last_mouse_position = points  # Update the last mouse position
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        target_rect = event.rect()
        painter.drawPixmap(target_rect, self.pixmap, target_rect)  # Draw the pixmap on the canvas
        painter.end()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("Paint App")
        canvas = Canvas()
        self.setCentralWidget(canvas)


app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()

"""

pdf.chapter_body(code)

libraries = """The libraries used in this project are:
1)PyQt6
2)PyQt6.QtWidgets
3)PyQt6.QtGui
4)PyQt6.QtCore
The PyQt6 library is used to create the GUI for the project.
The PyQt6.QtWidgets library is used to create the widgets for the project.
The PyQt6.QtGui library is used to create the GUI for the project.
The PyQt6.QtCore library is used to create the core for the project.
"""
pdf.chapter_body(libraries)



pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(25, list_of_dirs[25])
pdf.chapter_image(r'D:\inligntech\Pyqt_Stylesheets_QtDesigner\bm.png')

Description =   """

This project is to create a beverage maker using the Pyqt6 application
"""
pdf.chapter_body(Description)

code ="""
from PyQt6.QtWidgets  import QCheckBox,QRadioButton,QTabWidget,QHBoxLayout,QGroupBox, QPushButton,QWidget,QMainWindow,QApplication, QStyleFactory, QLabel,QVBoxLayout
import sys

 
class Window(QWidget):
    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setGeometry(100,100,700,500)
    # creating the tab widget
        tab_widget = QTabWidget()
        tea_tab= QWidget()
        coffee_tab =QWidget()

        tab_widget.addTab(tea_tab,"Tea")
        tab_widget.addTab(coffee_tab,"Coffee")

        


        # create the layout Tea
        tea_layout = QVBoxLayout()

        # create a label 

        liquid_label = QLabel("Select Milk /Water")
        spice_label = QLabel("Select Spices to add ")

        milk_button = QRadioButton("Milk ")
        water_button = QRadioButton("Water ")
        #sugar_button = QCheckBox("Sugar")
        #clove_button = QCheckBox("Clove ")
        #bpepper_button = QCheckBox("Black Pepper")
        #cinammon_button = QCheckBox("Cinnamon ")
        #turmeric_button = QCheckBox("Turmeric ")


        # create a container for milk/water
        liquid_group  = QGroupBox()
        spice_group = QGroupBox()
        # create a layout for liquid

        liquid_group_layout = QVBoxLayout()
        spice_group_layout = QVBoxLayout()    
        liquid_group_layout.addWidget(milk_button)
        liquid_group_layout.addWidget(water_button)
        
        spices = ['sugar','clove','blackpeppwe','cinnamon','turmeric']
        
        for spice in spices:
            spice_check_box = QCheckBox(spice)
            spice_group_layout.addWidget(spice_check_box)
        #spice_group_layout.addWidget(sugar_button)
        #spice_group_layout.addWidget(clove_button)
        #spice_group_layout.addWidget(bpepper_button)
        #spice_group_layout.addWidget(cinammon_button)
        #spice_group_layout.addWidget(turmeric_button)
        
            
        liquid_group.setLayout(liquid_group_layout)
        spice_group.setLayout(spice_group_layout)
        
        tea_layout.addWidget(liquid_label)
        tea_layout.addWidget(liquid_group)
        tea_layout.addWidget(spice_label)
        tea_layout.addWidget(spice_group)
        tea_tab.setLayout(tea_layout)
        
        mainlayout = QVBoxLayout(self)
        mainlayout.addWidget(tab_widget)


        




app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())

"""

pdf.chapter_body(code)


libraries = """The libraries used in this project are:
1)PyQt6
2)PyQt6.QtWidgets
3)PyQt6.QtGui
4)PyQt6.QtCore
The PyQt6 library is used to create the GUI for the project.
The PyQt6.QtWidgets library is used to create the widgets for the project.
The PyQt6.QtGui library is used to create the GUI for the project.
The PyQt6.QtCore library is used to create the core for the project.
"""
pdf.chapter_body(libraries)



pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(26, list_of_dirs[26])
pdf.chapter_image(r'D:\inligntech\Pyqt6_Notepad\notepad.png')

Description = """

This  project is used to create a Notepad application using Pyqt6 Library

"""

pdf.chapter_body(Description)

code= """
from PyQt6.QtWidgets  import QInputDialog,QFileDialog,QMenu,QMenuBar,QMainWindow,QTextEdit, QFormLayout, QWidget, QApplication,QLabel, QPushButton, QLineEdit, QCheckBox
from PyQt6.QtGui import QAction,QIcon,QTextCursor ,QColor 
from PyQt6.QtCore import Qt

import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setWindowTitle("Form Layout")
        self.setGeometry(100,100,400,300)
     
        self.edit_field = QTextEdit(self)
        self.setCentralWidget(self.edit_field)
        
        self.current_file = None
        # creating a menu bar
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)
        #create a Menu
        fileMenu = QMenu("File",self)
        menubar.addMenu(fileMenu)
        editmenu = QMenu("Edit",self)
        menubar.addMenu(editmenu)

        #creating an action 
        
        new_action = QAction("New",self)
        fileMenu.addAction(new_action)
        new_action.triggered.connect(self.new_file)
    
        open_action = QAction("Open",self)
        fileMenu.addAction(open_action)
        open_action.triggered.connect(self.open_file)
    
        save_action = QAction("Save",self)
        fileMenu.addAction(save_action)
        save_action.triggered.connect(self.save_file)
    
        save_as_action = QAction("Save as",self)
        fileMenu.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_file_as)

        #creating an edit menu
        
        #creating an action
        undo_action = QAction("Undo ",self)
        editmenu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

        redo_action = QAction("Redo ",self)
        editmenu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)

        cut_action = QAction("Cut ",self)
        editmenu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

        copy_action = QAction("Copy ",self)
        editmenu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)
        
        paste_action = QAction("Paste ",self)
        editmenu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

        find_action = QAction("Find ",self)
        editmenu.addAction(find_action)
        find_action.triggered.connect(self.find_text)

    
    
    
    def new_file(self):
        print("Creating New File ")
        self.edit_field.clear()
        self.current_file = None


    def open_file(self):
        print("opening New File ")
        filepath,_ = QFileDialog.getOpenFileName(self,"Open file","","All Files (*);; Python Files (*.py)")
        with open(filepath,"r") as f:
            data = f.read()
            self.edit_field.setText(data)


    def save_file_as(self):
        print("saving New File ")
        filepath,_ = QFileDialog.getSaveFileName(self,"Save file","","All Files (*);; Python Files (*.py)")
        print(filepath)
        if filepath:
            with open(filepath,'w') as f:
                f.write(self.edit_field.toPlainText())
            self.current_file = filepath

    def save_file(self):
        print("saving as New File ")
        if self.current_file:

            with open(self.current_file,'w') as f:
                f.write(self.edit_field.toPlainText())

        else:
            self.save_file_as()
    def find_text(self):
        print("Finding Text")  
        text,ok = QInputDialog.getText(self,"Find Text","Search for text:") 
        if ok:
            all_words = []
            self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)
            highlight_color = Qt.GlobalColor.yellow

            while (self.edit_field.find(text)):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)


                selection.cursor = self.edit_field.textCursor()
                all_words.append(selection)

            self.edit_field.setExtraSelections(all_words)

app = QApplication(sys.argv)
#app.setStyle('Fusion')

window = Window()

window.show()


sys.exit(app.exec())


"""

pdf.chapter_body(code)


libraries = """The libraries used in this project are:
1)PyQt6
2)PyQt6.QtWidgets
3)PyQt6.QtGui
4)PyQt6.QtCore
The PyQt6 library is used to create the GUI for the project.
The PyQt6.QtWidgets library is used to create the widgets for the project.
The PyQt6.QtGui library is used to create the GUI for the project.
The PyQt6.QtCore library is used to create the core for the project.
"""
pdf.chapter_body(libraries)



pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(30, list_of_dirs[30])
pdf.chapter_image(r'D:\inligntech\QrcodeGenerator\qrcode.png')

Description = """
This project is to create a Qrcode with the specified website link and name

"""
pdf.chapter_body(Description)


code="""
from tkinter import * 
import pyqrcode
from PIL import ImageTk,Image 

def  generate():
    link_name = name_entry.get()
    link= link_entry.get()

    file_name = link_name+".png"
    url =  pyqrcode.create(link)
    url.png(file_name,scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,450,window=image_label)

root = Tk()
canvas=Canvas(root,width=400,height=600)
canvas.pack()

app_label=Label(root,text="Qr code generator",fg="blue",font=("Arial",30))
canvas.create_window(200,50,window=app_label)

name_label = Label(root,text="Link name ")
link_label = Label(root,text="Link  ")
canvas.create_window(200,100,window=name_label)
canvas.create_window(200,160,window=link_label)
name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200,130,window=name_entry)
canvas.create_window(200,180,window=link_entry)

button = Button(root,text="Generate QR code ",command=generate)
canvas.create_window(200,230,window=button)

root.mainloop()


"""
libraries = """
1)tkinter
2)pyqrcode
3)PIL 

tkinter is used to create the gui application 
pyqrcode is used to create the Qr code
PIL is used to create the images

"""

pdf.chapter_body(libraries)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(30, list_of_dirs[30])
pdf.chapter_image(r'D:\inligntech\Snake_Pygame\snake.png')


Description ="""
This project is used to create the Snake game using the pygame library
"""

pdf.chapter_body(Description)

code= """"

import pygame
import random


pygame.init()

# setting the game window 
window_width = 800
window_height = 600

# set the display mode
window = pygame.display.set_mode((window_width, window_height))
# set the caption 
pygame.display.set_caption("Pygame Demo")

# set the colors
white =(255,255,255)
black =(0,0,0)
red = (255,0,0)
# gameover bool
game_over = False

# adjusted snake head positions
x1= window_width/2
y1= window_height/2

# change in x1, y1
x1_change =0
y1_change =0

# length of snake , score , snakebody
length_of_snake =1
score = 0
snake_body=[]


# snake touch window game stops
if x1 >= window_width or x1 < 0 or y1>=window_height or y1 <0 :
    game_over =True

# check frame rate
clock = pygame.time.Clock()

# Randomized food positions
food_x = round(random.randrange(0,window_width-10)/10) *10
food_y = round(random.randrange(0,window_height-10)/10) *10

#running event loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over =True
        #check for arrow keys press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0   
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0   
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10   
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10   

    #adjust x1 changes
    x1 += x1_change
    y1 += y1_change   
    #fill window black 
    window.fill(black)     
    

    # contain the length of the snake while travesing to just length of the snake.
    
    snake_head = []
    # append every single x1, y1
    snake_head.append(x1)
    snake_head.append(y1)
    # add it to snake head
    snake_body.append(snake_head)

    # for every x1,y1 added to snake head and then added to snakebody tuple.
    # start deleting the entries from the beginning if the snakebody exceeds snake_length
    if len(snake_body) > length_of_snake:
        del snake_body[0]
    # if snake touches itself, then it is gameover
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over=True
    
    # display score on the screen using blit
    font_style = pygame.font.SysFont(None,50)
    score_text = font_style.render("Score: "+str(score),True,white)
    window.blit(score_text,(10,10))

    # snake eats food then add new randomized food locations and update lenght and score 
    if x1 == food_x and y1==food_y:
        food_x = round(random.randrange(0,window_width-10)/10) *10
        food_y = round(random.randrange(0,window_height-10)/10) *10
        length_of_snake += 1
        score +=1

    #Draw food and snake location on screen
    pygame.draw.rect(window,red,[food_x,food_y,10,10])
    #pygame.draw.rect(window,white,[x1,y1,10,10])
    for segment in snake_body:
        pygame.draw.rect(window,white,[segment[0],segment[1],10,10])
        if x1 >= window_width or x1 < 0 or y1>=window_height or y1 <0:
            game_over =True
    
    # update display 
    pygame.display.update()
    

    clock.tick(15)

"""

pdf.chapter_body(code)


libraries = """
The libraries used to create the above code are
1)pygame
2)Random


pygame is a library used to create gui games with Python
Random is a random number generator

"""
pdf.chapter_body(libraries)

pdf.add_page()
pdf.set_font("helvetica", 'B', 16)
pdf.chapter_title(32, list_of_dirs[32])


Description = """"
This project is used to download videos using python
"""
pdf.chapter_body(Description)

code ="""
from tkinter import * 
from tkinter import filedialog
from pytubefix import YouTube
from moviepy.editor import  * 
import shutil

def download():
    try:

        video_path = url_entry.get()
        file_path = path_label.cget("text")
        if not video_path.startswith("https://www.youtube.com/"):
            print("Invalid YouTube URL")
            return
        mp4 = YouTube(video_path).streams.get_highest_resolution().download(output_path=file_path)
        videoclip = VideoFileClip(mp4)
        # code for MP3
        audio_file = videoclip.audio
        audio_file.write_audiofile('audio.mp3')
        shutil.move(audio.mp3,file_path)
        audio_file.close()
        videoclip.close()
        shutil.move(mp4,file_path)
        print("Download Complete")
    except Exception as e:
        print(f"An error occurred:{e}")       
 

  
def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


root= Tk()
root.title('Video Downloader')
canvas = Canvas(root,width=400, height=300)

canvas.pack()

app_label = Label(root,text="Video Downloader",fg="blue",font=("Arial",30))
canvas.create_window(200,20,window=app_label)
#entry to accept video url

url_entry = Entry(root)
url_label = Label(root, text="Enter video url:")
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,100,window=url_entry)

#path to download videos
path_label = Label(root, text="Select path to download")
path_button = Button(root,text="Select", command = get_path)
canvas.create_window(200,150,window=path_label)
canvas.create_window(200,170,window=path_button)

#downloadbutton 
download_button = Button(root,text="Download", command=download)

canvas.create_window(200,250,window=download_button)

root.mainloop()

"""
pdf.chapter_body(code)

requirements= """
This project has the following requirements

1)tkinter
2)pytubefix
3)moviepy.editor


tkinter is used to create gui based application 
pytubefix is a library to download youtube videos

"""
pdf.chapter_body(requirements)

pdf.output("Sample.pdf")
