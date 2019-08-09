import requests
from bs4 import BeautifulSoup
import csv

def get_stat(url):
    url = url.replace("http://", '', 1)
    url = url.replace("https://", '', 1)
    url = url.replace("www.", '', 1)

    to_get = "https://www.alexa.com/siteinfo/"+ url
    print(to_get)
    r = requests.get(to_get)
    soup = BeautifulSoup(r.text, "html.parser")

    rank_get = soup.find('div', attrs={'class': 'rankmini-rank'}) #page rank
    desc_get = soup.find('div', attrs={'class': 'descriptionText'}) #website description
    country_list = soup.find('div', attrs={'class': 'visitorList'}) #visitors list
    country_rank = soup.find('section', attrs={'class': 'countryrank'}) #rank based on countries
    site_metrics = soup.find('section', attrs={'class': 'flex'}) #page metrics


    rank_dirty = rank_get.text.strip()
    clean_rank = rank_dirty[1:]
    desc = desc_get.text.strip()

    print("Global page rank:", clean_rank,'\n')
    print("Page description:", desc, '\n')

    country_names = country_list.find_all('div', attrs={'id': 'countryName'})
    country_ranks = country_list.find_all('div', attrs={'id': 'countryPercent'})
    each_rank = country_rank.find_all('li')

    num_countries = int(len(country_names))
    print("Found stats for", num_countries, "countries" )
    
    countries = []
    countries_percentage = []
    countries_rank = []
    for x in range(num_countries):
        countries.append(country_names[x].text.strip()[3:])
        countries_percentage.append(country_ranks[x].text.strip())
        country_one_rank = each_rank[x].text.strip().split('#')[1]
    
    print(len(countries), len(countries_percentage), len(countries_rank) )
    # for x in range(num_countries):
    #     print(countries[x], ' : ' ,countries_percentage[x], ' : ', countries_rank[x])


    three_site_metrics = site_metrics.find_all('div', attrs={'class': 'small data'})
    print("three site metrics:", three_site_metrics)

    sites_linking_in = soup.find_all('div', attrs={'class': 'enun'})
    print("sites linkning in:", sites_linking_in)

    # ret = []
    # ret.append(url)
    # ret.append(desc)
    # ret.append(clean_rank)
    # ret.append(country_one)
    # ret.append(country_one_percent)
    # ret.append(country_one_rank)
    # ret.append(country_two)
    # ret.append(country_two_percent)
    # ret.append(country_two_rank)
    # ret.append(country_three)
    # ret.append(country_three_percent)
    # ret.append(country_three_rank)

    return ret


def main():
    print("Alexa script")
    website = raw_input("Enter site url: \n")
    get_stat(website)
    # readfile = open("sites.txt", "r")
    # writefile = open("results.txt", "w+")
    # sites_d = readfile.readlines()
    # sites = []
    # for s in sites_d:
    #     sites.append(s.rstrip())
    
    
    #print(sites)
    # print("Read ", len(sites), " sites")
    # readfile.close()
    # out_thing = []
    # for site in sites:
    #     print("fetching: ", site)
    #     out_thing.append(get_stat(site))

    # with open("output.csv",'w') as resultFile:
    #     wr = csv.writer(resultFile, dialect='excel')
    #     #for result in out_thing:
    #     wr.writerows(out_thing)

    # for result in out_thing:
    #     for metric in result:
    #         writefile.write(str(metric))
    #         writefile.write(' ')
    #     writefile.write('\n')
    # writefile.close()
    
    print("Done :)")
  
if __name__== "__main__":
  main()