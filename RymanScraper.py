def scrape(page):
    string = "{}".format(page)
    response = requests.get('https://ryman.com/events/list/?tribe_event_display=list&tribe_paged='+string)
    soup = BS(response.text)
    wordsoup = soup.get_text()
    headliners = re.findall('(?<=\\n\\t\\t)[a-zA-Z &,’.0-9]+', wordsoup)
    dates = re.findall('(?<=\\n)[a-zA-Z]*day, \w* \d*, \d*', wordsoup)
    times = re.findall('\d{1,2}:\d\d.{7}', wordsoup)
    zipped = list(zip(headliners, dates, times))
    df = pd.DataFrame(zipped, columns=['Headliners', 'Date', 'Time'])
    return df
def RymanScraper(pages):
    scraped_df = pd.DataFrame()
    for i in range(1, pages):
        scraped_df = pd.concat([scraped_df, scrape(i)]);
    scraped_df = scraped_df.reset_index(drop=True)
    return scraped_df
RymanScraper(7)
