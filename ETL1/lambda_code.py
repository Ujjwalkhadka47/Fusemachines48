'To Create the lambda function, write the code to fetch data from api, dumpded it into first s3 bucket, and
'then transform data then save to 2nd buckect.


import boto3
import pandas as pd
import io

def lambda_handler(event, context):
    
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Define the source and destination bucket and key
    source_bucket = 'apprentice-training-data-ujjwal-raw'
    
    source_key = 'publicapi_entries.csv'

    destination_bucket = 'apprentice-training-data-ujjwal-transform'
    
    destination_key = 'clean_data.csv'

    # Download CSV from source bucket
    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    
    csv_content = response['Body'].read()

    # Perform data cleaning using pandas
    df = pd.read_csv(io.BytesIO(csv_content))
    
    
    # Perform your data cleaning operations on the dataframe
    df = df.drop(['Auth'], axis=1)
    
    df = df.drop_duplicates()
    
    df = df.dropna()   
    
    # Convert the cleaned dataframe back to CSV content
    cleaned_csv_content = df.to_csv(index=False)

    # Upload cleaned CSV to destination bucket
    s3.put_object(Bucket=destination_bucket, Key=destination_key, Body=cleaned_csv_content)

    return {
        'statusCode': 200,
        'body': 'Data cleaned and stored successfully!'
    }
    
    
    
'The process of reading data from an S3 bucket, parsing it, and 
'inserting it into a PostgreSQL database &
'making it suitable for serverless execution in an AWS Lambda environment.

import boto3
import pandas as pd
import psycopg2
import io
import csv
from io import StringIO

def lambda_handler(event, context):
    
    db_params = {
    "host": "apprentice-training-2023-rds.cth7tqaptja4.us-west-1.rds.amazonaws.com",
    "database": "postgres",
    "user": "postgres",
    "password": "hello123"
    }              

    # Establish a connection to PostgreSQL
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    bucket_name = 'apprentice-training-data-ujjwal-transform'
    object_key = 'clean_data.csv'
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    data = response['Body'].read().decode('utf-8')
    
    # Parse data as CSV
    csv_data = StringIO(data)
    csv_reader = csv.reader(csv_data)
    next(csv_reader)
    
    values_to_insert = []
    for row in csv_reader:
        API = row[0]
        description = row[1]
        https = row[2]
        cors = row[3]
        link = row[4]
        
    
        values_to_insert.append((API, description, https, cors, link))
    
    placeholders = ', '.join(['%s'] * len(values_to_insert[0]))
    sql = f"INSERT INTO ujjwal_etl_assignment(API, description, https, cors, link) VALUES ({placeholders})"
    
    cursor.executemany(sql, values_to_insert)
    
    conn.commit()
    cursor.close()
    conn.close()
    return {
        'statusCode': 200,
        'body': 'Data cleaned and stored successfully!'
    }