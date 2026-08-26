from playsound import playsound
import random
from english_words import get_english_words_set
import matplotlib.pyplot as plt
target_x,target_y=random.randint(1,9),random.randint(1,9)
fig,ax=plt.subplots()
ax.plot([target_x],[target_y],'ro',label=f'target({target_x},{target_y})')
ax.set_ylim(0,10)
ax.set_xlim(0,10)
def onclick(event):
    if event.xdata is None or event.ydata is None:
        return
    ax.plot(event.xdata,event.ydata,'bx')
    dist=((event.xdata-target_x)**2 + (event.ydata-target_y)**2)**0.5
    if dist<0.5:
        ax.set_title("Captcha passed you may proceed! you can close this window to continue")
        playsound(r"C:\Users\Harshil Gandhi\Downloads\noice.mp3")
        choice1=int(input(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Select any one of this::::::::::::::::::::::::::::::::\
:::::::::::::\n1.To do list\n2.wordle\n3.contacts\n4.rock,paper,scissors\nEnter your choice:"))
        tasks=[]
        while True:
            if choice1==1:
                choice2=int(input("1.Add tasks\n2.view tasks\n3.remove tasks\n4.to exit the list manager\nEnter your choice:"))
                if choice2==1:
                    task=input("Enter the task to be added:")
                    tasks.append(task)
                    print(f"task {task} added successfully")
                elif choice2==2:
                    if not tasks:
                        print("No entry found.")
                    for i,task in enumerate(tasks,start=1):
                        print(f"{i}--->{task}")
                elif choice2==3:
                    if not tasks:
                        print("No task to be removed in the list")
                    
                    for i,task in enumerate(tasks,start=1):
                        print(f"{i}--->{task}")
                    ta=int(input("Enter the index of the word to be removed from the list:"))
                    tasks.pop(ta-1)
                    print(tasks)
                else :
                    print("thank you")
                    exit()
            elif choice1==2:
                all_words=get_english_words_set(['web2'],lower=True)
                three_letter_words=[word for word in all_words if len(word)==3]
                four_letter_words=[word for word in all_words if len(word)==4]
                five_letter_words=[word for word in all_words if len(word)==5]
                six_letter_words=[word for word in all_words if len(word)==6]
                choice2=int(input("difficulty level:\n1.Easy\n2.Medium\n3.hard\n4.master\nSelect difficulty :"))
                if choice2==1:
                    captcha_word=random.choice(three_letter_words)
                    user_input=input("Enter a three letter word")
                    if len(user_input)!=len(captcha_word):
                        print("error")
                    else:
                        feedback=""
                        for i in range(len(captcha_word)):
                            if user_input[i]==captcha_word[i]:
                                print(f"Green->user_input[i]")
                elif choice2==2:
                    captcha_word=random.choice(four_letter_words)
                    user_input=input("Enter a four letter word")
                elif choice2==3:
                    captcha_word=random.choice(five_letter_words)
                    user_input=input("Enter a five letter word")
                elif choice2==4:
                    captcha_word=random.choice(six_letter_words)
                    user_input=input("Enter a six letter word")
                else :
                    print("thank you")
                    
                    
    else:
        ax.set_title(f"Captcha failed")
        print("Better luck next time")
        playsound(r"C:\Users\Harshil Gandhi\Downloads\oof.mp3")
fig.canvas.draw()   
fig.canvas.mpl_connect('button_press_event',onclick)
plt.legend()
plt.show()
