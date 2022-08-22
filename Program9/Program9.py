import sqlite3

def main():
	print("Databases\n-------------------------------\n")

	conn = sqlite3.connect("emaildb.sqlite");
	cur = conn.cursor();

	cur.execute('DROP TABLE IF EXISTS Counts;');
	cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER);');

	file_name = input("Enter file name: ");
	if len(file_name) < 1:
		file_name = 'mbox-short.txt';

	file_handler = open(file_name);
	for line in file_handler:
		if not line.startswith('From: '):
			continue;
		pieces = line.split();
		email = pieces[1];
		cur.execute("SELECT count FROM Counts WHERE email = ?;", (email,));
		row = cur.fetchone();
		if row is None:
			cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1);", (email,));
		else:
			cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?;", (email,));

		conn.commit();

	sql_get_emails = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10;";

	for row in cur.execute(sql_get_emails):
		print(str(row[0]), row[1]);

	cur.close();


if __name__ == '__main__':
	main();