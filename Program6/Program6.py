import xml.etree.ElementTree as ET
import json

data = '''
<person>
	<name>Chuck</name>
	<phone type="intl">
		+1 734 303 4456
	</phone>
	<email hide="yes"/>
</person>
'''

input = '''
<stuff>
	<users>
		<user x="2">
			<id>001</id>
			<name>Chuck</name>
		</user>
		<user x="7">
			<id>009</id>
			<name>Brent</name>
		</user>
	</users>
</stuff>
'''

data2 = '''
{
	"name": "Chuck",
	"phone": {
		"type": "intl",
		"number": "+1 734 303 4456"
	},
	"email": {
		"hide": "yes"
	}
}
'''

data3 = '''
[
	{
		"id": "001",
		"x": "02",
		"name": "Chuck"
	},
	{
		"id": "009",
		"x": "07",
		"name": "Chucky"
	}
]
'''

def main():
	print("Web Services\n----------------------------\n");
	
	tree = ET.fromstring(data);
	print("Name:", tree.find('name').text);
	print("Attr:", tree.find('email').get('hide'));
	
	print("\n");

	stuff = ET.fromstring(input);
	lst = stuff.findall('users/user');
	print("User count:", len(lst), "\n");

	for item in lst:
		print("Name:", item.find('name').text);
		print("Id:", item.find('id').text);
		print("Attribute:", item.get('x'));

	print("\n");

	info = json.loads(data2);
	# print(info);
	print("Name:", info['name']);
	print("Hide:", info['email']['hide'], "\n");

	info = json.loads(data3);
	print("User count:", len(info));
	for item in info:	
		print("Name:", item['name']);
		print("Id:", item['id']);
		print("Attribute:", item['x']);

if __name__ == "__main__":
	main();



