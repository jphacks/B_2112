# 書籍管理するお

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2021/07/JPHACKS2021_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
* コロナ禍で読書をする時間の増加し，購入した書籍を管理したい
* 出先で本を購入する際に自分が持っている本を買ってしまう
### 製品説明（具体的な製品の説明）
* 自分の所持している書籍の一覧確認
* 自分の書籍，#読了のツイートをwordcloudで可視化
### 特長
#### 1. SPA
####　　2. 自分の書籍を可視化
####　　3. リアルタイムの読了を可視化

### 解決出来ること
* 出先で同じ本を購入してしまうこと
### 今後の展望
* デプロイ
* 欲しい書籍の登録（メモ機能？）
### 注力したこと（こだわり等）
* wordcloudの表示画像を好みの動物で表示，テキストは自分の所持する書籍情報で
* 

## 開発技術
### 活用した技術
#### API・データ
* 楽天書籍検索API
* TwitterAPI

#### フレームワーク・ライブラリ・モジュール
* Virtualenv
* Python3
    * Flask
    * tweepy
    * Word Cloud
* Mysql
* Firebase
* Vue.js
    * Bootstrap-vue

#### デバイス
* macOS BigSur
* Windows10

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 指定した単語を含むツイートと白黒画像を用いてwordcloudで可視化
* 
