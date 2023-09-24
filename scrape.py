#This program scrapes the websites of three local movie theaters using BeautifulSoup and displays the information 
#about today's movies to the user. Utilizes Tkinter to create a simple GUI.
#Authors: Carly Shearer and Rachel Gaff
#Date: 9/24/2023

import requests
from tkinter import *
from bs4 import BeautifulSoup
from datetime import *

#Get information from URL by selecting certain HTML elements
hollywood_4 = requests.get('https://www.showtimes.com/movie-theaters/rc-hollywood-cinema-4-11840/')
hollywood_4_soup = BeautifulSoup(hollywood_4.text, 'html.parser')
hollywood_4_titles = hollywood_4_soup.select('.media-heading')
hollywood_4_times = hollywood_4_soup.select('.ticketicons')

amc_square = requests.get('https://www.showtimes.com/movie-theaters/amc-security-square-8-8327/')
amc_square_soup = BeautifulSoup(amc_square.text, 'html.parser')
amc_square_titles = amc_square_soup.select('.media-heading')
amc_square_times = amc_square_soup.select('.ticketicons')

cinemark_egyptian = requests.get('https://www.showtimes.com/movie-theaters/cinemark-egyptian-24-and-xd-6250/')
cinemark_egyptian_soup = BeautifulSoup(cinemark_egyptian.text, 'html.parser')
cinemark_egyptian_titles = cinemark_egyptian_soup.select('.media-heading')
cinemark_egyptian_times = cinemark_egyptian_soup.select('.ticketicons')

x = datetime.now()
remove_date = x.strftime('%a') + ', ' + x.strftime('%b') + ' ' + x.strftime('%d') + ': '

movieList = []

class Movie:
  def __init__(self, theater, title, time):
    self.theater = theater
    self.title = title
    self.time = time

  def __str__(self):
    return f'{self.theater}: {self.title} at{self.time}'
  
  def __repr__(self): 
    return f'{self.theater}: {self.title} at{self.time}' 

#Scrape information from websites, remove unneccessary data
def create_hollywood_4_list(titles):
    for i, item in enumerate(titles):
        title = item.getText().strip().replace('\n', '').replace('\r', '').replace('Watch Trailer', '').replace('                       ', '')
        time = hollywood_4_times[i].getText().strip().replace('Regular Showtimes', '').replace('\n', ' ').replace(remove_date, '')
        movieList.append(Movie('Hollywood 4', title, time))
    return movieList

def create_amc_square_list(titles):
    for i, item in enumerate(titles):
        title = item.getText().strip().replace('\n', '').replace('\r', '').replace('Watch Trailer', '').replace('                       ', '')
        time = amc_square_times[i].getText().strip().replace('Regular Showtimes', '').replace('\n', ' ').replace(' (Reserved Seating / Closed Captions / Recliner Seats)', '').replace('(Reserved Seating / Recliner Seats)', '').replace(remove_date, '')
        movieList.append(Movie('AMC Square 8', title, time))
    return movieList

def create_cinemark_egyptian_list(titles):
    for i, item in enumerate(titles):
        title = item.getText().strip().replace('\n', '').replace('\r', '').replace('Watch Trailer', '').replace('                       ', '')
        time = cinemark_egyptian_times[i].getText().strip().replace('Regular Showtimes', '').replace('\n', ' ').replace('(Reserved Seating / Recliner Seats)', '').replace('Cinemark XD Showtimes ', '').replace('D-BOX Showtimes ', '').replace('D-BOX / ', '').replace(remove_date, '')
        movieList.append(Movie('Cinemark Egyptian 24', title, time))
    return movieList

#Add movie objects created from scraped data to list
(create_hollywood_4_list(hollywood_4_titles))
(create_amc_square_list(amc_square_titles))
(create_cinemark_egyptian_list(cinemark_egyptian_titles))

def display_theater_1():
  theater_text.configure(text='')
  theater = theater_button_1.cget('text')
  count1 = 0
  for obj in movieList:
      if theater in obj.theater:
        theater_text['text'] += str(obj) +'\n'
      else:
        count1 += 1
        continue
  if count1 == len(movieList):
    theater_text.configure('Sorry, no movies showing at this theater! I hope they\'re still in business...')

def display_theater_2():
  theater_text.configure(text='')
  theater = theater_button_2.cget('text')
  count2 = 0
  for obj in movieList:
      if theater in obj.theater:
        theater_text['text'] += str(obj) +'\n'
      else:
        count2 += 1
        continue
  if count2 == len(movieList):
    theater_text.configure('Sorry, no movies showing at this theater! I hope they\'re still in business...')

def display_theater_3():
  theater_text.configure(text='')
  theater = theater_button_3.cget('text')
  count3 = 0
  for obj in movieList:
      if theater in obj.theater:
        theater_text['text'] += str(obj) +'\n'
      else:
        count3 += 1
        continue
  if count3 == len(movieList):
    theater_text.configure('Sorry, no movies showing at this theater! I hope they\'re still in business...')

def display_times():
  time_text.configure(text='')
  time = time_text_box.get()
  count = 0
  for obj in movieList:
    if time in obj.time:
      time_text['text'] += str(obj) +'\n'
    else:
      count+= 1
      continue
  if count == len(movieList):
    time_text.configure(text='No movies are showing at this time!')

def display_titles():
  title_text.configure(text='')
  title = title_text_box.get()
  count = 0
  for obj in movieList:
      if title in obj.title:
         title_text['text'] += str(obj) +'\n'
      else:
         count+= 1
         continue
  if count == len(movieList):
    title_text.configure(text='This movie is not showing at any theaters!')

window = Tk()
window.geometry("1900x1000")

welcome = Label(text='Welcome to Film Finder! Today\'s Date: ' + str(date.today()), font=('Fixedsys', 20))
subtitle = Label(text='Hello broke UMBC student. We know you\'re too lazy to drive more than 20 minutes from the school.' +
                 ' We know you\'ve waited until today buy your ticket. So we\'ve collected the important information for you!\n' + 
                 ' Just click on a theater or enter a time or title to find what you\'re looking for. Make sure you\'re back in time' +
                 'to do that assignment you\'re procrastinating on!', font=('', 12))

theater_button_1 = Button(text ="Hollywood 4", command = display_theater_1)
theater_button_2 = Button(text ="AMC Square 8", command = display_theater_2)
theater_button_3 = Button(text ="Cinemark Egyptian 24", command = display_theater_3)
theater_text = Label(text="No movies to see yet!", anchor="w", justify="left")
theater_button_1.place(x=50,y=100)
theater_button_2.place(x=150,y=100)
theater_button_3.place(x=250,y=100)
theater_text.place(x=50,y=150)

time_text_box = Entry()
time_label = Label(text='Please enter a time in standard format.')
time_button = Button(text='Enter', command = display_times, bg='green')
time_text = Label(text='No movies to see yet!', anchor="w", justify="left")
time_label.place(x=50,y=550)
time_text_box.place(x=50,y=575)
time_button.place(x=175,y=575)
time_text.place(x=50,y=600)

title_text_box = Entry()
title_label = Label(text='Please enter a title.')
title_button = Button(text='Enter', command = display_titles, bg='green')
title_text = Label(text='No movies to see yet!', anchor="w", justify="left")
title_label.place(x=50,y=700)
title_text_box.place(x=50,y=725)
title_button.place(x=175,y=725)
title_text.place(x=50,y=750)

welcome.pack()
subtitle.pack()
window.mainloop()
