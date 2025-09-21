# Training Programme (Python + VUE CRUD)
## Task 1: Backend CRUD Development
In this task, you will extend the FastAPI + PostgreSQL backend to support full CRUD operations for both Employee and Department.

### Requirements
1. **CRUD Operations**
   - Implement Create, Read, Update, Delete endpoints for:
     - Department
     - Employee

2. **Validation Rules**
   - Employee must belong to an existing department.
   - Cannot create employee if `department_id` does not exist or is inactive.
   - Add unique constraints for department name and employee name.
   - Add `email` and `phone_no` filed to employee table:
      - Ensure that each employee’s email address and phone number are unique and follow proper formatting rules.

3. **Proper Error Handling**
    - Example: return `400 bad request` if department not found

4. **Extra**
   - Implement **soft delete** for both employees and departments. (Hint: use flag)
   - Document Upload(.pdf/.txt):
      - Add a `department_policy` field to department table.
      - Implement endpoints that allow users to upload and download document.

<br>

## Task 2: Vue Frontend Development
In this task, you will build a **Vue.js frontend** to interact with the backend APIs and demonstrate CRUD operations.

### Requirements
1. **Views**
   - Employee Management Page:
     - List employees in a table.
     - Create new employee form.
     - Edit employee details.
     - Delete employee.
   - Department Management Page:
     - List departments in a table.
     - Create new department form.
     - Edit department details.
     - Delete department.
   - `department_policy` Document Management:
     - Upload a document.
     - Display document content.
     - Provide download button for stored documents.

2. **Validation**
   - Ensure frontend validates required fields before sending API requests.
   - Prompt error messages when API calling fails.

3. **UI/UX**
   - Use simple form and table layout.
   - Add buttons for **Create**, **Edit**, **Delete/Deactivate**, **Upload/Download**.
   - Display success/error notifications.

4. **Extra**
   - Add filtering/search on employees (e.g., search by name or department).
   - Add pagination for large lists.

<br>

## Task 3: Containerize the Application
In this task, you will containerize both the backend and frontend, and prepare the project for deployment.

### Requirements
1. **Backend**
   - Write a `Dockerfile` for FastAPI backend.
   - Ensure database connection is configurable via environment variables.
   - Enable **CORS** for frontend-backend communication.

2. **Frontend**
   - Write a `Dockerfile` for Vue frontend.
   - Build the Vue project (`npm run build`) and serve with a lightweight server (e.g., nginx).

3. **Docker Compose**
   - Create a `docker-compose.yml` to run:
     - FastAPI backend
     - PostgreSQL database
     - Vue frontend
   - Ensure services can talk to each other via internal network.   

4. **Extra**
   - Add volume for Postgres and FastAPI backend to persist data.
   - Add `.env` file to manage environment variables.
   - Push images to Harbor.

<br>

## Common Tools
- [Docker](https://www.docker.com/products/docker-desktop/) and [Docker Compose](https://docs.docker.com/compose/): Containerize app
- [DBeaver](https://dbeaver.io/): Databse viewer
- [Postman](https://www.postman.com/): API testing
- [Node.js](https://nodejs.org/en/download): JavaScript runtime environment (please install using Windows installer .msi with version 21.7.3) 

<br>

## Expected Learning Outcomes:
- Understand CRUD operations in Python REST API.
- Practice frontend-backend integration with Vue.js.
- Containerize full app with Docker.
- Design and manage relational database schemas with PostgreSQL.
- Work with environment variables for configuration management.
- Learn how to handle `multipart/form-data` in FastAPI, file storage, and API integration with frontend.
- Gain experience with dependency management and virtual environments in Python.
- Learn how to structure a full-stack project with clear separation of concerns.
- Familiarize with API testing tools (e.g., Postman, curl) for verifying endpoints.
- Understand version control workflows (Git) in a collaborative project setting.