list_num = input("Enter numbers with spaces: ").split(" ")
numbers = list_num
for i in range(len(numbers)):
	numbers[i] = int(numbers[i])
numbers.sort()
print(numbers)


for i in range(1,max(numbers)+2):
	if i > 0 and i not in numbers:
		print(i)
		break
	else:
		continue





# for i in range(len(numbers)):
# 	if min(numbers) > 1:
# 		print(min(numbers) - 1)
# 		break
# 	elif min(numbers) < 0:
# 		for j in numbers:
# 			if j > 0:
# 				count_ = count_ + 1
# 				if count_ == j:
# 					continue
# 				else:
# 					print(count_)
# 					break
# 			else:
# 				continue
# 				



# for i in numbers:
# 	if min(numbers) > 0:
# 		count_ = count_ + 1
# 		if i == count_:
# 			continue
# 		else:
# 			print(count_)
# 			break
# 	else:
# 		if i > 0:
# 			count_ = count_ + 1
# 			if i == count_:
# 				continue
# 			else:
# 				print(count_)
# 				break
# 		
# if min(numbers) < 0:
# 	count_ = min(numbers)
# 	while count_ == :
# 		if count_ > 0:
# 			if count_ not in numbers:
# 				print(count_)
# 		else:
# 			count_ = count_ + 1
# 		min_num = True


# else:
# 	count_ = 1
# 	for i in numbers:
# 		if i == count_:
# 			count_ = count_ + 1
# 		else:
# 			print(count_)
# 			min_num = True




