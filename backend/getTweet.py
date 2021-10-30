import tweepy
import config
import re

# 取得したキーを格納
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_SECRET

def mkTweetFile():
    # 認証
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    #params編集
    searchkey = '#読了 -filter:retweets'
    item_num = 20

    # api指定
    tweets = api.search_tweets(q=searchkey,lang='ja',result_type='mixed', count=item_num)

    # 変数宣言
    text = str('')
    num = 1

    # tweet読み込み
    for tweet in tweets:
        print('****************'+str(num)+'****************')
        print(tweet.text)
        s = str(tweet.text)
        text += s
        num += 1
    # リンク削除
    ret = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)", "" ,text)
    return ret
    # print(ret)

    # f = open('tweet_text.txt','w')
    # f.write(ret)
    # f.close()


# if __name__ == '__main__':
#     main()