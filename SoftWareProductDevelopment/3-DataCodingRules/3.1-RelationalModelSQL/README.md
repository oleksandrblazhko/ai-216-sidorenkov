CREATE TABLE Users (
  id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100)
);

CREATE TABLE Guides (
  id INTEGER PRIMARY KEY,
  topic VARCHAR(100),
  description TEXT
);

CREATE TABLE Materials (
  id INTEGER PRIMARY KEY,
  type VARCHAR(30),
  link TEXT
);

CREATE TABLE Certificates (
  id INTEGER PRIMARY KEY,
  course VARCHAR(100),
  issue_date DATE
);

CREATE TABLE SupportRequests (
  id INTEGER PRIMARY KEY,
  type VARCHAR(50),
  status VARCHAR(50)
);
