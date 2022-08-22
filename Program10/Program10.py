from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

def main():
	print("Crawl and store in DB\n-------------------------------\n")

	TWITTER_URL = "https://api.twitter.com/1.1/friends/list.json";

	conn = sqlite3.connect('spider.sqlite');
	cur = conn.cursor();

	cur.execute('''CREATE TABLE IF NOT EXISTS Twitter
					(name TEXT, retrieved INTEGER, friends INTEGER);''');


	ctx = ssl.create_default_context();
	ctx.check_hostname = False;
	ctx.verify_mode = ssl.CERT_NONE;

	while True:
		account = input("Enter a Twitter account or quit: ");

		if account == 'quit':
			break;

		if len(account) < 1:
			cur.execute("SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1;");
			try:
				account = cur.fetchone()[0];
			except:
				print("No unretrieved Twitter accounts found");
				continue;

		url = twurl.augment(TWITTER_URL, {'screen_name': account, 'count': '5'});
		
		print("Retrieving ", url);
		
		connection = urlopen(url, context = ctx);
		data = connection.read().decode();
		headers = dict(connection.getheaders());

		print("Remaining ", headers['x-rate-limit-ramaining']);

		js = json.loads(data);

		cur.execute("UPDATE Twitter SET retrieved = 1 WHERE name = ?;", (account,));

		# Information variables
		count_new = 0;
		count_old = 0;

		for user in js['users']:
			friend = user['screen_name'];
			print(friend);

			cur.execute("SELECT friends FROM Twitter WHERE name = ? LIMIT 1;", (friend,));

			try:
				count = cur.fetchone()[0];
				cur.execute("UPDATE Twitter SET friends = ? WHERE name = ?;", (count + 1,), (friend,));
				count_old += 1;
			except:
				cur.execute("INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1);", (friend,));
				count_new = count_new + 1;

		print("New accounts = ", count_new, "\nRevisited accounts = ", count_old);
		conn.commit();

	curr.close();


if __name__ == '__main__':
	main();