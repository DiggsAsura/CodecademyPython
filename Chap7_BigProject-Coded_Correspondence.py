#print(letter)

#def caesar_cipher(string):
#	alpha = ['a', 'b', 'c,', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']
#	new_string = []
#	for i in string:
#		new_string.append(i)
#		if new_string[i] == alpha[i]:
#			print(i)
#	return new_string
  
#print(caesar_cipher(letter))
# Nope. I think I kind of have the right ideas, but we do not work with lists[] here, directly with strings instead. 

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
alpha = "abcdefghijklmnopqrstuvwxyz"
punct = "!.?,' "

translated_message = ""
for letter in message:
	if letter not in punct: # can i write it if letter not in punct?
		letter_value = alpha.find(letter)
		translated_message += alpha[(letter_value + 10) % len(alpha)]
	else:
		translated_message += letter
		
#print(translated_message)
		
message_for_v = "Hey man! Cool cipher, thanks for showing me V! You got anything else going on?"
trans_mes = ""
for letter in message_for_v:
	if letter not in punct:
		letter_value = alpha.find(letter)
		trans_mes += alpha[(letter_value - 10) % len(alpha)]
	else:
		trans_mes += letter

#print(trans_mes)


def decoder(message, offset):
	translate_message = ""
	for letter in message:
		if not letter in punct:
			letter_value = alpha.find(letter)
			translate_message += alpha[(letter_value + offset) % len(alpha)]
		else:
			translate_message += letter
	return translate_message
	
def coder(message, offset):
	translate_message = ""
	for letter in message:
		if not letter in punct:
			letter_value = alpha.find(letter)
			translate_message += alpha[(letter_value - offset) % len(alpha)]
		else:
			translate_message += letter
	return translate_message

first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print(decoder(first_message, 10))
print(decoder(second_message, 14))


# Part 5 - got a message without offset supplied. We need to brute force it. This will be done iterating over every chars in the alphabet!

coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1, 26):
	print("Offset: " + str(i))
	print("\t " + decoder(coded_message, i) + "\n")


