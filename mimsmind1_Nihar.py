import random
import sys

def get_length():
	if len(sys.argv) > 1:
		return int(sys.argv[1])
	else: 
		return 3

def number_of_rounds(length):
	return (2**length) + length

def mimsmind1_game():
	length = get_length()
	max_rounds = number_of_rounds(length)
	print("Let's play the mimsmind1 game. You have {} guesses.".format(max_rounds))
	correct_num = random.randint(0,10 ** length - 1)
	#correct_num = 8
	#print("Correct Number: " + str(correct_num))
	correct_num_lst = list(str(correct_num).rjust(length,'0'))
	msg = ""
	for chance in range(max_rounds):
		while(True):
			try:
				if chance == 0 and msg == "":
					user_input_str = input("Guess a {}-digit number: ".format(length))
					user_input = int(user_input_str)
				else: 
					user_input_str = input(msg)
					user_input = int(user_input_str)

				if len(user_input_str) != length:
					raise Exception()
				break
			except: 
				msg = "Invalid input. Try again: "
				continue
		user_input_lst = list(user_input_str)
		count_bulls = 0
		count_cows = 0
		user_correct_num_lst = correct_num_lst[:]
		for x in range(len(correct_num_lst)):
			if user_input_lst[x] == correct_num_lst[x]:
				count_bulls += 1
				user_correct_num_lst.remove(user_input_lst[x])
			elif user_input_lst[x] in user_correct_num_lst:
				count_cows += 1
		#correct_num_lst = correct_num_lst_copy[:]
		if count_bulls == length:
			print("Congratulations. You guessed the correct number in {} tries".format(chance + 1))
			break
		else:
			msg = str(count_bulls) + " bull(s), " + str(count_cows) + " cow(s). Try again: "
	else: 
		print("Sorry. You did not guess the number in {} tries. The correct number is {}.".format(max_rounds, correct_num))





def main():
	mimsmind1_game()


if __name__ == '__main__':
    main()
