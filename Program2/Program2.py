def main():
	print(type([1, 3, 8]));

	friends = ["Joe", "Rick", "Jo"];

	for i in range(len(friends)):
		print(f"Friend {i} is {friends[i]}.");

	my_list = [1, 3, 8] + friends;
	for item in my_list:
		print(item, end = ", ");

	print("");
	for item in my_list[:4]:
		print(item, end = ", ");

	print(dir(my_list));
	my_list[3:].sort();
	print(my_list);
	print(sum(my_list[:3]));
	print(sum(my_list[:3]) / len(my_list[:3]));

	print("");
	print("==================================================================");
	print("");

	file_handler = open("mbox-short.txt");
	for line in file_handler:
		if line.startswith("From"):
			line = line.rstrip();
			words = line.split();

			if len(words) > 2:
				print(words[2]);


if __name__ == "__main__":
	main();



