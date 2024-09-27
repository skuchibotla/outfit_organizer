-- Create enums if they don't already exist
DO $$ 
BEGIN 
  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'gender_enum') THEN
    CREATE TYPE gender_enum AS ENUM ('male', 'female', 'non-binary', 'other');
  END IF;

  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'status_enum') THEN
    CREATE TYPE status_enum AS ENUM ('draft', 'saved');
  END IF;

  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'season_enum') THEN
    CREATE TYPE season_enum AS ENUM ('fall', 'winter', 'spring', 'summer');
  END IF;
END $$;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255) UNIQUE NOT NULL,
    encrypted_password VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    gender gender_enum,
    age INT
);

-- Clothes table and indexes
CREATE TABLE IF NOT EXISTS clothes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    image_url VARCHAR(255) UNIQUE NOT NULL,
    type VARCHAR(255) NOT NULL,
    color VARCHAR(255) NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_clothes_user_id ON clothes (user_id);
CREATE INDEX IF NOT EXISTS idx_clothes_type ON clothes (type);
CREATE INDEX IF NOT EXISTS idx_clothes_color ON clothes (color);

-- Outfits table and indexes
CREATE TABLE IF NOT EXISTS outfits (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    image_url VARCHAR(255),
    status status_enum DEFAULT 'draft' NOT NULL,
    CONSTRAINT unique_outfits_user_id_name UNIQUE (user_id, name)
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_outfits_user_image_url ON outfits (user_id, image_url) 
WHERE image_url IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_outfits_user_id ON outfits (user_id);
CREATE INDEX IF NOT EXISTS idx_outfits_name ON outfits (name);
CREATE INDEX IF NOT EXISTS idx_outfits_status ON outfits (status);

-- Categories table and indexes
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    name VARCHAR(255) UNIQUE NOT NULL, 
    occasion VARCHAR(255),
    season season_enum, 
    CONSTRAINT unique_categories_user_id_name UNIQUE (user_id, name)
);

CREATE INDEX IF NOT EXISTS idx_categories_user_id ON categories (user_id);
CREATE INDEX IF NOT EXISTS idx_categories_name ON categories (name);
CREATE INDEX IF NOT EXISTS idx_categories_occasion ON categories (occasion);
CREATE INDEX IF NOT EXISTS idx_categories_season ON categories (season);

-- Joint tables
CREATE TABLE IF NOT EXISTS clothes_outfits (
    clothing_id INTEGER NOT NULL REFERENCES clothes (id) ON DELETE CASCADE,
    outfit_id INTEGER NOT NULL REFERENCES outfits (id) ON DELETE CASCADE,
    PRIMARY KEY (clothing_id, outfit_id)
);

CREATE TABLE IF NOT EXISTS clothes_categories (
    clothing_id INTEGER NOT NULL REFERENCES clothes (id) ON DELETE CASCADE,
    category_id INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
    PRIMARY KEY (clothing_id, category_id)
);

CREATE TABLE IF NOT EXISTS outfits_categories (
    outfit_id INTEGER NOT NULL REFERENCES outfits (id) ON DELETE CASCADE,
    category_id INTEGER NOT NULL REFERENCES categories (id) ON DELETE CASCADE,
    PRIMARY KEY (outfit_id, category_id)
);
