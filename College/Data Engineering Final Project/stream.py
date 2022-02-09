# import library
import tweepy
from kafka import KafkaProducer
from datetime import datetime, timedelta
import csv
import pandas as pd

consumer_key = "Gg0FYnVBi1a9MeVR4cd7iBIHH"
consumer_secret = "i3whWfXsPi5uNjAXwskSQKmZobfgezo4SmK4R8hfL6WkWZGfdM"
access_token = "818938632782299136-VM0HUdQzBHdWsaWkXIfStkzSoKzRa0L"
access_token_secret = "IcKhsxWvCnLVqp2iigRw4tdNVqMsxFNWkGt5kXfQKhcfH"

# setup autentikasi
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# instansiasi API
api = tweepy.API(auth, wait_on_rate_limit=True)

# menyesuaikan waktu dengan waktu lokal (GMT +7 / UTC +7)
def normalize_time(time):
    mytime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    mytime += timedelta(hours=7)
    return (mytime.strftime("%Y-%m-%d %H:%M:%S"))

# instansiasi Kafka Producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10, 1))

# inisialisasi topik, kata kunci, serta batas maksimum query dan tweet
topic_name = 'windows_11'
search_key = "windows 11"
maxId = -1
maxTweets = 3000
tweetCount = 0
tweetsPerQuery = 500

# deklarasi file csv
csvFile = open("/home/stndb01/Documents/Data_Engineering/Proyek/"+search_key+".csv", "a+", newline="", encoding="utf-8")
csvWriter = csv.writer(csvFile)

# deklarasi list
tweet_id = []
tweet_username = []
tweet_text = []

# perulangan untuk mendapatkan tweet dengna API Twitter hingga limit yang ditentukan
while tweetCount < maxTweets:
    # mengambil data tweet pertama kali
    if maxId <= 0:
        # newTweets = api.search_tweets(q=search_key, lang="en", count=tweetCount, max_id=maxId)
        newTweets = api.search_tweets(q=search_key, lang="en", count=tweetCount)
    # mengambil data tweet kedua dan seterusnya
    newTweets = api.search_tweets(q=search_key, lang="en", count=tweetsPerQuery)

    # mengambil atribut tertentu dari suatu tweet
    for i in newTweets:
        record = str(i.user.id_str)
        record += ';'
        record = str(i.user.name)
        record += ';'
        # record += str(normalize_timestamp(str(i.created_at)))
        # record += ';'
        # record += str(i.full_text.encode('utf-8'))
        record += str(i.text.encode('utf-8'))
        record += ';'
        print(str.encode(record))
        producer.send(topic_name, str.encode(record))

        tweet_id.append(str(i.user.id_str))
        tweet_username.append(str(i.user.name))
        tweet_text.append(str(i.text.encode('utf-8')))
        tweets = [str(i.user.id_str), str(i.user.name), str(i.text.encode('utf-8'))]
        csvWriter.writerow(tweets)

    # menambah jumlah TweetCount dan MaxId
    tweetCount += len(newTweets)
    maxId = newTweets[-1].id

# mencoba mencetak
dictTweets = {"id":tweet_id, "username":tweet_username, "text":tweet_text}
df = pd.DataFrame(dictTweets)
# df
