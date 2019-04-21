# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:04:33 2019

@author: Sanyam Jain
"""
def rock_paper_scissor(nim1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("Player One Wins!!")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print("Player Two Wins!!")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print("Player One Wins!!")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Scissor"):
        print("Player Two Wins!!")    
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
        print("Player One Wins!!")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Rock"):
        print("Player Two Wins!!")    
        

player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Paper',1:'Rock',2:'Scissor'}
while(1):
    num1=input("Player One , Enter Your Choice : ")
    num2=input("Player Two , Enter Your Choice : ")
    bit1=int(input("Player One , Enter the secret bit position : "))
    bit2=int(input("Player Two , Enter the secret bit position : "))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue ? Y/N : ")
    if(ch=='N'):
        break
    