## Introduction to Object-Oriented Programming:

Object-Oriented Programming (OOP) is a way of organizing your code that focuses on creating reusable structures called objects.

## What is a Class?
*A class is a blueprint or template that defines the structure and behavior of objects.*  Understanding classes is fundamental to OOP.
When you create a class, you're essentially designing a new type of data structure. Python comes with built-in data types like integers (int), `strings (str)`, `lists (list)`, and `dictionaries (dict)`.

`Every class definition includes two main components:`

`Attributes` are the data that objects created from the class will store. These are like variables, but they belong to the object.

*Example:* For a User class, `attributes might include` name, email, age, and registration_date

`Methods` are functions that belong to the class and define what actions objects can perform.

class User:  `declares that we're creating a new class called User.` 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.is_active = True  # Default value for all users
    
The __init__ method is a special method called a constructor. It runs 

**Self**: automatically whenever you create a new object from the class.
When you define methods inside a class, the first parameter is always self. This parameter is a reference to the specific object instance that the method is being called on. In other words, self is how a method knows which object's data to work with.

Metaphot 
Class → the blueprint for one type of room
Objects → different rooms created from that blueprint
Attributes → items or information inside each room
Methods (def) → actions that can be performed in the room

For example:

### Encapsulation and Data Protection
Encapsulation is one of the four fundamental principles of Object-Oriented Programming. The term means "enclosing" or "wrapping" data and the methods that work on that data together within a single unit — the class. However, encapsulation goes beyond just bundling things together. It also involves controlling access to an object's data.

###  What is Web Mining?

Web mining is simply the process of gathering additional information from the internet to enrich your analysis.

**A Quick Note on Terminology**

You might hear the term `"parsing"` used interchangeably with web mining. When analysts say they're going to `"parse"` a website, they mean they're going to extract data from it. Same concept, different word!

#### HTML (Hypertext Markup Language) 
#### HTTP (Hypertext Transfer Protocol) 

# HTTP & HTTPS (Transfer Protocols) – Practical Notes

## What is a Protocol?

A **protocol** is a set of rules that computers use to communicate over the internet.

For websites, the communication protocol is **HTTP (Hypertext Transfer Protocol)**.

---

# Request–Response Cycle

Every interaction with a website follows the same simple process:

Browser (Client)
        │
        │ Request
        ▼
     Web Server
        │
        │ Response
        ▼
Browser displays webpage

**Example:**
When you enter:

```
https://example.com
```
Your browser sends an **HTTP request**, and the server responds with:

- HTML
- CSS
- Images
- Data

---

# HTTP vs HTTPS

| HTTP | HTTPS |
|------|--------|
| No encryption | Encrypted communication |
| Less secure | Secure communication |
| Data can be intercepted | Data is protected using encryption |

**Key Point:** Always use **HTTPS** when accessing websites or collecting data.

---

# Five Parts of an HTTP Request

## 1. HTTP Method

Defines the action you want to perform.

| Method | Purpose |
|---------|---------|
| GET | Retrieve data |
| POST | Send data |
| PUT | Update existing data |
| DELETE | Remove data |

**Examples**

Retrieve data:

```http
GET /products
```

Send login information:

```http
POST /login
```

---

## 2. Path

The **path** identifies the specific resource or page on a website.

Example URL:

```
https://example.com/products
```

- **Domain:** `example.com`
- **Path:** `/products`

Think of it like a building:

- Domain = Building address
- Path = Apartment number

---

## 3. HTTP Version

Specifies which version of HTTP is being used.

Examples:

- HTTP/1.1
- HTTP/2

This is usually handled automatically by the browser.

---

## 4. Request Headers

Headers provide additional information about the request.

Examples include:

- Browser type (`User-Agent`)
- Preferred language
- Cookies
- Authentication information
- Accepted content types

Headers help the server understand how to respond appropriately.

---

## 5. Request Body

The request body contains the data sent to the server.

Usually included in **POST** requests.

Examples:

- Username and password
- Search form data
- Uploaded files

**Note:** GET requests typically do **not** have a request body.

---

# Why This Matters for Data Science

Understanding HTTP helps you:

- Use APIs
- Perform web scraping
- Automate data collection
- Debug web requests
- Understand browser-server communication

These skills are essential for many machine learning and data science projects.

---

# Typical Web Scraping Workflow

```text
Python Script
      │
      ▼
HTTP GET Request
      │
      ▼
Web Server
      │
      ▼
HTML Response
      │
      ▼
BeautifulSoup / pandas
      │
      ▼
Extract useful data
```

---

# Typical API Workflow

```text
Python Script
      │
      ▼
HTTP GET Request
      │
      ▼
REST API
      │
      ▼
JSON Response
      │
      ▼
Python Dictionary
      │
      ▼
Data Analysis / Machine Learning
```

---

# Key Takeaways

- **HTTP** is the protocol used for communication between browsers and web servers.
- **HTTPS** is the secure, encrypted version of HTTP.
- Every website interaction follows a **Request → Response** cycle.
- The most common HTTP methods are **GET** (retrieve data) and **POST** (send data).
- An HTTP request consists of **Method, Path, Version, Headers, and Body**.
- Understanding HTTP is fundamental for **web scraping, API development, automation, and machine learning data collection**.

## HTML is a language for organizing and describing the content on a web page.

# What is HTML, Anyway?

HTML stands for Hypertext Markup Language. Let's break that down:

Hypertext: Text that contains links to other text (that's what makes the "web" a web!)
Markup: Instructions that describe how content should be displayed
Language: A structured way of communicating these instructions
HTML tags work exactly the same way! They come in pairs:

An opening tag that says "this section starts here"
Content (the stuff inside)
A closing tag that says "this section ends here"
The Anatomy of an HTML Element
Let's look at a real example. Here's how you'd mark up a main heading:

## Scrape the website
Options:
Send GET requests to fetch HTML pages
Parse through complicated HTML structure
Extract data from tables, divs, and spans
Hope the website structure doesn't change (or your code breaks!)
 
Use an API 
Send a request directly asking for the specific data you want
Receive clean, structured data (no HTML clutter!)
Get exactly what you need in an easy-to-use format
No parsing complicated HTML required

**API (Application Programming Interface) is like a waiter in a restaurant.**
* You (the customer) are like a user or an app.
* The kitchen is like the server or system where the   real work happens.
* The waiter (API) takes your request, delivers it to the kitchen, and brings back what you asked for.

# code to open web in terminal

uvicorn main:app --reload --host 127.0.0.1 --port 80

Common File Structure in FastAPI Projects
As your FastAPI project grows, you might organize it like this:

fastapi_training/
    ├── main.py           # Entry point - brings everything together
    ├── api.py            # API route handlers (endpoints)
    ├── schemas.py        # Data models (Pydantic schemas)
    ├── database.py       # Database connection and setup
    └── venv/             # Virtual environment