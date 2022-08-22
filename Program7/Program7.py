import urllib.request, urllib.parse, urllib.error
import json

service_url = "http://maps.googleapis.com/maps/api/geocode/json?"

def main():
	print("APIs\n----------------------------\n");

	while True:
		address = input("Enter location: ");
		if (len(address) < 1) or address is 'quit':
			break;

		url = service_url + urllib.parse.urlencode({'address': address});

		print("Retreiving", url);
		url_handle = urllib.request.urlopen(url);
		data = url_handle.read().decode();
		print("Retreived", len(data), " characters");

		try:
			js = json.loads(data);
		except:
			js = None;

		if not js or 'status' not in js or js['status'] != 'OK':
			print("====== Failure to retreive ======");
			print(data);
			continue;

		lat = js['results'][0]['geometry']['location']['lat'];
		lng = js['results'][0]['geometry']['location']['lng'];

		print("latitude:", lat, " longitude:", lng);
		location = js['results'][0]['formatted_address'];
		print(location);


	

if __name__ == "__main__":
	main();



