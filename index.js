const express = require('express')
const path = require('path')
const app = express()
const hbs = require('hbs')
const multer = require('multer')
const upload = multer()
const {Trie} = require('regexgen');

app.set('views',path.join(__dirname,'views'))
app.set('view engine','hbs')

app.get('/',(req,res)=>{
    res.render('index')
})
app.post('/',upload.any(),(req,res)=>{
    //console.log(req.files)
    let t = new Trie
    var data = (req.files[0].buffer).toString('utf8')
    for(i in data){
        t.add(i)
    }
    var x = (t.toRegExp()).toString('utf8')
    //console.log(x[0]+x[x.length-1])
    x = setCharAt(x,0,'^(')
    x = setCharAt(x,x.length-1,')$')
    //res.send(x)
    res.render('index',{
        'showData' : true,
        'data' : x
    })
})
app.listen(4000,()=>{
    console.log('server start port 4000')
})


function setCharAt(str,index,chr) {
    if(index > str.length-1) return str
    return str.substring(0,index) + chr + str.substring(index+1)
}