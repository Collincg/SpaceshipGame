import turtle, random, math

class Game:
    '''
    Purpose: to spawn a player in the SpaceCrast class, draw the moon's surface, initialize the world coordinates, spawn obstacles with obastacle class, and run the gameloop()
    Instance variables: 
        surface: surface of the moon
        asteroids: list of asteroids
    Methods: 
        __init__: initializes the class
        gameloop: loops the game and determines when it's over under what condition
    '''
    def __init__(self):
        #Bottom left corner of screen is (0, 0)
        #Top right corner is (500, 500)
        turtle.setworldcoordinates(0, 0, 500, 500)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.delay(0)
        
        self.surface = turtle.Turtle()
        self.surface.penup()
        self.surface.goto(-5,18)
        self.surface.pendown()
        #self.surface.right(90)
        self.surface.forward(530)
        

        self.asteroids = []
        player_px = random.uniform(100,400)
        player_py = random.uniform(250,450)
        player_vx = random.uniform(-4,4)
        player_vy = random.uniform(-2,0)

        self.player = SpaceCraft(player_px, player_py, player_vx, player_vy)
        #self.player.goto(250, 250)
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.left_turn, 'Left')
        turtle.onkeypress(self.player.right_turn, 'Right')
        for i in range(10):
            px = random.uniform(0,500)
            py = random.uniform(0,500)
            vx = random.uniform(-5,5)
            vy = random.uniform(-5,5)
            self.asteroids.append(Obstacles(px, py, vx, vy))
        turtle.tracer(0,0)
        self.gameloop()
        #These two lines must always be at the BOTTOM of __init__
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        crash = True
        for i in self.asteroids:
            i.move_obstacles()
            if (abs(self.player.xcor() - i.xcor()) <= 9) and (abs(self.player.ycor() - i.ycor()) <= 9):
                crash = False
        self.player.move()

        if (self.player.ycor() >= 20) and crash:
            turtle.ontimer(self.gameloop, 30)
            turtle.update()
        else:
            if (self.player.vx < 3 and self.player.vx > -3) and (self.player.vy < 3 and self.player.vy > -3) and crash:
                turtle.write("Successful landing!", font=("Ariel", 20, "normal"))
            else:
                turtle.write("You crashed!", font=("Ariel", 20, "normal"))



class SpaceCraft(turtle.Turtle):
    '''
    Purpose: 
        to create the spacecraft and the mechanics required for the player to move it
    Instance Variables:
        px: x-position
        py: y-position
        vx: x-velocity
        vy: y-velocity
        fuel_remaining: fuel remaining in spaceship
    Methods:
        __init__: initializes
        move: moves the spaceship to x and y coordinates and sets gravity
        thrust: propels the ship in the direction it's facing if there is remaining fuel
        left_turn: turns the spaceship left 15 degrees if there is fuel remaining
        right_turn: turns the spaceship right 15 degrees if there is fuel remaining
    '''
    def __init__(self, px, py, vx, vy):
        turtle.Turtle.__init__(self)
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        # self.vx = vx
        # self.vy = vy
        self.fuel_remaining = 40
        self.left(90)
        self.penup()
        self.speed(0)
        self.goto(px, py)
    def move(self):
        self.vy -= 0.0468
        px = self.xcor() + self.vx
        py = self.ycor() + self.vy
        self.goto(px,py)

    def thrust(self):
        if self.fuel_remaining > 0:
            self.fuel_remaining -= 1
            angle_pointing = math.radians(self.heading())
            self.vx += math.cos(angle_pointing)
            self.vy += math.sin(angle_pointing)
            print(self.fuel_remaining)
        else:
            print("Out of fuel")
    def left_turn(self):
        if self.fuel_remaining > 0:
            self.fuel_remaining -= 1
            self.left(15)
            print(self.fuel_remaining)
        else:
            print("Out of fuel")
    def right_turn(self):
        if self.fuel_remaining > 0:
            self.fuel_remaining -= 1
            self.right(15)
            print(self.fuel_remaining)
        else:
            print("Out of fuel")

class Obstacles(turtle.Turtle):
    '''
    Purpose: 
        to create the moving obstacles (asteroids) which the player must avoid
    Instance Variables:
        vx = x-velocity
        vy = y-velocity
    Methods:
        __init__: initializes
        move_obstacles: moves the obstacles and bounces them off the walls. 
    '''
    def __init__(self, px, py, vx, vy):
        turtle.Turtle.__init__(self)
        self.vx = vx
        self.vy = vy
        self.shape('circle')
        self.color('red')
        self.penup()
        self.speed(0)
        self.goto(px,py)
        self.goto(px, py)
        self.move_obstacles()
    def move_obstacles(self):
        self.speed(50)
        self.vy -= 0.1
        px = self.xcor()
        py = self.ycor()
        px += self.vx
        py += self.vy
        if px > 500:
            px = 500
            self.vx *= -1
        if px < 0:
            px = 0
            self.vx *= -1
        if py > 500:
            py = 500
            self.vy *= -1
        if py < 0:
            py = 0
            self.vy *= -1
        self.goto(px,py)




if __name__ == '__main__':
    Game()
    # for i in range(10):
    #     px = random.uniform(0,500)
    #     py = random.uniform(0,500)
    #     vx = random.uniform(-5,5)
    #     vy = random.uniform(-5,5)
    #     asteroids = Obstacles(px, py, vx, vy)