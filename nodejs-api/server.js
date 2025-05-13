// nodejs-api/server.js

const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve static files for the dashboard
app.use(express.static(path.join(__dirname, 'views')));

// Endpoint to simulate fetching evaluated cloud configurations
app.get('/api/configs', async (req, res) => {
  try {
    // For demo purposes, assume the Python evaluation has dumped a JSON file
    // Alternatively, you could call a Python REST API endpoint here.
    // For now, we simulate with a static local file (or use axios to call another service)
    const configs = require('../python-module/sample_data/evaluated_configs.json');
    res.json(configs);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch configuration data.' });
  }
});

// Endpoint to serve the dashboard page
app.get('/dashboard', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'dashboard.html'));
});

app.listen(PORT, () => console.log(`Node.js API listening on http://localhost:${PORT}`));
