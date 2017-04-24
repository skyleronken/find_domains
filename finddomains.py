#!/usr/bin/env python

# requirements
# pip install -e git://github.com/davedash/Alexa-Top-Sites.git#egg=alexa-top-sites
# pip install requests
#

import requests
import alexa

pr_formatter = "%-30s  %-70s  %-20s"
hl = '-' * 140

def get_bido_domains():

    req = requests.get('http://bido.com/api/liveAuctions/fullset?noAdult=1')
    doms = req.json().get('auctions')
    return doms

def get_alexa_sites(num=1000000):

    doms = alexa.top_list(num)
    return [i[1] for i in doms]

def find_trusted_domains(auction_doms, alexa_sites):
    trusted_doms = [i for i in auction_doms if i['name'] in alexa_sites]
    return trusted_doms

def find_categorized_domains(auction_doms):
    cat_doms = [i for i in auction_doms if i['category'] != "Uncategorized"]
    return cat_doms

def print_header(title):
    print title
    print pr_formatter % ('Name', 'Category', 'Site')

def print_domains(header, doms):
    print_header(header)
    print hl
    for dom in doms:
        print pr_formatter % (dom['name'], dom['category'], dom['link'])
    print hl
    print ''

def main():
    
    auction_doms = get_bido_domains()
    alexa_sites = get_alexa_sites()

    trust_doms = find_trusted_domains(auction_doms, alexa_sites)
    print_domains('Trusted Domains', trust_doms)

    cat_doms = find_categorized_domains(auction_doms)
    print_domains('Categorized Domains', cat_doms)

if __name__ == "__main__":
    main()