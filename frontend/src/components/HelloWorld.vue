<template>
  <div class="container">
    <div class="contents">
      <p></p>
    <div>
      <b-card no-body>
      <b-tabs pills card>
        <b-tab title="書籍一覧" active><b-card-text>
      <div class="block1">
        <div class="a1">
        <b-form-input v-model="search_text" placeholder="検索" style="margin-bottom:10px;"></b-form-input>
        <p></p>
        </div>
        <b-table
        striped
        hover
        :items="items"
        :filter="search_text"
        :filter-included-fields="['title', 'author', 'publisher']"
        ></b-table>
        </div>
      </b-card-text></b-tab>
      <b-tab title="Word Cloud"><b-card-text>
      <div class="block3">
        <div class="category-list">
          <a v-for="(image,i) in images" :key="i">
            <img :src="image" heigit="64" width="64"/>
          </a>
        </div>
        <div class="word1">
          <p></p>
          <input type='text' v-model='mask2' @change="getword2" placeholder="画像番号:自分" style="margin-bottom:10px;">
        </div>
        <div class="word2">
          <p></p>
          <input type='text' v-model='mask' @change="getword" placeholder="画像番号:Twitter" style="margin-bottom:10px;">
        </div>
        <img src = "@/assets/tw.png" class="wc2">
        <img src = "@/assets/my.png" class="wc2">
      </div>
      </b-card-text></b-tab>
      <b-tab title="書籍編集"><b-card-text>
        <div class="a1">
        <b-form-input v-model="add1" placeholder="isbn" style="margin-bottom:10px;"></b-form-input>
        <b-form-input v-model="add2" placeholder="日付" style="margin-bottom:10px;"></b-form-input>
        <b-button type="button" v-on:click="add">追加</b-button>
        <p></p>
        </div>
      </b-card-text></b-tab>
      </b-tabs>
      </b-card>
    </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios'
const URL = 'http://127.0.0.1:5000/'

export default {
  data () {
    return {
      value: null,
      name: null,
      randomNumber: 0,
      add1: '',
      add2: '',
      mask: '',
      mask2: '',
      word: '',
      search_text: '',
      images: [
        require('@/assets/images/1.png'),
        require('@/assets/images/2.png'),
        require('@/assets/images/3.png'),
        require('@/assets/images/4.png'),
        require('@/assets/images/5.png'),
        require('@/assets/images/6.png'),
        require('@/assets/images/7.png'),
        require('@/assets/images/8.png'),
        require('@/assets/images/9.png'),
        require('@/assets/images/10.png'),
        require('@/assets/images/11.png'),
        require('@/assets/images/12.png'),
        require('@/assets/images/13.png'),
        require('@/assets/images/14.png'),
        require('@/assets/images/15.png'),
        require('@/assets/images/16.png'),
        require('@/assets/images/17.png'),
        require('@/assets/images/18.png'),
        require('@/assets/images/19.png'),
        require('@/assets/images/20.png'),
        require('@/assets/images/21.png'),
        require('@/assets/images/22.png'),
        require('@/assets/images/23.png'),
        require('@/assets/images/24.png'),
        require('@/assets/images/25.png'),
        require('@/assets/images/26.png'),
        require('@/assets/images/27.png'),
        require('@/assets/images/28.png'),
        require('@/assets/images/29.png'),
        require('@/assets/images/30.png'),
        require('@/assets/images/31.png'),
        require('@/assets/images/32.png'),
        require('@/assets/images/33.png'),
        require('@/assets/images/34.png'),
        require('@/assets/images/35.png'),
        require('@/assets/images/36.png')
      ],
      items: [],
      getData: [],
      tableData: [],
      infoText: ''
    }
  },
  created () {
    this.value = localStorage.getItem('Key')
    localStorage.removeItem('Key')
    // console.log(this.value)
    this.name = this.value.substring(0, this.value.indexOf('@'))
    // console.log(this.name)
    var params = new FormData()
    params.append('name', this.name)
    axios.post(`${URL}api/bookinfo`, params)
      .then(response => {
        for (var i in response.data) {
          this.getData = {
            author: response.data[i].author,
            buydate: response.data[i].buydate,
            id: response.data[i].id,
            imageurl: response.data[i].imageurl,
            publisher: response.data[i].publisher,
            title: response.data[i].title
          }
          this.tableData.push({
            title: this.getData.title,
            author: this.getData.author,
            publisher: this.getData.publisher,
            buydate: this.getData.buydate
          })
          this.infoText += this.getData.title
          this.infoText += ' '
          this.infoText += this.getData.author
          this.infoText += ' '
          this.infoText += this.getData.publisher
          this.infoText += ' '
        }
        console.log(this.infoText)
        // console.log(this.getData)
      })
      .catch(error => {
        alert(error)
      })
  },
  mounted () {
    this.items = this.tableData
  },
  methods: {
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      // const path = `http//localhost:5000/api/random`
      axios.get(`${URL}api/random`)
        .then(response => {
          // console.log(response.data)
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    },
    getword: function () {
      this.randomNumber = this.mask
      // console.log(this.randomNumber)
      var params = new FormData()
      params.append('number', this.mask)
      console.log(params)
      axios.post(`${URL}api/word`, params)
        .then(response => {
          // this.wordcloud = response.data.wordcloud
          console.log(response.data)
          this.mask = ''
        })
        .catch(error => {
          console.log(error)
        })
      // this.wordcloud.to_file('wordcloud.png')
    },
    getword2: function () {
      var params = new FormData()
      params.append('number', this.mask2)
      params.append('text', this.infoText)
      axios.post(`${URL}api/u_word`, params)
        .then(response => {
          console.log(response.data)
          this.mask2 = ''
        })
        .catch(error => {
          console.log(error)
        })
    },
    add: function () {
      var params = new FormData()
      params.append('isbn', this.add1)
      params.append('date', this.add2)
      params.append('name', this.name)
      axios.post(`${URL}api/add`, params)
        .then(response => {
          alert('success')
          console.log(response.data)
          this.tableData = []
          for (var i in response.data) {
            this.getData = {
              author: response.data[i].author,
              buydate: response.data[i].buydate,
              id: response.data[i].id,
              imageurl: response.data[i].imageurl,
              publisher: response.data[i].publisher,
              title: response.data[i].title
            }
            this.tableData.push({
              title: this.getData.title,
              author: this.getData.author,
              publisher: this.getData.publisher,
              buydate: this.getData.buydate
            })
            console.log('1')
          }
          this.items = this.tableData
          this.add1 = ''
          this.add2 = ''
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  computed: {
    filter: function () {
      var tableData = []
      var book
      for (var i in this.tableData) {
        book = this.tableData[i]
        if (book.title.indexOf(this.word) !== -1) {
          tableData.push(book)
        }
      }
      return tableData
    }
  }
}

// var tableData = [{
//   title: '鬼滅の刃1',
//   author: 'トマト',
//   publisher: '集英社'
// },
// {
//   title: '鬼滅の刃2',
//   author: 'トマト',
//   publisher: '集英社'
// },
// {
//   title: '鬼滅の刃3',
//   author: 'トマト',
//   publisher: '集英社'
// },
// {
//   title: '鬼滅の刃4',
//   author: 'トマト',
//   publisher: '集英社'
// },
// {
//   title: 'アイウエオ',
//   author: 'うんこ',
//   publisher: '集英社'
// }]
</script>

<style scoped>
.contents {
  position: relative;
}
.block1 {
  float: middle;
}
.a1 {
  width: 50%;
  margin: 0 auto;
  max-width: 500px;
}
.block2 {
  float: left;
  position: relative;
  height: 70vh;
}
.word1 {
  float: left;
  width: 50%;
}
.word2 {
  float: right;
  width: 50%;
}
.category-list {
  float: bottom;
  margin: 0 auto;
  width: 75%;
}
.p{
  text-align: center;
}
.wc2{
  float:right;
  width:48%;
  height:auto;
  margin-bottom: 30px;
}
</style>
