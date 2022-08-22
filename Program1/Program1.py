def main():
	file_handler = open("mbox-short.txt", 'r');
	line_counter = 0;
	
	print(file_handler);

	for line in file_handler:
		# print(line);
		line_counter += 1;

	print(line_counter);

	file_handler.seek(0);
	file_str = file_handler.read();
	
	print(len(file_str));

	print(file_str[:20]);

	file_handler.seek(0);

	for line in file_handler:
		# if line.startswith("From:"):
		# 	line = line.rstrip();
		# 	print(line);

		if "@uct.ac.za" in line:
			line = line.rstrip();
			print(line);

if __name__ == "__main__":
	main();



