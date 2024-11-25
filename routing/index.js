import express from 'express';
import cors from 'cors';
import axios from 'axios';

const app = express();
const port = 3000;

// Configure CORS
app.use(cors({
  origin: ['http://localhost:8080', 'http://127.0.0.1:8080'],
  methods: ['GET', 'POST'],
  allowedHeaders: ['Content-Type'],
}));

app.use(express.json());

app.post('/upload/:user_id', async (req, res) => {
  const userId = req.params.user_id;

  try {
    const response = await axios.post(`http://localhost:8000/remove-background/${userId}`, req, {
      headers: {
        'Content-Type': req.headers['content-type']
      },
    });

    res.send(response.data.message);
  } catch (err) {
    res.status(err.response?.status || 500).send(err.response?.data?.error);
  }
});

app.listen(port);
