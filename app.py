from fastapi import FastAPI
from transformers import pipeline

# create a new FASTAPI app instance
app = FastAPI()

# initialize the zero-shot classification pipeline
pipe = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/classify")
def classify(statement:str):

    candidate_labels = ['bullish', 'bearish']
    
    # Generate the classificatin score of the input
    generated_score = pipe(statement, candidate_labels)
    
    # Output whether the classification score was bullish or bearish
    if generated_score['labels'][0] > generated_score['labels'][1]:
        return {"data" : candidate_labels[0]}
    else:
        return {"data" : candidate_labels[1]} 
