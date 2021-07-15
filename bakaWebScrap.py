from bs4 import BeautifulSoup
import requests
import random

class baka(object):

    def __init__(self):
        self.all_genres = ['action', 'adult', 'adventure', 'comedy', 'doujinshi', 'drama', 'ecchi', 'fantasy', 'gender bender', 'harem', 'hentai', 'historical', 'horror', 'josei', 'lolicon', 'martial arts', 'mature', 'mecha', 'mystery', 'psychological', 'romance', 'school life', 'sci-fi', 'seinen', 'shotacon', 'shoujo', 'shoujo ai', 'shounen', 'shounen ai', 'slice of life', 'smut', 'sports', 'supernatural', 'tragedy', 'yaoi', 'yuri']

        self.include_tags = []
        self.exclude_tags = []

    def reset_include_tag(self):
        self.include_tags = []

    def reset_exclude_tag(self):
        self.exclude_tags = []

    def setInclude_tags(self, lst = []):
        if len(lst) == 0:
            return
        for genre in lst:
            if genre.lower() in self.all_genres:
                tmp = genre.split(" ")
                toAdd = ""
                for words in tmp:
                    toAdd += words.capitalize() + " "
                toAdd = toAdd[:-1]
                self.include_tags.append(toAdd)
    def setExclude_tags(self,lst = []):
        if len(lst) == 0:
            return
        for genre in lst:
            if genre.lower() in self.all_genres:
                tmp = genre.split(" ")
                toAdd = ""
                for words in tmp:
                    toAdd += words.capitalize() + " "
                toAdd = toAdd[:-1]
                self.exclude_tags.append(toAdd)
    def setSearchInfo(self,page=-1):
        base_url = "https://www.mangaupdates.com/series.html?"
        setPage = ""
        if page != -1 and page > 0:
            setPage = "page=" + str(page)
        exclude = ""
        include = ""
        if len(self.include_tags) != 0:
            include = "&genre="
            for i in self.include_tags:
                include += i.replace(" ","+") + "_"
            include = include[:-1]

        if len(self.exclude_tags) != 0:
            exclude = "&exclude_genre="
            for j in self.exclude_tags:
                exclude += j.replace(" ","+") + "_"
            exclude = exclude[:-1]
        addon = setPage + "&orderby=rating&perpage=5" + include + exclude
        return base_url + addon

    def getPageNumber(self):
        search_url = self.setSearchInfo()
        html_doc = requests.get(search_url).text
        soup = BeautifulSoup(html_doc,'lxml')
        totalPages = soup.find(name="span",class_="d-none d-md-inline-block")
        if totalPages == None:
            return None
        else:
            return int(totalPages.text.split(" ")[1][1:-1])

    def random_search_by_tag(self):
        pageLimit =self.getPageNumber()
        if pageLimit is None:
            print("No page number. Change your matches")
            return None
        else:
            randNum = random.randrange(1, pageLimit)
            print("Random number:",randNum)
            return self.search_by_tags(page=randNum)
    def search_by_tags(self,page = -1):
        search_url = ""
        assert page is not int
        if page == -1 or page < 0:
            search_url = self.setSearchInfo()
        else:
            search_url = self.setSearchInfo(page)

        print(search_url)
        html_page = requests.get(search_url).text
        soup = BeautifulSoup(html_page, "lxml")
        mangasParent = soup.find(name="div", id="main_content")
        mangasInfo = mangasParent.find_all(name="div", class_="col-12 col-lg-6 p-3 text")
        mangaCollection  = []

        for i in mangasInfo:
            newDic = {}
            newDic['title'] = i.find(name="b").text
            #print(i.find(name="b").text)
            newDic['desc'] = i.find(name="div",class_="text flex-grow-1").text
            #print(i.find(name="div",class_="text flex-grow-1").text)
            newDic['genres'] = i.find(name="div",class_="textsmall").text
            #print(i.find(name="div",class_="textsmall").text)
            web = i.find(name='a',href=True)
            newDic['web'] = web['href']
            imgT = i.find(name='img',src=True)
            if imgT is None:
                newDic['img'] = None
            else:
                newDic['img'] = imgT['src']
            rating = i.find_all(name='div', class_='text')
            count = 0
            for j in rating:
                if count == 3:
                    #print(j.text)
                    newDic['score'] = j.text
                    break
                count += 1

            mangaCollection.append(newDic)
        return mangaCollection

    def getCategories(self):

        htmlF = requests.get('https://www.mangaupdates.com/genres.html').text
        soup = BeautifulSoup(htmlF,'lxml')
        genresParent = soup.find("div",id="main_content")
        genresTitles = genresParent.find_all(name="div", class_="pl-3 pt-3 pr-3 releasestitle")
        with open('genres.txt','w') as ifstrm:
            for title in genresTitles:
               # print(title.text.lower())
                self.all_genres.append(title.text.lower())
                ifstrm.write(title.text.lower() + '\n')
            ifstrm.close()


