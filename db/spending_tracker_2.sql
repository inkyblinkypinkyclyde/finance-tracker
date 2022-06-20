DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;


CREATE TABLE accounts(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    balance INT,
    credit_limit INT,
    is_account BOOLEAN
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    amount INT,
    date DATE,
    description VARCHAR(255),
    into_account_id INT REFERENCES accounts(id) ON DELETE CASCADE,
    out_of_account_id INT REFERENCES accounts(id) ON DELETE CASCADE,
    is_visible BOOLEAN
);
