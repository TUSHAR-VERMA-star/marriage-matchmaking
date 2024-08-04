# Marriage Matchmaking App

This project is a Django-based API for managing user profiles and finding potential matches. It allows for the creation, retrieval, updating, and deletion of user profiles, and also supports finding matches based on dynamic criteria.

## Features

- Create, read, update, and delete user profiles
- Find potential matches based on criteria such as city, interests, gender, and age range
- Validate email addresses

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- virtualenv

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/TUSHAR-VERMA-star/marriage-matchmaking.git
    cd marriage-matchmaking-app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages**:
    ```bash
    pip install django djangorestframework
    ```

5. **Apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

### Running the Development Server

To start the Django development server, use the following command:

```bash
python manage.py runserver
```
### Running the Development Server

The API will be available at `http://127.0.0.1:8000/api/`.

### Testing the API

You can test the API using tools like Postman, cURL, or Django Rest Framework's browsable API.

## API Endpoints

### User Endpoints

1. **Create User**
    - **URL**: `/api/users/`
    - **Method**: `POST`
    - **Body**:
      ```json
      {
        "name": "John Doe",
        "age": 30,
        "gender": "M",
        "email": "johndoe@example.com",
        "city": "New York",
        "interests": "reading, traveling"
      }
      ```

2. **Read Users**
    - **URL**: `/api/users/`
    - **Method**: `GET`

3. **Read User by ID**
    - **URL**: `/api/users/<id>/`
    - **Method**: `GET`

4. **Update User**
    - **URL**: `/api/users/<id>/`
    - **Method**: `PUT`
    - **Body**:
      ```json
      {
        "name": "John Doe",
        "age": 31,
        "gender": "M",
        "email": "johndoe_updated@example.com",
        "city": "Los Angeles",
        "interests": "reading, traveling"
      }
      ```

5. **Delete User**
    - **URL**: `/api/users/<id>/`
    - **Method**: `DELETE`

6. **Find Matches for a User**
    - **URL**: `/api/users/<id>/matches/?city=San+Francisco&interests=traveling&interests=reading&min_age=25&max_age=35`
    - **Method**: `GET`

## Logic and Validation

### Matching Logic

The matching logic dynamically filters users based on query parameters. The criteria include:

- **City**: Matches the specified city.
- **Interests**: Matches any of the provided interests.
- **Gender**: Filters by specified gender.
- **Age Range**: Filters users within the specified age range.

### Validation

- **Email Validation**: Ensures the email field is a valid email address and is unique in the database.
- **Age Validation**: Converts age parameters to integers and ensures they are within valid ranges.
- **Dynamic Filtering**: Uses query parameters to filter matches dynamically based on the criteria provided.
