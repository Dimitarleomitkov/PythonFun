import xml.etree.ElementTree as ET
import sqlite3

def Lookup(d, key):
	found = False;
	for child in d:
		if found:
			return child.text;
		if child.tag == 'key' and child.text == key:
			found = True;
	return None;

def main():
	print("Creating a database of a music library\n-------------------------------\n");

	conn = sqlite3.connect('music_library.sqlite');
	cur = conn.cursor();

	# Make fresh tables with executescript()
	cur.executescript(
'''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT UNIQUE
);

CREATE TABLE Album (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id INTEGER,
	title TEXT UNIQUE
);

CREATE TABLE Track (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT UNIQUE,
	album_id INTEGER,
	len INTEGER,
	rating INTEGER,
	count INTEGER
);

'''
	);

	file_name = input("Enter file name: ");
	if len(file_name) < 1:
		file_name = "Library.xml";

	xml_stuff = ET.parse(file_name);
	all_tracks = xml_stuff.findall('dict/dict/dict');
	print("Tracks found: ", len(all_tracks));

	for entry in all_tracks:
		if Lookup(entry, 'Track ID') is None:
			continue;

		name = Lookup(entry, 'Name');
		artist = Lookup(entry, 'Artist');
		album = Lookup(entry, 'Album');
		play_count = Lookup(entry, 'Play Count');
		rating = Lookup(entry, 'Rating');
		song_length = Lookup(entry, 'Total Time');
		
		if name is None or artist is None or album is None:
			continue;
		print(name, artist, album, play_count, rating, song_length);

		# Put them in the database
		cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?);", (artist,));
		cur.execute("SELECT id FROM Artist WHERE name = ?;", (artist,));
		artist_id = cur.fetchone()[0];

		cur.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?);", (album, artist_id));
		cur.execute("SELECT id FROM Album WHERE title = ?;", (album,));
		album_id = cur.fetchone()[0];

		cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, len, rating, count)
		 				VALUES (?, ?, ?, ?, ?)''', (name, album_id, song_length, rating, play_count));

		conn.commit();

	cur.close();


if __name__ == '__main__':
	main();