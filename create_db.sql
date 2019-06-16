CREATE DATABASE IF NOT EXISTS book_quotes;

USE book_quotes;

CREATE TABLE IF NOT EXISTS book_quotes.authors (
  author_id INT(255) NOT NULL AUTO_INCREMENT,
  author_name VARCHAR(255) NOT NULL,
  picture_url VARCHAR(255),
  PRIMARY KEY (author_id),
  UNIQUE INDEX (author_id));
  
CREATE TABLE IF NOT EXISTS book_quotes.books (
  book_id INT(255) NOT NULL AUTO_INCREMENT,
  book_name VARCHAR(255) NOT NULL,
  book_link VARCHAR(255),
  author_id INT(255),
  PRIMARY KEY (book_id),
  FOREIGN KEY (author_id) REFERENCES authors(author_id),
  UNIQUE INDEX (book_id));
  
CREATE TABLE IF NOT EXISTS book_quotes.quotes (
  quote_id INT(255) NOT NULL AUTO_INCREMENT,
  quote_content VARCHAR(255) NOT NULL,
  likes INT(255),
  tags VARCHAR(255),
  book_id INT(255),
  PRIMARY KEY (quote_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id),
  UNIQUE INDEX (quote_id));