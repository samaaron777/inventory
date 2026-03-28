# FastAPI Inventory Management API

## Description
This project is a FastAPI-based inventory management API that supports full CRUD (Create, Read, Update, Delete) operations on inventory items. It demonstrates RESTful API design, request handling, and data validation using Pydantic.


## Project Overview
This project is a lightweight RESTful API built using FastAPI for managing an inventory system. It allows users to create, retrieve, update, and delete items through structured HTTP endpoints, demonstrating core backend and API development concepts.



## Problem Statement
Managing inventory efficiently requires a structured backend system that supports CRUD operations with proper validation and error handling. This project provides a simple yet scalable API solution for handling such operations.



## Key Features
- Create new inventory items
- Retrieve items by ID
- Search items by name
- Update existing items
- Delete items
- Input validation using Pydantic
- Proper HTTP status codes and error handling



## Tech Stack
- Backend: FastAPI
- Language: Python
- Data Validation: Pydantic



## API Endpoints

### Get Item by ID
GET /get-item/{item_id}

### Get Item by Name
GET /get-item-by-name/?name=<item_name>

### Create Item
POST /create-item/{item_id}

### Update Item
PUT /update-item/{item_id}

### Delete Item
DELETE /delete-item?item_id=<id>


## Data Model

### Item Schema
- name: string
- price: float
- brand: optional string

### UpdateItem Schema
- name: optional string
- price: optional float
- brand: optional string



## How It Works
The API uses FastAPI to handle HTTP requests and route them to the appropriate functions. Data validation is handled using Pydantic models, ensuring that all incoming data meets the required structure.

Inventory data is stored in an in-memory dictionary, making this a lightweight and fast prototype suitable for demonstrating API design and functionality.



## Error Handling
- 404: Item not found
- 409: Item already exists
- Validation errors handled automatically by FastAPI



## Future Improvements
- Integration with a database (PostgreSQL / MongoDB)
- Authentication and authorization
- Pagination for large datasets
- Deployment using Docker
- API documentation enhancements



## Running the Application

1. Install dependencies:
```bash
pip install fastapi uvicorn

Run the server:
uvicorn working:app --reload
Open in browser:
http://127.0.0.1:8000/docs
