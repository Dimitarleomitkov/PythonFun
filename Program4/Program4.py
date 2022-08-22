import re

def main():
	print("Regex!\n");
	
	file_handler = open("mbox-short.txt");
	# for line in file_handler:
		# if re.search('^X-\S+:', line):
			# print(line.rstrip());

	# x = list();
	# file_handler.seek(0);
	# for line in file_handler:
	# 	numbers = re.findall('[0-9]+', line);
	# 	if len(numbers) > 0:
	# 		x.append(numbers);
	# print(x);

	# file_handler.seek(0);
	# counted_emails = dict();
	# emails = re.findall("\S+@\S+", file_handler.read());
	# for email in emails:
	# 	counted_emails[email] = counted_emails.get(email, 0) + 1;
	# print(sorted(counted_emails.items(), key = lambda item: item[1], reverse = True));

	file_handler.seek(0);
	numlist = list();
	for line in file_handler:
		stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line);
		if len(stuff) > 0:
			numlist.append(stuff[0]);
	print("Maximum: ", max(numlist));

	

if __name__ == "__main__":
	main();



