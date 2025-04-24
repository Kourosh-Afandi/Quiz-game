name=input("Please enter your name:")
print("Hello",name)
print("Let's start the quiz!")
print()
print()
print("Q1: What is the capital of France?")
print("A. London")
print("B. Berlin")
print("C. Paris")
print()
answer1=input("Your answer:").lower()
print()
score=0
if answer1=="c" or answer1=="paris":
	print("Correct!")
	score=score+1
else:
	print("Wrong! The correct answer is C. Paris")
print()
print()
print("Q2: What is 2 to the power of 3?")
print("A. 8")
print("B. 6")
print("C. 5")
print()
answer2=input("Your answer:").lower()
print()
if answer2=="8" or answer2=="a":
	print("Correct!")
	score=score+1
else:
	print("Wrong! The correct answer is A. 8")
print()
print()
print("Q3: What color do you get when you mix red and blue?")
print("A. Green")
print("B. Purple")
print("C. Yellow")
print()
answer3=input("Your answer:").lower()
print()
if answer3=="b" or answer3=="purple":
	print("Correct!")
	score=score+1
else:
	print("Wrong! The correct answer is B. Purple")
print()
print()
print("You got",score,"out of 3 correct.")
total_questions=3
percentage=(score/total_questions)*100
print("You answered",int(percentage),"% of the questions right!")
print()
if score==3:
	print("Great job!")
elif score==2:
	print("Well done!")
elif score==1:
	print("That's good!")
elif score==0:
	print("Try better next time!")