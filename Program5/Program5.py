import socket
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen


cmd_get = "GET";
link = "http://data.pr4e.org/romeo.txt"
link2 = "http://www.dr-chuck.com/page1.htm"
link3 = "https://www.thecalculatorsite.com/cooking"
protocol = "HTTP/1.0\r\n\r\n";

def main():
	print("Network!\n----------------------------\n");
	
	# The hard way with sockets

	# my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	
	# try:
	# 	my_socket.connect(('data.pr4e.org', 80));
	# except:
	# 	print("[EXCEPTION!]: The host was not found.");

	# cmd = f"{cmd_get} {link} {protocol}".encode();

	# my_socket.send(cmd);
	# while True:
	# 	data = my_socket.recv(512);
	# 	if len(data) < 1:
	# 		break;
	# 	print(data.decode());
	# my_socket.close();

	# print("H in ordinal is ", ord('H'), '\n');

	# The easier way with urllib

	# file_handler = urllib.request.urlopen(f"{link}");

	# counted_words = dict();
	# for line in file_handler:
	# 	words = line.decode().split();
	# 	for word in words:
	# 		counted_words[word] = counted_words.get(word, 0) + 1;

	# print(sorted(counted_words.items(), key = lambda item: item[1], reverse = True));

	# file_handler = urllib.request.urlopen(f"{link2}");

	# for line in file_handler:
	# 	print(line.decode().strip());


	req = Request(
	    url=f'{link3}', 
	    headers={'User-Agent': 'Mozilla/5.0'}
	)

	file_handler = urllib.request.urlopen(req);

	for line in file_handler:
		print(line.decode());


if __name__ == "__main__":
	main();



