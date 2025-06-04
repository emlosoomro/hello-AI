print("hello i am AI bot. what is your name?")
name=input()
print("nice to meet you",name)
print("how are you feeling today. good or bad")
mood=input().lower()
if mood=="good":
    print("i am glad to hear that")
elif mood=="bad":
    print("sorry to hear that")
else:
    print("i see sometimes its hard to put feelings in words")
print("it was nice meeting you",name,"good bye")