import httpx

BASE_URL = "https://comick-api-proxy.notaspider.dev/api"
r = httpx.get(f'{BASE_URL}/genre/?tachiyomi=true', follow_redirects=True)
rjson = r.json()

demographic_ids = {0: "shounen", 1: "Shoujo", 2: "Seinen", 3: "Josei", 4: "None"}
genre_map = {genre['id']: genre['name'] for genre in rjson}


def search_manhwa(title):    
    url= f'{BASE_URL}/v1.0/search/'
    response = httpx.get(f'{url}', params={"tachiyomi":True, "q": title, }, follow_redirects=True)
    response_json=response.json()
    return [{'hid': item['hid'], 'title': item['title'], 'slug': item['slug'], 'genres': [genre_map[id] for id in item['genres']], 
             'status': item['status'], 'demographic': demographic_ids.get(item['demographic'], "Unknown"), 'cover_url': item['cover_url']} for item in response_json]

#print(search_manhwa("Solo Leveling"))

def fetch_by_hid(hid, title):
    title_result = search_manhwa(title)
    matches =  [item for item in title_result if item['hid'] == hid ] 
    if not matches:
        return None
    else:
        return matches[0]
