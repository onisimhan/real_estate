-- SQL script for create databasa and tables
--
CREATE DATABASE IF NOT EXISTS house_rent WITH ENCODING 'UTF8';

CREATE SCHEMA house_rent;
SET SCHEMA 'house_rent';

\connect house_rent;

CREATE TABLE IF NOT EXISTS main (
  id SERIAL NOT NULL PRIMARY KEY,
  address text NULL,
  city text NULL,
  state VARCHAR(2),
  zip_code VARCHAR(10),
  bedrooms SMALLINT NULL,
  bathrooms_full SMALLINT NULL,
  bathrooms_half SMALLINT NULL,
  square_feet VARCHAR(20) NULL,
  square_feet_lot VARCHAR(20) NULL,
  price VARCHAR(20) NULL,
  description TEXT NULL,
  style VARCHAR(250) NULL,
  home_type VARCHAR(250) NULL,
  year_built VARCHAR(4) NULL,
  price_per_square_foot VARCHAR(20) NULL,
  date_posted timestamp NULL,
  status VARCHAR(20) NULL,
  longitude VARCHAR(20) NULL,
  latitude VARCHAR(20) NULL,
  create_date timestamp NULL,
  original_url TEXT NULL,
  features JSON NULL
);

CREATE TABLE IF NOT EXISTS images (
  id SERIAL NOT NULL PRIMARY KEY,
  main_id SERIAL NOT NULL REFERENCES main (id),
  name VARCHAR(100),
  path VARCHAR(250),
  alt VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS schools (
  id SERIAL NOT NULL PRIMARY KEY,
  main_id SERIAL NOT NULL REFERENCES main (id),
  score VARCHAR(10) NULL,
  name VARCHAR(100) NULL,
  grades VARCHAR(10) NULL,
  distance VARCHAR(10) NULL
);

CREATE TABLE IF NOT EXISTS listing_provider (
  id SERIAL NOT NULL PRIMARY KEY,
  main_id SERIAL NOT NULL REFERENCES main (id),
  listing_agent VARCHAR(100) NULL,
  agent_phone_number VARCHAR(25) NULL,
  listed_by VARCHAR(100) NULL,
  broker_location VARCHAR(50) NULL,
  data_source VARCHAR(50) NULL
);
