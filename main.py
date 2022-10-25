from random import *

card = [2, 3, 4, 6, 7, 8, 9, 10, 11] * 4
random.shuffle(card)



print("Привет, сыграем в Blackjack?")

count = 0

current = card.pop()
count += current
print(count)

current = card.pop()
count += current
print(count)

while True:

	c = input("Берем карту?: ")

	if c == 'y':
		current = card.pop()
		print("Вам досталась карта: ", current)
		count += current
		print("Сумма ваших очков: ", count)
		if count > 21:
			print("Вы проиграли")
			break
		if count == 21:
			print("Вы выиграли")
			break
		else:
		 	print("У вас: ", count, "очков")
	elif c == 'n':
		print("Вы набрали ", count, "очков")
		break
	if count > 21:
		print("Вы проиграли")
		break
	elif count == 21:
		print("Вы выиграли")
		break


print("До скорых встреч!")





