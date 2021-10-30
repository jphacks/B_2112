import firebase from 'firebase/compat/app'
import 'firebase/compat/auth'

const firebaseConfig = {
  apiKey: 'AIzaSyCTmfZriKMDsW2XmfGiiEIbkqKQiX-7THg',
  authDomain: 'jp-hackathon.firebaseapp.com',
  projectId: 'jp-hackathon',
  storageBucket: 'jp-hackathon.appspot.com',
  messagingSenderId: '25602127455',
  appId: '1:25602127455:web:7e5a3291e256902426cdea',
  measurementId: 'G-RS4VJC0Q6H'
}

firebase.getCurrentUser = () => {
  return new Promise((resolve, reject) => {
    const unsubscribe = firebase.auth().onAuthStateChanged(user => {
      unsubscribe()
      resolve(user)
    }, reject)
  })
}

firebase.initializeApp(firebaseConfig)
export default firebase
