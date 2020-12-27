#データサイエンスすこ
import random
#　library to use twitterapi easily
import tweepy

# assign twiter api key
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

#<<AWS Lambda>>
def lambda_handler(event, context):
    
    # university striing list
    ynu = ["横", "浜", "国", "立", "大", "学"] 
    ycu = ["横", "浜", "市", "立", "大", "学"]
    # faculty list
    ynu_faculty = ["教育","経済", "経営", "理工", "都市科" ]
    ycu_faculty =  ["国際教養","国際商", "理", "データサイエンス", "医" ]

    # string that should be liked and hashtaged
    winning_tickets = [
        "横横横横横横",
        "浜浜浜浜浜浜",
        "国国国国国国",
        "市市市市市市",
        "立立立立立立",
        "大大大大大大",
        "学学学学学学",
        "横国横国横国",
        "横市横市横市",
        "横浜市立大学",
        "横浜国立大学"
        ]

    # randomly extract from an integer value from 1 to 1000
    num = random.randint(1, 1000)

    #　When the extracted integer value is 451 or less
    if  num <= 451 :
        # use Yokohama City Univ
        univ = ycu
        faculty = ycu_faculty 
    else:
        # use Yokohama National Univ
        univ = ynu
        faculty = ynu_faculty 


    # allow duplication and randomly select 6 characters
    univ_word = ""
    for _ in range(6):
        univ_word +=  random.choice(univ)

    #randomly choose a faculty
    faculty_word = "学部"
    tmp =  random.choice(faculty)
    faculty_word  = tmp  + faculty_word 

    #If you get a hit, attach a hashtag
    if univ_word in winning_tickets :
        tweet_content = (f"""
        {univ_word} {faculty_word}
        
        #ycu 　#横浜市立大学
        #ynu 　#横浜国立大学
            """)
    else:
        tweet_content = f"{univ_word} {faculty_word}"

    #　call twitter api
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    #Create an API instance
    api = tweepy.API(auth)
    # Tweet !!!!
    api.update_status(tweet_content)

    # like the winning tweet
    for status in api.user_timeline(id='@'):
            tweet_id = status.id 
            if "#ycu" in status.text.split(" "):
                try:
                    api.create_favorite(tweet_id)
                except:
                    print('error')

if __name__ == "__main__":
    lambda_handler(None, None)