import bakaWebScrap as bak

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lst = ['gender bender']
    #lst = ['horror','lolicon','mature','mystery','romance','sci-fi']
    #lst = ['gender bender', 'horror', 'ecchi']
    obj = bak.baka()
    # obj.getCategories()
    obj.setInclude_tags(lst=lst)
    #tmp = obj.search_by_tags()
    tmp = obj.random_search_by_tag()
    for i in range(len(tmp)):
        print(i, ":")
        for j in tmp[i].values():
            print(j)
        print("\n")
