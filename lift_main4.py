#--------------------------------------------------------------------------------------------------------------------------------
class Lift():
    current_floor=0 #class
#--------------------------------------------------------------------------------------------------------------------------------
    def __init__(self) :
        self.max_floor=6    #constructor
        self.min_floor=-1
        self.user_floor=0
#--------------------------------------------------------------------------------------------------------------------------------
    def lift_mechanics(self):
#--------------------------------------------------------------------------------------------------------------------------------        
        while(True):
            self.user_floor=int(input("enter lift numbe from 1 to 5: "))
            while(self.user_floor>6):
                print("you;ve entered wrong number")
                self.user_floor=int(input("enter lift numbe from 1 to 5: "))
#--------------------------------------------------------------------------------------------------------------------------------
            if self.user_floor== self.current_floor or self.user_floor==self.max_floor or self.user_floor==self.min_floor:
                print("you've on same floor orout of bound")
#--------------------------------------------------------------------------------------------------------------------------------                
            else:
                while self.current_floor<self.user_floor:
                     print("the lift is going up %d" %(self.current_floor))
                     self.current_floor=self.current_floor+1
                #print(f"lift is on up{self.user_floor} floor ")
#--------------------------------------------------------------------------------------------------------------------------------
                while self.current_floor>self.user_floor:
                     print("the lift is going down %d" %(self.current_floor))
                     self.current_floor=self.current_floor-1
            print(f"lift is on {self.user_floor} floor ")
#--------------------------------------------------------------------------------------------------------------------------------            
 
elev=Lift()              #instance of class
#--------------------------------------------------------------------------------------------------------------------------------  

while(True):
    lift_display='''    ======== LIFT ========
    |   5    *  *     4  |
    |        *  *        |
    |   3    *  *     2  |
    |        *  *        |
    |   1    *  *     0  | 
    ======================'''

    print(lift_display)
    elev.lift_mechanics()
#--------------------------------------------------------------------------------------------------------------------------------    