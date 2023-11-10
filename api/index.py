from fastapi import FastAPI
import os
from supabase import create_client, Client



url: str = "https://dyiypkrejvdhkakvxfmb.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR5aXlwa3JlanZkaGtha3Z4Zm1iIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTk1OTAzODUsImV4cCI6MjAxNTE2NjM4NX0.9sNfC7BqpiWLa44TSAtYSYGbztrB-7QsXjbCVOMXu8o"
print(url)
supabase: Client = create_client(url, key)

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}



@app.get("api/suap")
def supatest():
    response = supabase.table('image_meta').select("*").execute()
    return response