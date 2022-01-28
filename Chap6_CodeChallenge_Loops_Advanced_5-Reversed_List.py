# Chapter 6 - Python Code Challenges
# Loops (Advanced) 5
# Reversed List

# For the final challenge, we are going to test two lists to see if the second list is the reverse of the first 
# list. There are a few different ways to approach this, but we are going to try a method that iterates through
# each of the values in one direction for the first list and compares them against the values starting from the 
# other direction in the second list. Here is what you need to do:

# 1. Define a function that has two input parameters for our lists
# 2. Loop through every index in one of the lists from beginning to end
# 3. Within the loop, compare the element in the first list at the current index against the element in the 
#    second list's last index minus the current index (OK that was actually the hint which I needed!). If there was 
#    a mistmatch, then the lists aren't reversed and we can return False
# 4. If the loop ended successfully, then we know the lists are reversed and we can return True. 

# Ok this is kinda motivating. I might not make it completly on first try, but I have a couple hunches. 

def reversed_list(lst1, lst2):
	for i in range(len(lst1)): # hahaha, this time I think I at least should get this one right, right? XD
		#if lst1[i] == lst2[-1-i]: Wrong... Also, they want to check False first.
		#if lst1[i] != range(len(lst2[-1] - i): - NO range. and inside brackets. Bahhhrgh.
		if lst1[i] != lst2[len(lst2) - 1 - i]: # cheated, looked at the solution.... sadpanda. REMEMBER!
			return False
	return True # This indentation. Why..  Why.... WHYY?! :((( 
			
# FUCK, both return True. What's wrong with my If statement? 
# Had to check it up, and sadly, the if statement isn't as close as I hoped. 


# INDENTATIONBRAINFUCK. Really. Yes. Really. 
# I have no clue why Else: return True will give the wrong output, and same without Else:, but with the return 
# True one additional step behind will do. This gives me serious brain wrinkles. 
# GDI. 

# Ok next lol. :D

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
