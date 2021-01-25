"""
Author: Matas Sabaliauskas
GoodMourningFashion_Outreach
Instagram Automation Script: Commenting only
geckodriver 0.27.0
instapy 0.6.11
"""

import random
from instapy import InstaPy
from instapy import smart_run

# get a session!
insta_username = 'USERNAME CENSORED'
insta_password = 'PASSWORD CENSORED'
session = InstaPy(username=insta_username, password=insta_password)
#session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
#session = InstaPy(username='GoodMourningFashion_Outreach', password='GoodMorning123!', proxy_address='1.0.0.96',proxy_port='80', headless_browser=True)


with smart_run(session):
    #All hashtags:

    hashtags = ['influencer', 'influencerswanted', 'streetfashionstyle', 'streetfashion',
                'londonfashion', 'londonfashionista', 'londonfashionweek', 'ukmodels',
                'londonfashionbloggers', 'londonfashionstylist', 'ukfashionblogger', 'ukfashion', 'ootd', 'instafashion'
                ]

    # General Hashtags:
    '''
    hashtags = ['brand', 'hoodies', 'hoodiestyle', 'kstyle',
                       'asianfashion', 'koreanfashion', 'koreanstyle', 'ulzzang', 'kfashion',
                       'ulzzanggirl', 'seoulfashion', 'streetstyle', 'fashionblogger', 'InstaStyle', 'fashionpost',
                       'menstyle', 'womenfashion', 'loveforfashion', 'fashionforeveryone', 'fashionstatement', 'OOTD',
                       'seoulfashion', 'koreanclothes', 'cutestyle', 'kpopgirl', 'koreanlooks','streetstyle',
                       'koreanoutfit', 'outwear', 'ulzzangs', 'ulzzangstyle', 'dailyootd', 'koreanbeauty',
                        'influencersofinstagram','influencers','influencer','instagram','blogger','influencerstyle',
                        'instagood','follow','love','influencermarketing','fashionblogger',
                        'like','beauty','photography','style','model','influencerswanted','photooftheday','bloggers',
                        'youtubers','influencerdigital','bloggerstyle','likeforlikes',
                        'lifestyle','youtube','youtuber','picoftheday','instadaily','followforfollowback','bhfyp','fashion',
                        'beautiful','art','me','smile','ootd','followme','moda','myself','cute',
                        'happy','instalike','photo','girl','makeup','likes','instafashion','fashionstyle','f','likeforfollow',
                        'likeforlike','selfie','nature','life','portrait','photoshoot','summer',
                        'shopping','followback','followers','followforfollow','outfit','look','comment','dress','design',
                        'photographer','handmade','travel','onlineshopping','fun','ecommerce','marketing',
                        'business','digitalmarketing','entrepreneur','ecommercebusiness','webdesign','seo','website',
                        'marketingdigital','shopify','online','amazon','socialmedia','onlineshop',
                        'onlinebusiness','branding','smallbusiness','startup','dropshipping','socialmediamarketing',
                        'onlinemarketing','onlinestore','onlineboutique','shoppingonline','fashionista',
                        'sale','shop','shoponline','accessories','shoes','shoplocal','boutique'
                ]
                
    '''


    #Randomly chooses 20 hashtags, that are used one by one
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]     #how many hashtags it will work through in total

    # general settings
    #session.set_do_follow(enabled=False, percentage=50, times=1)
    #session.set_do_like(enabled=True, percentage=1)
    session.set_do_comment(enabled=True, percentage=100)


    session.set_comments(["Hi :) We love your content! \nPlease drop us a DM if you're interested to collab \n-GoodMourning :heart:"],media='Photo')


    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=15000,
                                    max_following=2000,
                                    min_followers=100,
                                    min_following=50)

    # "likes" = general likes, "likes_h" = likes hourly, "likes_d" = likes daily
    session.set_quota_supervisor(enabled=True, peak_server_calls_hourly=30,
                                 sleep_after=["server_calls_h", "likes", "likes_h", "comments_h", "follows", "unfollows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=50,
                                 peak_likes_daily=100,
                                 peak_comments_hourly=50,
                                 peak_comments_daily=100,
                                 peak_follows_hourly=10,
                                 peak_follows_daily=10)

    #Chooses 10% of content to interact with
    session.set_user_interact(amount=1, percentage=15, randomize=True)
    session.set_dont_like(['sex', 'nude', 'india'])

    # activity
    # Chooses "amount" +-10 posts to interact with
    session.like_by_tags(my_hashtags, amount=100, media=None)