from clarifai.client import ClarifaiApi
# for main testing
import getInsta, keys


def getTaggedPics(pictureURLsList):

	taggedPics = []
	clarifai_api = ClarifaiApi()  # assumes environment variables are set.
	for picURL in pictureURLsList:
		result = clarifai_api.tag_image_urls(picURL)
		tagsPic = result['results'][0]['result']['tag']['classes']
		taggedPics.append(tagsPic)
	return taggedPics

def getTopTags(picsTagsList, N):

	tagCounts = {}
	for picTags in picsTagsList:
		for tag in picTags:
			if tag in tagCounts:
				tagCounts[tag] += 1
			else:
				tagCounts[tag] = 1

	n=0
	topNtags = []
	for topTag in sorted(tagCounts, key=tagCounts.get, reverse=True):
		print topTag, tagCounts[topTag]
		print n
		print "-----------------------------------"
		topNtags.append(topTag)
		if ( n>N ):
			break
		n+=1
	return topNtags


def main():
	ACCESS_TOKEN = keys.INSTA_ACCESS_TOKEN
	userid = getInsta.getUserId("beyonce", ACCESS_TOKEN)
	picUrls = getInsta.getPicsOfUser(userid, 25, ACCESS_TOKEN)
	picsTags = getTaggedPics(picUrls)
	top5Tags = getTopTags(picsTags, 7)
	print top5Tags



if __name__ == "__main__":
	main()