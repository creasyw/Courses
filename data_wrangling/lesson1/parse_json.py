import json
import requests

from pprint import pprint


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    #print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data

def filter_results(key):
    return filter(lambda k: k["name"].lower() == key.lower(),
                  query_by_name(ARTIST_URL,
                                query_type["simple"],
                                key)["artists"])

def main():
    results = filter_results("First Aid Kit")
    print "The bands called \"First Aid Kit\": ", len(results)

    results = filter_results("Queen")
    results = filter(lambda k: k.get("begin-area", None) is not None, results)
    print "The begin-area for Queen is: ", results[0]["begin-area"]["name"]

    results = filter_results("The Beatles")
    # The 'es' stands for spanish
    alias = [k for k in results[0]["aliases"] if k["locale"] == 'es']
    print "Spanish alias for beatles is: ", alias[0]["name"]

    results = filter_results("Nirvana")
    print "Nirvana disambiguation is: ", results[0]["disambiguation"]

    results = filter_results("One Direction")
    print "The form time of One Direction is: ", results[0]["life-span"]["begin"]


if __name__ == '__main__':
    main()
