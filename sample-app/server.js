const express = require('express')
const app = express()
const port = 3000

let service = process.env.SERVICE_NAME || 'default'
app.get('/', (req, res) => res.send(`Hello World from ${service}!`))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))