import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Initialisation of the server, the client and the promisify
const app = express();
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Data of the products
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Function to get a product by its ID
function getItemById(id) {
  return listProducts.find(product => product.id === id);
}

// Function to reserve stock by its ID
async function reserveStockById(itemId, decrement = 1) {
  const currentStock = await getCurrentReservedStockById(itemId);
  const newStock = (currentStock !== null ? currentStock : getItemById(itemId).stock) - decrement;
  await setAsync(`item.${itemId}`, Math.max(newStock, 0));
}

// Function to get the current reserved stock by its ID
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock) : null;
}

// Initialisation stock of all products
async function initializeStock() {
  for (const item of listProducts) {
    await setAsync(`item.${item.id}`, item.stock);
  }
}

// Road to list all products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map(({ id, name, price, stock }) => ({
    itemId: id,
    itemName: name,
    price: price,
    initialAvailableQuantity: stock
  })));
});

// Road to list a product by its ID
app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId));
  if (!item) {
    res.json({ status: 'Product not found' });
  } else {
    const currentStock = await getCurrentReservedStockById(item.id) || item.stock;
    res.json({ ...item, currentQuantity: currentStock });
  }
});

// Road to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId));
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentStock = await getCurrentReservedStockById(item.id);
  if (currentStock === null || currentStock <= 0) {
    res.json({ status: 'Not enough stock available', itemId: item.id });
    return;
  }

  await reserveStockById(item.id);
  res.json({ status: 'Reservation confirmed', itemId: item.id });
});

// Start the server
const port = 1245;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
  initializeStock();
});
