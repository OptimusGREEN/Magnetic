from bs4 import BeautifulSoup
import math, pyperclip, re, requests
import logging
from libs.magnetic import mglobals


path = mglobals.base_path

class Search(object):
    
    def __init__(self):
        
        self.query = None
        self.limit = None
        self.max_size = None
        self.magnets = []

    def x1377(self):
        try:
            main_link = "https://1377x.to/search/" + self.query + '/1/'
            main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml')

            self.limit_counter = 0
            page_links_soup = main_soup.findAll('a', attrs={'href': re.compile("^/torrent/")})
            for page_link in page_links_soup:
                if self.limit_counter < self.limit:
                    page_link = "https://1377x.to" + page_link.get('href')
                    page_request = requests.get(page_link, headers={'User-Agent': 'Mozilla/5.0'})
                    page_source = page_request.content
                    page_soup = BeautifulSoup(page_source, 'lxml')

                    title = page_soup.find('h1').text
                    seeder = page_soup.find('span', class_="seeds").text
                    leecher = page_soup.find('span', class_="leeches").text
                    size = page_soup.findAll('span')[15].text
                    date = page_soup.findAll('span')[19].text
                    magnet = page_soup.find('a', attrs={'href': re.compile("^magnet:?")}).get('href')

                    # row_position = self.tableTableWidget.rowCount()
                    # self.tableTableWidget.insertRow(row_position)
                    # self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(title))
                    # self.tableTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(seeder))
                    # self.tableTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(leecher))
                    # self.tableTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(size))
                    # self.tableTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(date))
                    # self.tableTableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem("1377x"))
                    self.magnets.append(magnet)
                    self.limit_counter = self.limit_counter + 1
        except Exception as e:
            logging.error(e)

    def kat(self):
        try:
            main_link = "https://kat.rip/usearch/" + self.query
            main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml')

            # titles_soup = main_soup.findAll('a', class_="cellMainLink")
            # seeders_soup = main_soup.findAll('td', class_="green center")
            # leechers_soup = main_soup.findAll('td', class_="red lasttd center")
            # sizes_soup = main_soup.findAll('td', class_="nobr center")
            # dates_soup = main_soup.findAll('td', class_="center", title=True)
            magnets_soup = main_soup.findAll('a', attrs={'href': re.compile("^magnet:?"), 'title': "Torrent magnet link"})

            # titles = []
            # seeders = []
            # leechers = []
            # sizes = []
            # dates = []
            # self.limit_counter = 0
            # for title in titles_soup:
            #     if self.limit_counter < self.limit:
            #         titles.append(title.text)
            #         self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for seeder in seeders_soup:
            #     if self.limit_counter < self.limit:
            #         seeders.append(seeder.text)
            #         self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for leecher in leechers_soup:
            #     if self.limit_counter < self.limit:
            #         leechers.append(leecher.text)
            #         self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for size in sizes_soup:
            #     if self.limit_counter < self.limit:
            #         sizes.append(size.text)
            #         self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for date in dates_soup:
            #     if self.limit_counter < self.limit:
            #         dates.append(date.text)
            #         self.limit_counter = self.limit_counter + 1
            self.limit_counter = 0
            count1 = 0
            for magnet in magnets_soup:
                if self.limit_counter < self.limit:
                    self.magnets.append(magnet.get('href'))
                    # self.limit_counter = self.limit_counter + 1
                    # count1 = count1 + 1
            if len(magnets_soup) > 0:
                return magnets_soup
            return
            # count2 = 0
            # while count2 < count1:
            #     row_position = self.tableTableWidget.rowCount()
            #     self.tableTableWidget.insertRow(row_position)
            #     self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(titles[count2]))
            #     self.tableTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(seeders[count2]))
            #     self.tableTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(leechers[count2]))
            #     self.tableTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(sizes[count2]))
            #     self.tableTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(dates[count2]))
            #     self.tableTableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem("KAT"))
            #     count2 = count2 + 1
        except Exception as e:
            logging.error(e)

    def nyaa(self):
        try:
            main_link = 'https://nyaa.si/?q=' + self.query
            main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml')

            titles_soup = main_soup.findAll('a', title=True, class_=False, attrs={'href': re.compile("^/view/")})
            seeders_soup = main_soup.findAll('td', class_="text-center")
            leechers_soup = main_soup.findAll('td', class_="text-center")
            sizes_soup = main_soup.findAll('td', class_="text-center")
            dates_soup = main_soup.findAll('td', class_="text-center")
            magnets_soup = main_soup.findAll('a', attrs={'href': re.compile("^magnet:?")})

            # titles = []
            # seeders = []
            # leechers = []
            # sizes = []
            # dates = []
            self.limit_counter = 0
            # for title in titles_soup:
            #     if self.limit_counter < self.limit:
            #         titles.append(title.text)
            #         self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for seeder in seeders_soup:
            #     if self.limit_counter < self.limit*6:
            #         seeders.append(seeder.text)
            #         self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for leecher in leechers_soup:
            #     if self.limit_counter < self.limit*6:
            #         leechers.append(leecher.text)
            #         self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for size in sizes_soup:
            #     if self.limit_counter < self.limit*6:
            #         sizes.append(size.text)
            #         self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for date in dates_soup:
            #     if self.limit_counter < self.limit*6:
            #         dates.append(date.text)
            #         self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # count1 = 0
            for magnet in magnets_soup:
                if self.limit_counter < self.limit:
                    self.magnets.append(magnet.get('href'))
                    self.limit_counter = self.limit_counter + 1
                    # count1 = count1 + 1
            if len(magnets_soup) > 0:
                return magnets_soup
            return

            # seeder1 = seeders[3]
            # seeders.pop(0)
            # seeders.pop(1)
            # seeders.pop(2)
            # seeders.pop(3)
            # seeders = seeders[6-1::6]
            # seeders.insert(0, seeder1)
            #
            # leecher1 = leechers[4]
            # leechers.pop(0)
            # leechers.pop(1)
            # leechers.pop(2)
            # leechers.pop(3)
            # leechers.pop(4)
            # leechers = leechers[6-1::6]
            # leechers.insert(0, leecher1)
            #
            # size1 = sizes[1]
            # sizes.pop(0)
            # sizes.pop(1)
            # sizes = sizes[6-1::6]
            # sizes.insert(0, size1)
            #
            # date1 = dates[2]
            # dates.pop(0)
            # dates.pop(1)
            # dates.pop(2)
            # dates = dates[6-1::6]
            # dates.insert(0, date1)

            # count2 = 0
            # while count2 < count1:
            #     row_position = self.tableTableWidget.rowCount()
            #     self.tableTableWidget.insertRow(row_position)
            #     self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(titles[count2]))
            #     self.tableTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(seeders[count2]))
            #     self.tableTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(leechers[count2]))
            #     self.tableTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(sizes[count2]))
            #     self.tableTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(dates[count2]))
            #     self.tableTableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem("Nyaa"))
            #     count2 = count2 + 1
        except Exception as e:
            logging.error(e)

    def rarbg(self):
        try:
            main_link = 'https://torrentapi.org/pubapi_v2.php?mode=search&search_string=' + self.query + '&token=lnjzy73ucv&format=json_extended&app_id=lol'
            main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml').text

            titles_soup = main_soup.split(",")
            seeders_soup = main_soup.split(',"')
            leechers_soup = main_soup.split(',"')
            sizes_soup = main_soup.split(',"')
            dates_soup = main_soup.split(',"')
            magnets_soup = main_soup.split('"')

            # titles = []
            # seeders = []
            # leechers = []
            # sizes = []
            # dates = []
            # self.limit_counter = 0
            # for title in titles_soup:
            #     if self.limit_counter < self.limit:
            #         if title.startswith('{"title":') or title.startswith('{"torrent_results":[{"title":'):
            #             title = title.replace('"', '')
            #             title = title.replace("{torrent_results:[{title:", '')
            #             title = title.replace('{title:', '')
            #             titles.append(title)
            #             self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for seeder in seeders_soup:
            #     if self.limit_counter < self.limit:
            #         if seeder.startswith('seeders":'):
            #             seeder = seeder.replace('seeders":', '')
            #             seeders.append(seeder)
            #             self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for leecher in leechers_soup:
            #     if self.limit_counter < self.limit:
            #         if leecher.startswith('leechers":'):
            #             leecher = leecher.replace('leechers":', '')
            #             leechers.append(leecher)
            #             self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for size in sizes_soup:
            #     if self.limit_counter < self.limit:
            #         if size.startswith('size":'):
            #             def convert_size(size):
            #                 if size == 0:
            #                     return "0B"
            #                 size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            #                 i = int(math.floor(math.log(size, 1024)))
            #                 p = math.pow(1024, i)
            #                 s = round(size / p, 2)
            #                 size = "%s %s" % (s, size_name[i])
            #                 sizes.append(size)
            #             size = int(size.replace('size":', ''))
            #             convert_size(size)
            #             self.limit_counter = self.limit_counter + 1
            # self.limit_counter = 0
            # for date in dates_soup:
            #     if self.limit_counter < self.limit:
            #         if date.startswith('pubdate":'):
            #             date = date.replace('pubdate":"', '')
            #             date = date.replace('+0000"', '')
            #             dates.append(date)
            #             self.limit_counter = self.limit_counter + 1
            self.limit_counter = 0
            # count1 = 0
            for magnet in magnets_soup:
                if self.limit_counter < self.limit:
                    if magnet.startswith("magnet:?"):
                        self.magnets.append(magnet)
                        self.limit_counter = self.limit_counter + 1
                        # count1 = count1 + 1

            # count2 = 0
            # while count2 < count1:
            #     row_position = self.tableTableWidget.rowCount()
            #     self.tableTableWidget.insertRow(row_position)
            #     self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(titles[count2]))
            #     self.tableTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(seeders[count2]))
            #     self.tableTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(leechers[count2]))
            #     self.tableTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(sizes[count2]))
            #     self.tableTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(dates[count2]))
            #     self.tableTableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem("RARBG"))
            #     count2 = count2 + 1
        except Exception as e:
            logging.error(e)

    def tpb(self):
        try:
            main_link = 'https://tpb.party/search/' + self.query + '/1/99/0/'
            main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml')
            sizes_soup = main_soup.findAll('font', class_="detDesc")
            magnets_soup = main_soup.findAll('a', attrs={'href': re.compile("^magnet")})
            self.limit_counter = 0
            for magnet in magnets_soup:
                if self.limit_counter < self.limit:
                    self.magnets.append(magnet.get('href'))
                    self.limit_counter = self.limit_counter + 1
        except Exception as e:
            logging.error(e)
    
    def magnetyze(self, search_query, sites=("rarbg", "x1377"), scrape_limit=10, max_file_size_gb=3):
        func_dict = {"tpb": self.tpb,
                     "rarbg": self.rarbg,
                     "x1377": self.x1377,
                     "kat": self.kat,
                     "nyaa": self.nyaa}
        self.limit = scrape_limit
        self.query = search_query
        self.max_size = max_file_size_gb
        for site in sites:
            scrape = func_dict[site]
            scrape()
