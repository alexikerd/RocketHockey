import numpy as np





class Object():


    def __init__(self,x,y,radius):

        self.x = x
        self.y = y
        self.radius = radius
        self.vx = 0
        self.vy = 0

    def accelerate(self,friction,action):

        self.vx += 0
        self.vy += 0

    def move(self):

        self.x += self.vx
        self.y += self.vy

    def reset(self):

        pass


class Puck(Object):

    def __init__(self):
        super().__init__(0,0,10)

        self.type = 0
        self.vx = np.random.uniform(-10,10)
        self.vy = np.random.uniform(-10,10)


    def reset(self):

        self.x = 0
        self.y = 0
        self.vx = np.random.uniform(-10,10)
        self.vy = np.random.uniform(-10,10)


class Striker(Object):

    def __init__(self,x,y):
        super().__init__(x,y,15)

        self.type = 1
        self.xi = x
        self.yi = y

    def reset(self):

        self.x = self.xi
        self.y = self.yi
        self.vx = 0
        self.vy = 0



class Player():

    def __init__(self,name):

        self.name = name
    
    def __repr__(self):

        return self.name.title()






class Game():

    def __init__(self):

        self.height = 300
        self.width = 200
        self.friction = -0.1
        self.pucksize = 3
        self.strikersize = 15


        self.over = False
        self.score = [0,0]
        self.puck = Object(0,0,3)
        self.players = [Player(f'Player {i}') for i in range(2)]
        self.objects = [Striker(0,(self.height-(3*self.strikersize))*(2*i-1)) for i in range(2)] + [Puck()]



    def step(self,action):

        for obj in self.objects:

            obj.accelerate(self.friction,action)
            obj.move()

        self.handle_collision()



    def handle_collision(self):

        print(self.objects[-1].x,self.objects[-1].vx,self.objects[-1].y,self.objects[-1].vy)

        for obj in self.objects:

            if obj.x<=-1*self.width + obj.radius:
                obj.vx *= -1
                obj.x += -1*(obj.x + self.width - obj.radius)

            elif obj.x>=self.width - obj.radius:
                obj.vx *= -1
                obj.x += 2*(self.width - obj.radius - obj.x)



            if obj.y<=-1*self.height + obj.radius:
                obj.vy *= -1
                obj.y += -1*(obj.y + self.height - obj.radius)


            elif obj.y>=self.height - obj.radius:
                obj.vy *= -1
                obj.y += 2*(self.height - obj.radius - obj.y)





    def reset(self):

        self.over = False
        self.score = [0,0]


    def play_round(self):

        self.step(None)
        self.handle_collision()







        
        self.reset()





