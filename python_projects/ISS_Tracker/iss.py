import requests, json, turtle


iss = turtle.Turtle()

def setup(screen):
    global iss
    screen.setup(1000, 500)
    screen.bgpic('earth.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    turtle.register_shape('../headfirstlearntocode-master/ch10/iss.gif')
    iss.shape('../headfirstlearntocode-master/ch10/iss.gif')

def move_iss(lat, lon):
    global iss
    iss.hideturtle()
    iss.penup()
    iss.goto(lat, lon)
    iss.pendown()
    iss. showturtle()

def track_iss():
    iss_url = 'http://api.open-notify.org/iss-now'
    response= requests.get(iss_url)

    if (response.status_code == 200):
        response_dictionary = json.loads(response.text)
        position = response_dictionary['iss_position']
        lat = float(position['latitude'])
        lon = float(position['longitude'])
        move_iss(lat, lon)
    else:
        print("Houston, we have a problem:", response.status_code)
    widget = turtle.getcanvas()
    widget.after(5000, track_iss)

def main():
    screen = turtle.Screen()
    setup(screen)
    track_iss()

if __name__ == '__main__':
    main()
    
turtle.mainloop()
