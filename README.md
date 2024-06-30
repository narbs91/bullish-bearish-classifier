# Hugging Face Demo

This is a simple Python REST API built with [FastAPI](https://fastapi.tiangolo.com/) that demonstrates how to integrate a Hugging Face ML Model.  This App represents a simple API that incorporates the [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli) model from Hugging Face that will allow someone to classify a piece of text as being "bullish" or "bearish".

## Getting Started

1. Clone the repo

2. Install the dependencies via

```bash
pip install --no-cache-dir --upgrade -r requirements.txt
```

3. Run the app via

```bash
uvicorn app:app --port 7860
```

4. Open the Swagger Page : [localhost:7860/docs](http://localhost:7860/docs)

## Endpoint

### Classify

**Description**: Classifies a given statement as 'bullish' or 'bearish'

**Type** : GET

**Input Parameters** 
- `statement` : the statement to classify as 'bullish' or 'bearish'

**Response**: A json response with the result of the classification

Ex:

```javascript
{
    "data": "bullish"
}
```

**Sample Request**: 

```http://localhost:7860/classify?statement="hugging face is awesome"```