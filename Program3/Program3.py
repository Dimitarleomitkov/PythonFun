def main():
	print("Dictionaries!");

	bag = dict();

	bag['money'] = 12;
	bag['candy'] = 3;
	bag['tissues'] = 75;

	print(bag);
	print(bag['tissues'] - 1);

	counts = dict();
	names = ["csev", "cwen", "csev", "zqian", "cwen"];

	for name in names:
		counts[name] = counts.get(name, 0) + 1;
	print(counts);

	print("Scan the book...");
	file_handler = open("The swamp was upside down.txt", 'r');

	words = file_handler.read().split();
	word_dictionary = dict();
	for word in words:
		word_dictionary[word] = word_dictionary.get(word, 0) + 1;
	max_key = max(word_dictionary, key = word_dictionary.get);
	print("Most used word:");
	print(max_key, word_dictionary[max_key]);
	print(sorted(word_dictionary.items(), key = lambda item: item[1], reverse = True)[:10]);

	

if __name__ == "__main__":
	main();



