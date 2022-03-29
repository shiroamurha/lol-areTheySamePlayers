from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bsoup
import requests



# browser and page init
def driver_webscrapping():
	browser = sync_playwright().start().webkit.launch()
	page = browser.new_page()

	# go to url
	page.goto("https://u.gg/lol/profile/br1/elinkgas13/overview") #https://u.gg/lol/profile/br1/s%20h%20iï%20r%20o/overview

	# clicking on update button for (obviously) uptading the infos
	page.locator(
		"button[class='update-button']"
	).click()

	summonerNames = list()

	# select the div with the names in three last matches 
	for matchCard_nthIterator in range(0, 3):
		summoner_names_selector = page.locator(
			f"div[class='match-history_match-card'] >> nth={matchCard_nthIterator}"
	
				).locator("div[class='group-four']"
					)
		
		# select team div of summoner names inside the match div
		for teamList_nthIterator in range(0,2):
			
			# for every summoner name in the team, summonerNames recieve each name 	
			for summonerName_nthIterator in range(0, 5):

				summonerNames.append(summoner_names_selector.locator(
					f"div[class='team-list'] >> nth={teamList_nthIterator}"
		
						# name extracted from <a title="summoner name here">
						).locator(f"a >> nth={summonerName_nthIterator}").get_attribute(name='title'))
	browser.close()

	open('tome.txt', 'w', encoding='utf-8').write(f'{summonerNames}')

	print(len(summonerNames))

#########################################
# 

isLiveGame = True

if isLiveGame:

	live_game = bsoup(requests.get('https://u.gg/lol/profile/br1/vanshader/live-game').text, features='html.parser').prettify()
	open('live_game.html', 'w', encoding='utf-8').write(str(live_game))
	
	print(live_game.find_all(
		'div',
		class_ = 'player-name',
		limit = 10

	))
################################################# riot api
#driver_webscrapping()

