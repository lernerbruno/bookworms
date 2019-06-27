create DATABASE IF NOT EXISTS book_quotes;

USE book_quotes;

create TABLE IF NOT EXISTS book_quotes.authors (
  author_id INT(255) NOT NULL AUTO_INCREMENT,
  author_name VARCHAR(255) NOT NULL,
  GR_author_id INT(255),
  gender VARCHAR(100),
  year_of_birth INT(255),
  ethnic_group VARCHAR(255),
  country VARCHAR(255),
  PRIMARY KEY (author_id),
  UNIQUE INDEX (author_name, GR_author_id));
  
create TABLE IF NOT EXISTS book_quotes.books (
  book_id INT(255) NOT NULL AUTO_INCREMENT,
  book_name VARCHAR(255) NOT NULL,
  GR_book_id VARCHAR(255),
  PRIMARY KEY (book_id),
  UNIQUE INDEX (book_name));
  
create TABLE IF NOT EXISTS book_quotes.quotes (
  quote_id INT(255) NOT NULL AUTO_INCREMENT,
  quote_content TEXT NOT NULL,
  likes INT(255),
  author_id INT(255),
  book_id INT(255),
  PRIMARY KEY (quote_id),
  FOREIGN KEY (author_id) REFERENCES authors(author_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id),
  UNIQUE INDEX (quote_content(100)));

create TABLE IF NOT EXISTS book_quotes.tags (
  tag_id INT(255) NOT NULL AUTO_INCREMENT,
  tag_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (tag_id),
  UNIQUE INDEX (tag_name));

create TABLE IF NOT EXISTS book_quotes.quote_tags (
  id INT(255) NOT NULL AUTO_INCREMENT,
  quote_id INT(255) NOT NULL,
  tag_id INT(255) NOT NULL,
  FOREIGN KEY (quote_id) REFERENCES quotes(quote_id),
  FOREIGN KEY (tag_id) REFERENCES tags(tag_id),
  PRIMARY KEY (id));
