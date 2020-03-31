from googleapiclient.discovery import build
import pprint

# add key1 to file google.key - would not be include in github
# acquire the key
def read_google_key():
    google_api_key = None
    try:
        with open('google.key','r') as f:
            list1 = f.readlines()
            google_api_key = list1[0].strip()
            engine_api_key = list1[1].strip()
    except:
        try:
            with open('../google.key','r') as f:
                google_api_key = list1[0].strip()
                engine_api_key = list1[1].strip()
        except:
            raise IOError('google.key file not found')

    if not google_api_key:
        # raise KeyError('Google key not found')
        # this would be removed when issueing- Note that Error 500: LIMITATIONS
        google_api_key = "AIzaSyBjGCyqUeXZT-AdZlWIf9auoK41_8kpxF8"
        engine_api_key = "010938217216454462722:unpmdeb1lhb"

    key_list = [google_api_key,engine_api_key]
    return key_list

def run_google_search(search_term):

    #define key
    api_key = read_google_key()[0]
    cse_key = read_google_key()[1]

    # resource object: send the request
    # first para: service- > customsearch
    # 2 para: version
    # 3 para: api_key

    # call cse() to create custom search resource object
    resource = build("customsearch", 'v1', developerKey=api_key).cse()

    # return the list of search results
    # q -> query string
    # cx - > engine id
    # call execute() will atcually executing the request

    result = resource.list(q=search_term, cx=cse_key).execute()

    results = []
    for each in result['items']:
        # print(each)
        results.append({
            'title': each['title'],
            'link': each['link'],
            'summary': each['snippet']})
    # pick the title and link
    # for item in result['items']:
    #     print(item['title'], item['link'], item['snippet'])


    # print("-----------------------{0} results are matched.-----------------------".format(len(result)))
    return results

    # pretty print all the result tags(JSON FOMATTED)
    # pprint.pprint(result)