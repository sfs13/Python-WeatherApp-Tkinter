from tkinter import Label, Entry, Button, Tk
from sys import path

path.append('..\\source\\')
from WeatherApp import showWeather


root = Tk()
root.geometry('310x250')
root.resizable(
    'False',
    'False'
)
root.iconbitmap('../assets/logo.ico')
root.title('WeatherApp')

Label(
    root,
    text='Enter the city name:',
    font='Arial 15'
).pack()

entryPlace = Entry(
    root,
    width=25,
    font='Arial 13'
)
entryPlace.pack()

Button(
    root,
    text='Confirm',
    width=13,
    font='Arial 13',
    command=showWeather
).pack(pady=5)

labelWeather = Label(
    root,
    font='Arial 15'
)
labelWeather.pack()

root.mainloop()
