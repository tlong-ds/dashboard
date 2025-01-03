import streamlit as st
import gspread
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from datetime import date

def init_sheets_client():
    SERVICE_ACCOUNT_FILE = "fabled-pivot-446609-e4-d1fb55e9792a.json"
    SCOPES_SHEETS = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials_sheets = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES_SHEETS
    )
    sheets_client = gspread.authorize(credentials_sheets) 
    return sheets_client



def read_google_sheet():
    try:
        sheets_client = init_sheets_client()
        sheet = sheets_client.open("2025 Task Management").sheet1 
        data = sheet.get_all_records()  
        df = pd.DataFrame(data) 
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None


# Function to append data to Google Sheets
def append_to_google_sheet(task, due_date):
    try:
        sheets_client = init_sheets_client()
        sheet = sheets_client.open("2025 Task Management").sheet1 
        
        values = [False, task, str(due_date)]
        sheet.append_row(values)
        return True
    except Exception as e:
        st.error(f"Google Sheets Error: {e}")
        return False

# Task creation function
def create():
    task = st.session_state.get("task_input", "").strip()
    due_date = st.session_state.get("due_input", None)

    if not task:
        st.error("Task input is empty! Please provide a valid task.")
        return

    if not due_date:
        st.error("Due date input is invalid!")
        return

    # Append task to Google Sheets
    if append_to_google_sheet(task, due_date):
        st.success("Task created successfully!")
    else:
        st.error("Failed to add the task to Google Sheets.")

# Task creation form
def create_task():
    # Initialize session state values
    if "task_input" not in st.session_state:
        st.session_state.task_input = ""
    if "due_input" not in st.session_state:
        st.session_state.due_input = date.today()

    # Form for creating a task
    with st.form(key="task_gen"):
        st.text_input("Task: ", value=st.session_state.task_input, key="task_input")
        st.date_input(
            "Due",
            min_value=date(1900, 1, 1),
            value=st.session_state.due_input,
            key="due_input"
        )
        st.form_submit_button("Submit", on_click=create)

    
def update_task(task, check):
    try:
        sheets_client = init_sheets_client()
        sheet = sheets_client.open("2025 Task Management").sheet1 
        cell = sheet.find(task)
        if cell:
            row = cell.row
            sheet.update_cell(row, 1, check)
            return True
        else:
            return False
    except Exception as e:
        st.error(f"Google Sheets Error: {e}")
        return False



