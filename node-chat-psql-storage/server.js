const express = require('express')
const app = express()
const logger = require('morgan')
const bodyParser = require('body-parser')
const server = require('http').Server(app)
const io = require('socket.io')(server)

const ctr = require('./controller')
// Log requests to the console.
app.use(logger('dev'));

// Parse incoming requests data (https://github.com/expressjs/body-parser)
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));


app.use(express.static(__dirname + '/public'))

app.get('/', (req, res) => {
  return res.sendFile('index.html')
})

app.get('/api/all', ctr.getAllCars);

io.on('connection', socket => {
  ctr.getPastMessages(socket)

  socket.on('new message', data => {
    let msgObject = {
      username: data.username || 'unknown',
      message: data.message
    }
    ctr.saveMessage(msgObject)
    socket.broadcast.emit('message created', msgObject)
  })
})

server.listen(3000)
console.log("I'm Alive ! ");
