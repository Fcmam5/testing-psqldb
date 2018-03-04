const pgp = require('pg-promise')()
const connectionString = 'postgres://abdeldjalil:igmo@localhost:5432/conc_test'
const db = pgp(connectionString)

module.exports = {
  getAllCars: (req, res, next) => {
    db.any('select * from Cars')
      .then(function (data) {
        res.status(200)
          .json({
            message: 'Retrieved ALL ' + data.length + ' Cars',
            data: data,
          })
      })
      .catch(function (err) {
        return next(err);
      })
  },
  getPastMessages: skt => {
    db.any('select * from chat')
      .then( data => {
        return skt.emit('load messages', data)
      })
      .catch((err) => {
        return skt.emit('load messages', [])
      })
  },
  saveMessage: (msgObject, cb) => {
    db.none('INSERT INTO chat(username, message)' +
            'VALUES (${username}, ${message})', msgObject)
            .then(() => {
              // cb
              console.log("Done !");
            })
            .catch((e) => {
              console.error(e);
            })
  }
}
