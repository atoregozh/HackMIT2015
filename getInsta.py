import requests, json
import keys

ACCESS_TOKEN = keys.INSTA_ACCESS_TOKEN


def getUserId(name):
	url = "https://api.instagram.com/v1/users/search?q=" + name + "&access_token=" + ACCESS_TOKEN
	response = requests.get(url)

	if response.status_code == 200:
		data = json.loads(response.text)
		location_id = data["data"][0]["id"]
		return location_id
	return None

def getPicsOfUser(userid, count):
	url = "https://api.instagram.com/v1/users/" + userid + "/media/recent/?access_token=" + ACCESS_TOKEN + "&count=" + str(count)
	response = requests.get(url)

	picUrls = []
	if response.status_code == 200:
		data = json.loads(response.text)
		for i in xrange(count):
			picUrls.append(data["data"][i]["images"]["standard_resolution"]["url"])
		return picUrls
	return None

def main():
    #TEST
    userid = getUserId("jessicaalba")
    picUrls = getPicsOfUser(userid, 25)
    #print picUrls

if __name__ == "__main__":
    main()