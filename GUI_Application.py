import tkinter
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import json


# function to get weather
def func_get_weather(event=None):
    city = app_dropdown.get()
    api_key = "aada99debd82abd05fd240cee05d6750"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    server_data = requests.get(url)
    server_data_json = server_data.json()

    app_output.config(text="Hold on...")
    root.update_idletasks()


    temp = server_data_json ["main"] ["temp"]
    feels_like = server_data_json ["main"] ["feels_like"]
    humidity = server_data_json ["main"] ["humidity"]
    weather_desc = server_data_json ["weather"] [0] ["description"]
    icon_code = server_data_json ["weather"] [0] ["icon"]
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

    weather_icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url, stream=True).raw))


    app_output.config(text=f"The Temperature of {city} is: {temp}°C\n"
                            f"Feels like: {feels_like}°C\n"
                            f"Humidity: {humidity}%\n"
                            f"Weather Condition: {weather_desc.capitalize()}"
    )     #config send the temperature data to the GUI
    app_icon.config(image = weather_icon)
    app_icon.image = weather_icon


    output_frame.pack()
    app_icon.pack(pady=5)




# function to clear the output
def clear_output():
    app_output.config(text="")
    app_icon.config(image="")




root = tkinter.Tk()
root.geometry("900x700")
root.title("Weather App")


image_path = r"D:\python revision\GUI Application with Python Tkinter\bg-997x700.png"
image = Image.open(image_path)
bg_image = ImageTk.PhotoImage(image)

# bg_image = PhotoImage(file = image_path)

set_bg_image = tkinter.Label(root,image=bg_image)
set_bg_image.image = bg_image
set_bg_image.place(relheight=1, relwidth=1)


app_header = tkinter.Label(root, text="My Weather App", font=("Georgia", 24), bg="white", fg="blue", bd=2, relief="solid")
app_header.pack(pady=20)


app_label = tkinter.Label(root, text="Select City", font=("Georgia",15))
app_label.pack(pady=20)


cities = ["Mumbai", "Pune", "Hyderabad", "Bengaluru", "Goa", "Delhi", "Other cities..."]
app_dropdown = ttk.Combobox(root, values=cities, font=("Georgia", 10))
app_dropdown.pack(pady=20)

# Bind Enter key to the func_get_weather function
# <Return> refers to the Enter key in tkinter.
app_dropdown.bind("<Return>", func_get_weather)


app_weather_button = tkinter.Button(root, text="Get Weather", font=("Georgia", 12), command=func_get_weather)
app_weather_button.pack(pady=10)


output_frame = tkinter.Frame(root, highlightbackground="Light Green", highlightthickness=5)

app_output = tkinter.Label(output_frame, text="", font=("Georgia", 15))
app_output.pack(pady=5)


app_icon = tkinter.Label(root)
app_icon.pack(pady=5)



app_clear_button = tkinter.Button(root, text="Clear", font=("Georgia", 12), command=clear_output)
app_clear_button.pack(pady=10)




root.mainloop()