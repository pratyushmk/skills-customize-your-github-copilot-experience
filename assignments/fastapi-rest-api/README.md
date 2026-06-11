# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by defining endpoints, handling JSON requests and responses, and validating input data.

## 📝 Tasks

### 🛠️ Create a FastAPI app

#### Description
Set up a new FastAPI application with at least three REST endpoints to manage a collection of items.

#### Requirements
Completed program should:

- Use FastAPI to create an API application.
- Define endpoints for `GET /items`, `GET /items/{item_id}`, and `POST /items`.
- Store items in an in-memory list or dictionary.
- Return JSON responses with item data.
- Use Pydantic models for request validation and response schemas.
- Include appropriate HTTP status codes for success and error cases.

### 🛠️ Validate request data

#### Description
Use a Pydantic model to validate incoming request payloads for creating new items.

#### Requirements
Completed program should:

- Define a `Item` schema with fields such as `name`, `description`, and `price`.
- Ensure `name` is a non-empty string and `price` is a positive number.
- Return a validation error when request data is invalid.
- Include example request body structure in the README.

### 🛠️ Handle missing items gracefully

#### Description
Implement error handling for requests that reference an item ID that does not exist.

#### Requirements
Completed program should:

- Return a `404 Not Found` response for unknown item IDs.
- Include a JSON error message explaining the issue.
- Keep the API behavior consistent for missing resources.

#### Example request body

```json
{
  "name": "Notebook",
  "description": "A compact writing pad",
  "price": 12.50
}
```
