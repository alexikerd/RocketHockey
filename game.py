
config = {
    "height":50
    ,"width":25
    ,"friction":-0.1
    ,"pucksize":3
    ,"strikersize":5
}





class Object():


    def __init__(self,x,y,radius):

        self.x = x
        self.y = y
        self.radius
        self.vx = 0
        self.vy = 0

    def accelerate(self,friction,action):

        self.vx += 0
        self.vy += 0

    def move(self):

        self.x += self.vx
        self.y += self.vy


        
    def reset(self):



class Player():

    def __init__(self,name):

        self.name = name
    
    def __repr__(self):

        return name.title()



class Game():

    def __init__(self,config):

        self.height = height
        self.width = width
        self.friction = friction
        self.pucksize = pucksize
        self.strikersize = strikersize


        self.over = False
        self.players = 
        self.puck = Object(0,0,3)
        self.players = [Player(f'Player {i}') for i in range(2)]
        self.objects = [Object(0,(self.height-self.strickersize)*(2*i-1),self.strikersize) for i in range(2)] + [Object(0,0,self.pucksize)]


    def move(self,action):

        for player in self.players:

            player.accelerate(self.friction,action)

    def check_collision(self):

        for player in self.players:


    def step(self):

        for player in self.players:

            player.move()

        self.puck.move()




    def reset(self):

        self.over = False

        for player in self.players:

            player.reset()

    def play_round(self):

        while not self.over:







        
        self.reset()




