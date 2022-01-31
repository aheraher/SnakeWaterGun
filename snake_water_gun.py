import pyfiglet
import random 
# from playsound import playsound 
from colorama import Fore 

def Game(com,user):
    if com == user :
        return 'same'
    
    elif com == 's':
        if user == 'w':
            return False 
        elif user =='g':
            return True 

    elif com == 'w':
        if user == 'g':
            return False 
        elif user =='s':
            return True 
    elif com == 'g':
        if user == 's':
            return False 
        elif user =='w':
            return True 

print(Fore.GREEN,"Com turn : (S)snake (W)water (G)gun :")
ran_no = random.randint(1,3)
if ran_no == 1:
    com = 's'
elif ran_no == 2:
    com = 'w'
elif ran_no == 3 :
    com ='g'

user=input("Your turn : (S)snake (W)water (G)gun :")

result = Game(com,user)
if result == 'same':
    print (Fore.BLUE,"Match tie ")
    
    ans = pyfiglet.figlet_format("TIE" )
    print(ans)


elif result:
    print(Fore.BLUE,"You win ")
    # playsound('C:\\Users\\Hp\\OneDrive\\Desktop\\myProjects\\ly.mp3') #C:\\Users\\Hp\\OneDrive\\Desktop\\myProjects\\Tera Hua Full Song _ Loveyatri _ Atif Aslam _ Aayush Sharma _Warina Hussain .mp3
    ans = pyfiglet.figlet_format("Win ")
    print(ans)
else :
    print(Fore.RED,"You loose")
    ans = pyfiglet.figlet_format("loose" )
    print(ans)

print(f"You choose is {user} ")
print(f"Com choose is {com} ")



