# AI-POWERED-RECOMMENDATION-ENGINE

##  Project Overview

The AI Recommendation Engine is a backend web application developed using Python and Flask.  
It demonstrates a simple yet effective content-based filtering system that generates movie recommendations based on user input.

The system processes a structured dataset and identifies similar items using genre-based similarity logic, exposed through a RESTful API.

##  Objective

The objective of this project is to design and implement a backend system that:

- Accepts user input (movie name)
- Processes structured dataset using Python
- Identifies similar movies using content-based filtering logic
- Returns recommendations in JSON format via REST API

##  Key Features

- RESTful API built using Flask  
- Lightweight AI-based recommendation logic  
- Dataset-driven content filtering  
- Fast and structured JSON responses  
- Easily extensible for other domains (products, books, music)  



##  System Workflow

1. User sends a movie name to the API  
2. System searches the dataset for the matching movie  
3. Extracts the genre of the identified movie  
4. Filters dataset based on the same genre  
5. Returns a list of similar movie recommendations  

## Dataset Overview

The dataset contains basic movie information used for generating recommendations:

| Title         | Genre   |
|--------------|--------|
| Inception     | Sci-Fi |
| Interstellar  | Sci-Fi |
| The Matrix    | Sci-Fi |
| Titanic       | Romance |
| The Notebook  | Romance |
| Avatar        | Sci-Fi |
| Joker         | Drama  |
| Avengers      | Action |
| Iron Man      | Action |

---

##  API Endpoints

###  Base Endpoint

GET /


**Response:**

AI Recommendation Engine API is running


---

###  Recommendation Endpoint

GET /recommend?movie=Inception


---

### Sample API Response

```json
{
  "input_movie": "Inception",
  "recommendations": [
    "Interstellar",
    "The Matrix",
    "Avatar"
  ]
}
# Technologies Used
Python 3.x
Flask
Pandas
REST API Architecture
