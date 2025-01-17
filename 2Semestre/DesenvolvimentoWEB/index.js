var express = require('express');
var app = express();
app.use(express.static('./pages'));

const products = []
const users = []

const router = express.Router();
router.get('/api/products', (req, res) => {
    res.status(200).json(products);
})
router.post('/api/products', (req, res) => {
    var product = req.body
    products.id = 1
    products.push(product)
    res.status(201).json(product)
})

router.get('/api/users', (req, res) => {
    res.status(200).json(users);
})
router.post('/api/users', (req, res) => {
    var user = req.body
    user.id = 1
    users.push(user)
    res.status(201).json(user)
})

app.use(router)

const port = 3000;

app.get('/hello', (req, res) => {
    res.send('Hello World');
});

app.listen(port, () => {
    
    console.log('Server running on port ' + port);
});