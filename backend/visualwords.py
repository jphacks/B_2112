# coding: utf-8
from wordcloud import WordCloud
import re
from PIL import Image
import numpy as np

def word_cloud(number, text):
    print(number)
    mask = np.array(Image.open('images/'+ str(number) +'.png'))
    mask = np.where(mask == 0, 0, 255)
    
    # 作成したテキストの読み込み
    # with open('tweet_text_50.txt', 'r', encoding='utf-8') as f:
    #     text = f.read()


    # 除外したい単語
    # stop_text = ["ぴよぴよ", "ぽよぽよ"]

    # wordcloudの設定
    wordcloud = WordCloud(mask = mask,
                background_color="black",
                font_path="ipaexm.ttf",
                collocations = False,
                # stopwords = stop_text,
                colormap = 'Oranges',
                width=800,height=600).generate(text)
    print(wordcloud)

    #worcloudの作成
    wordcloud.to_file("../frontend/src/assets/my.png")

    #文字列に変換
    # im = np.array(Image.open("output\\"+ str(number)+".png"))

    # return wordcloud
    return None

# word = word_cloud(3)
# # im = np.array(Image.open("output\\2.png"))
# # print(type(im))
# # print(im.shape)
# word.to_file("test\\tweet_text_10.png")