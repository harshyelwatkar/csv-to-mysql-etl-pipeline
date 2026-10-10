# CSV-to-MySQL ETL Pipeline

A Python-based ETL project that extracts sales records from CSV files, validates and transforms the data using pandas, and loads valid records into a MySQL database.

## Features

- Extracts and combines data from multiple CSV files.
- Converts order IDs, sales amounts, and dates to appropriate data types.
- Removes duplicate order IDs and records with missing required fields.
- Rejects invalid order IDs and negative sales amounts.
- Loads data into MySQL using SQLAlchemy and PyMySQL.
- Handles existing order IDs using MySQL's duplicate-key update feature.
- Verifies the destination record count and checks for invalid sales amounts.

## Tech Stack

- Python
- pandas
- MySQL
- SQLAlchemy
- PyMySQL
- python-dotenv
- Jupyter Notebook

## Project Structure

```text
ETL_Pipeline/
├── .env.example
├── .gitignore
├── README.md
├── test_connection.py
├── mysql/
│   ├── data/
│   │   ├── sales.csv
│   │   └── sales_2.csv
│   ├── requirements.txt
│   └── src/
│       └── etl_csv_to_mysql.ipynb
└── sql/
    └── schema.sql
```

## Setup

1. Install Python 3.12 and MySQL 8.
2. Create a virtual environment and activate it.
3. Install dependencies:

   ```bash
   pip install -r mysql/requirements.txt
   ```

4. Create the database and table using `sql/schema.sql`.
5. Create a `.env` file in the project root using `.env.example` as a template.
6. Update the environment variables with your local MySQL credentials.
7. Open `mysql/src/etl_csv_to_mysql.ipynb` in VS Code and select your project virtual environment as the kernel.
8. Run the notebook cells in order.

## Environment Variables

```dotenv
DB_HOST=localhost
DB_PORT=3306
DB_NAME=sales_etl
DB_USER=etl_user
DB_PASSWORD=your_local_password
```

Never commit real passwords or your `.env` file.

## Validation Results

For the supplied sample data, the initial pipeline run produced:

- Source records: 20
- Valid records loaded: 19
- Rejected records: 1
- Negative-amount records in the destination table: 0

## Future Improvements

- Add automated unit tests for data validation.
- Add structured logging and error reporting.
- Track rejected records in a separate audit file.
- Add incremental loading and more comprehensive data quality checks.
