## Usage
1. Setup: `make setup`
2. Unit Tests: `make tests`
3. Build dist: `make dist`

## Scope of Work

The scope of this project is to design and implement a template engine, which converts a custom template to Postman collection in JSON format. This improves manageability and reusability of API collections and tests.

## Broad Area of Work
Postman is an application used for API testing. It is an HTTP client that tests HTTP requests, utilizing a graphical user interface, through which we obtain different types of responses that need to be subsequently validated. The current research project focus is on developing a template engine that can produce postman collections in JSON format.

![image6](https://user-images.githubusercontent.com/26188281/149787703-7d3b0b03-971b-4706-b386-641ba94c5f90.png)

## Background

Testing is one of the most critical processes of the Software Development Lifecycle (SDLC). It helps companies to perform a comprehensive assessment of software and ensure that their product fulfills the client’s needs.

The CI/CD pipeline approach has emerged as a result of a tendency for today’s software users to be less and less tolerant towards defects and at the same time expect fast updates and fixes. Testing is one process that can and should be automated to a great extent within the CI/CD pipeline.

Postman is an application that is used for API testing. Newman is a command-line Collection Runner for Postman. It enables you to run and test a Postman Collection directly from the command line. It is built with extensibility in mind so that you can easily integrate it with your continuous integration servers and build systems.

The Postman collections created via the GUI have to be exported as in JSON format, which is used by the Newman client. Postman lacks the ability to reuse requests, tests, and pre-request scripts. It is also difficult to maintain postman collections in JSON format in version control systems as the collection has to be exported after each change.


## Objectives
The objectives of project are as follows:

1. Create a template engine for postman which can be used to define collections and requests.
2. The template engine will generate postman collection in JSON format, which can be imported by Postman GUI application or run using Newman client


