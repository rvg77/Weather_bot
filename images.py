from flickrapi import FlickrAPI
import config


def get(tags):
    flickr = FlickrAPI(config.FLICKR_PUBLIC, config.FLICKR_SECRET, format='parsed-json')
    rnd = 1
    raw = flickr.photos.search(tags=tags[0:1], text=tags[1], tag_node='all', per_page=rnd, extras=config.extras)
    return raw['photos']['photo'][rnd - 1]['url_m']
