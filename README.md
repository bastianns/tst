# Flask API with Authentication and Sentiment Analysis

A robust Flask API providing public and secure endpoints with API key authentication and sentiment analysis capabilities. Deployed on Vercel.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Requirements](#requirements)
- [Deployment](#deployment)
- [License](#license)

## Overview

This Flask API provides a scalable architecture for handling both public and authenticated requests, along with sentiment analysis capabilities. The application is optimized for Vercel deployment and includes comprehensive security measures.

## Features

- Public and secure endpoint access
- API key authentication
- Sentiment analysis simulation
- Vercel deployment support
- Comprehensive documentation
- Easy-to-use endpoints

## Endpoints

### 1. Public Endpoint

- **URL**: `/public`
- **Method**: `GET`
- **Authentication**: Not required
- **Description**: Returns a general message accessible to everyone
- **Example Response**:
  ```json
  {
      "message": "This is a public route accessible without authentication."
  }
  ```

### 2. Secure Endpoints

#### Protected Route
- **URL**: `/secure`
- **Method**: `GET`
- **Authentication**: API Key required
- **Headers**: `X-API-Key: your_api_key`

#### Sentiment Analysis
- **URL**: `/secure/get_sentiment_user`
- **Method**: `POST`
- **Authentication**: API Key required
- **Headers**: `X-API-Key: your_api_key`

## Authentication

The API uses API key authentication for secure endpoints. Keys should be included in the request header:
```
X-API-Key: your_api_key
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-api.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. Run the development server:
   ```bash
   flask run
   ```

## API Documentation

Detailed API documentation is available at `/docs` when running the server locally. For the deployed version, visit the documentation URL provided in your deployment settings.

## Requirements

- Python 3.8+
- Flask
- Flask-Cors
- python-dotenv
- Additional dependencies listed in `requirements.txt`

## Deployment

This API is configured for deployment on Vercel. Follow these steps to deploy:

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Configure your Vercel project:
   ```bash
   vercel init
   ```

3. Deploy:
   ```bash
   vercel deploy
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Acknowledgments

- Flask framework and its contributors
- Vercel for hosting
- All contributors to this project