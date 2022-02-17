from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from services import MatchingValuesService

class WordComparer(BaseModel):
    values: Optional[list] = None
    options: Optional[list] = None
    

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "please use /docs or /words_comparer with POST method",
        "urls": ["https://word-comparer.herokuapp.com/words_comparer", "https://word-comparer.herokuapp.com/docs"]
        }

@app.get("/words_comparer")
async def get_compare_words():
    return {
        "message": "please use /docs or /words_comparer with POST method",
        "urls": ["https://word-comparer.herokuapp.com/words_comparer", "https://word-comparer.herokuapp.com/docs"]
        }

@app.post("/words_comparer")
async def compare_words(word_comparer: WordComparer):
    matching_service = MatchingValuesService(word_comparer.values, word_comparer.options)
    values, values_with_ratio = matching_service.get_each_value()
    return {
        "highest_value": values,
        "value_with_ratio": values_with_ratio
    }