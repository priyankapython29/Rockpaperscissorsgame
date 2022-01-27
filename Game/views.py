from django.shortcuts import render
from django.http import HttpResponse
import random
from django import template

# Create your views here.

def checkwinner(p1choice,p2choice,request):
    if p1choice==p2choice:
        winner="None"
    elif (p1choice=="ROCK" and p2choice=="SCISSOR") or (p1choice=="SCISSOR" and p2choice=="PAPER") or (p1choice=="PAPER" and p2choice=="ROCK"):
        winner="User"
    elif (p2choice=="ROCK" and p1choice=="SCISSOR") or (p2choice=="SCISSOR" and p1choice=="PAPER") or (p2choice=="PAPER" and p1choice=="ROCK"):
        winner="Computer"
    else:
        winner="None"
    return winner
     

computerchoice=" "
userscore=0
computerscore=0
while True:
  print ("Do you want to play the game Y/N : ")
  ans=input()
  if ans=='Y':
    print ("choose any of the options-ROCK,PAPER,SCISSOR :")
    userchoice=input()
    print ("Player Selected :",userchoice)
    randomnum=random.randint(1,3)
    if randomnum==0:
      computerchoice="ROCK"
    elif randomnum==1:
      computerchoice="PAPER"
    elif randomnum==2:
      computerchoice="SCISSOR"
    
    print ("Computer Selected :",computerchoice)
    winner=checkwinner(userchoice,computerchoice)
    print ("Winner :",winner)
    if winner=="User":
      userscore+=1
    elif winner=="Computer":
      computerscore+=1
    
    print ("Player Score :",userscore )
    print ("computer Score :",computerscore)
  elif ans=='N':
    if userscore>computerscore:
      print ("Player is the winner")
    elif userscore<computerscore:
      print ("Computer is the winner")
    else:
      print ("Tie!!")
    
    print ("Game over")
    break
  else:
    print ("Invalid choice")
#return render(request,"Game/signup.html")
            
       
