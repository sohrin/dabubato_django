CREATE DATABASE dabubato_db;
CREATE USER dabubato_user WITH PASSWORD 'dabubato_pass';
ALTER ROLE dabubato_user SET client_encoding TO 'utf8';
ALTER ROLE dabubato_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE dabubato_user SET timezone TO 'Asia/Tokyo';
GRANT ALL PRIVILEGES ON DATABASE dabubato_db TO dabubato_user;