import express from 'express';
import axios from 'axios';

const app = express();
const port = 3000;

app.get('/upload', async (req, res) => {
  try {
    const response = await axios.get('http://localhost:8000/remove-background', {
      params: {
        image_path: req.params.image_path
      }
    });

    res.send(response.data.message);
  } catch (err) {
    res.status(err.response.status).send(err.response.data.error);
  }
});

app.listen(port);