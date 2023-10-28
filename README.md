# Keras-OCR Server

This Docker container provides a Flask application for performing text recognition (OCR) using Keras-OCR.

## Example

Here's an example of how to use the OCR server with `curl`:

```bash
# Replace BASE64_IMAGE_DATA_HERE with your actual Base64 image data
curl -X POST -H "Content-Type: application/json" -d '{"image": "BASE64_IMAGE_DATA_HERE"}' http://localhost:5000/ocr
```

This will send a POST request to the OCR server and print the JSON response with OCR results.

```json
{
    "results": ["spam", "ham", "egg", "123"]
}
```

## Usage

### Using Docker

```bash
docker run -d -p 5000:5000 --name ocr yat1ma30/keras-ocr-server
```

### Using Python 3.9-3.11

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the server:

    ```bash
    python server.py
    ```

## Notes

-   This container is recommended for testing purposes.
-   Be mindful of security considerations.
