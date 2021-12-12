function Teni() {
    fetch('http://ec2-3-86-80-181.compute-1.amazonaws.com:8000/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: 'User 1'
        })
    }).then(res => {
        return res.json()
    })
    .then(data => console.log(data))
    .catch(error => console.log('ERROR MESSAGE'))

}
// fetch('http://ec2-3-86-80-181.compute-1.amazonaws.com:8000/', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({
//         name: 'User 1'
//     })
// }).then(res => {
//     return res.json()
// })
// .then(data => console.log(data))
// .catch(error => console.log('ERROR MESSAGE'))