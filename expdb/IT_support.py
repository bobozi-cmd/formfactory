
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "IT Support Request Form submission with various fields and validations.",
        "experience": "",
        "parameters": {
            "request_type": "Type of IT support request, {'Hardware Issue', 'Software Issue', 'Network Issue', 'Access/Permission Request', 'Other'}, 变量类型: str",
            "priority_level": "Level of priority for the request, {'Critical','Urgent-System Down','High-Work Blocked','Medium-Limited Functionality','Low-Minor Issue'}, 变量类型: str",
            "subject": "Brief description of the issue., 变量类型: str",
            "detailed_description": "Detailed description of the issue., 变量类型: str",
            "location_department": "Location or department where the issue is occurring., 变量类型: str",
            "number_of_affected_users": "The number of users affected by the issue., 变量类型: int",
            "preferred_contact_time": "Preferred time for contact, format: e.g., Mon-Fri 9AM-5PM, 变量类型: str",
            "your_name": "Name of the person submitting the request., 变量类型: str",
            "your_email": "Email address of the person submitting the request., 变量类型: str",
            "contact_phone_number": "Phone number for contact., 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_label('Request Type').select_option(kwargs['request_type'])
    except Exception as e:
        print(f'Error selecting request type: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Priority Level').select_option(kwargs['priority_level'])
    except Exception as e:
        print(f'Error selecting priority level: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Subject').fill(kwargs['subject'])
    except Exception as e:
        print(f'Error filling subject: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Detailed Description').fill(kwargs['detailed_description'])
    except Exception as e:
        print(f'Error filling detailed description: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Location/Department').fill(kwargs['location_department'])
    except Exception as e:
        print(f'Error filling location/department: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('spinbutton', name='Number of Affected Users').fill(str(kwargs['number_of_affected_users']))
    except Exception as e:
        print(f'Error filling number of affected users: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Preferred Contact Time').fill(kwargs['preferred_contact_time'])
    except Exception as e:
        print(f'Error filling preferred contact time: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Your Name').fill(kwargs['your_name'])
    except Exception as e:
        print(f'Error filling your name: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Your Email').fill(kwargs['your_email'])
    except Exception as e:
        print(f'Error filling your email: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Contact Phone Number').fill(kwargs['contact_phone_number'])
    except Exception as e:
        print(f'Error filling contact phone number: {e}')
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('button', name='Submit Support Request').click()
    except Exception as e:
        print(f'Error submitting form: {e}')
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/tech-software/support-request"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
