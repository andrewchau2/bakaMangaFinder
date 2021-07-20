import bakaWebScrap as bak


if __name__ == '__main__':

    includeTags = ['action', 'adventure'] #Add include tags here
    excludeTags = ['slice of life'] #Add exclude tags here
    obj = bak.baka()
    obj.setInclude_tags(lst=includeTags)
    obj.setExclude_tags(lst=excludeTags)

    # Optional. Default search settings is used if we don't set anything
    #obj.setSearch_options(perpage=5,orderby='rating')


    print("Page number: ", obj.getPageNumber()) #Gets the total page number for your search
    results = obj.search_by_tags()
    print(results)

    #results = obj.random_search_by_tag() #There is also a random search option based on your pref

