from firebase import firebase

firebase = firebase.FirebaseApplication('https://fir-test-10952.firebaseio.com/')
result = firebase.get('/DATABASE3',None)

print (result)
