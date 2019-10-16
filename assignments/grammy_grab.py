import requests
import bs4
import json
DB = []


def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers, timeout=10)

def encodeAndStrip(string):
	return string.encode('utf-8').strip()

if __name__ == '__main__':
	for i in range(3,61,10):
		print("Number {}".format(i))
		try:
			if i % 10 == 1 and i != 11:
				url = 'https://www.grammy.com/grammys/awards/{}st-annual-grammy-awards'.format(i)
			elif i % 10 == 2 and i != 12:
				url = 'https://www.grammy.com/grammys/awards/{}nd-annual-grammy-awards'.format(i)
			elif i % 10 == 3 and i != 13:
				url = 'https://www.grammy.com/grammys/awards/{}rd-annual-grammy-awards'.format(i)
			else:
				url = 'https://www.grammy.com/grammys/awards/{}th-annual-grammy-awards'.format(i)
			res = grabSite(url)
			page = bs4.BeautifulSoup(res.text, 'lxml')
			for award in page.select(".view-grouping"):
				try:
					category = encodeAndStrip(award.select(".view-grouping-header")[0].getText())
					info = {"annualGrammy": i, "category": category}
					try:
						winner = encodeAndStrip(award.select("p")[0].select(".freelink-internal")[0].getText())
						individualAward = False
					except:
						winner = encodeAndStrip(award.select(".views-field-title")[0].getText())
						individualAward = True
						info['awardType'] = 'Individual'
						info['awardFor'] = winner

					if individualAward == False:
						info['awardType'] = 'Work'
						workTitle = encodeAndStrip(award.select(".views-field-title")[0].getText())
						info['awardFor'] = workTitle
					#winner = award.select(".flaggable")[0].getText().strip()
					info['name'] = winner
					DB.append(info)
					'''if individualAward == False:
						print("{} - {} - {}".format(category, winner, workTitle))
					else:
						print("{} - {}".format(category, winner))'''

				except:
					print("Error with award on {}".format(i))

		except:
			print("Problem with {}".format(i))
	with open("Database.csv", 'w') as fout:
json.dump(DB, fout)