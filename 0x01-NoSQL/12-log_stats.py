#!/usr/bin/env python3
'''Task 12's module.
'''
from pymongo import MongoClient

def print_nginx_request_logs(nginx_collection):
    # Count total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Define HTTP methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count status check requests
    status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

def run():
    # Connect to MongoDB
    client = MongoClient('localhost', 27017)

    # Access the 'logs' database and the 'nginx' collection
    db = client.logs
    nginx_collection = db.nginx

    # Print statistics
    print_nginx_request_logs(nginx_collection)

if __name__ == "__main__":
    run()
