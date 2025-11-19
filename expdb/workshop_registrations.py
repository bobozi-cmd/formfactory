
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写并提交一个工作坊的注册表单",
        "experience": "",
        "parameters": {
            "full_name": "输入'Full Name', 变量类型: str",
            "email": "输入'Email Address', 变量类型: str",
            "phone": "输入'Phone Number', 变量类型: str",
            "organization": "输入'Organization/Company', 变量类型: str",
            "workshop_type": "选择'Workshop Category', {'Technology & IT': 'Technology & IT', 'Business & Management': 'Business & Management', 'Leadership & Communication': 'Leadership & Communication', 'Digital Marketing': 'Digital Marketing', 'Finance & Investment': 'Finance & Investment'}, 变量类型: str",
            "session_date": "输入'Preferred Session Date', 日期格式为 YYYY-MM-DD, 变量类型: str",
            "session_time": "选择'Preferred Time Slot', {'morning': 'Morning (9:00 AM - 12:00 PM)', 'afternoon': 'Afternoon (1:00 PM - 5:00 PM)', 'evening': 'Evening (6:00 PM - 9:00 PM)'}, 变量类型: str",
            "delivery_mode": "选择'Preferred Delivery Mode', {'In-Person': 'In-Person', 'Online': 'Online', 'Hybrid': 'Hybrid'}, 变量类型: str",
            "education_level": "选择'Highest Education Level', {'High School': 'High School', 'Bachelor's Degree': 'Bachelor's Degree', 'Master's Degree': 'Master's Degree', 'PhD': 'Doctorate', 'other': 'Other'}, 变量类型: str",
            "experience_years": "输入'Years of Professional Experience', 变量类型: str",
            "current_role": "输入'Current Role/Position', 变量类型: str",
            "dietary_requirements": "选择'Dietary Requirements', {'None': 'None', 'Vegetarian': 'Vegetarian', 'Vegan': 'Vegan', 'Halal': 'Halal', 'Kosher': 'Kosher', 'Other (Please specify)': 'Other (Please specify)'}, 变量类型: str",
            "accessibility_needs": "输入'Accessibility Requirements', 变量类型: str",
            "payment_method": "选择'Payment Method', {'Credit Card': 'Credit Card', 'Bank Transfer': 'Bank Transfer', 'Company Sponsored': 'Company Sponsored'}, 变量类型: str",
            "billing_address": "输入'Billing Address', 变量类型: str",
            "expectations": "输入'What do you hope to learn from this workshop?', 变量类型: str",
            "special_requests": "输入'Any other special requests or comments?', 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Full Name').fill(kwargs['full_name'])
    except Exception as e:
        print(f"Error filling 'Full Name': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Email Address').fill(kwargs['email'])
    except Exception as e:
        print(f"Error filling 'Email Address': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Phone Number').fill(kwargs['phone'])
    except Exception as e:
        print(f"Error filling 'Phone Number': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Organization/Company').fill(kwargs['organization'])
    except Exception as e:
        print(f"Error filling 'Organization/Company': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Workshop Category').select_option(kwargs['workshop_type'])
    except Exception as e:
        print(f"Error selecting 'Workshop Category': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Preferred Session Date').fill(kwargs['session_date'])
    except Exception as e:
        print(f"Error filling 'Preferred Session Date': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Preferred Time Slot').select_option(kwargs['session_time'])
    except Exception as e:
        print(f"Error selecting 'Preferred Time Slot': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Preferred Delivery Mode').select_option(kwargs['delivery_mode'])
    except Exception as e:
        print(f"Error selecting 'Preferred Delivery Mode': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Highest Education Level').select_option(kwargs['education_level'])
    except Exception as e:
        print(f"Error selecting 'Highest Education Level': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('spinbutton', name='Years of Professional').fill(kwargs['experience_years'])
    except Exception as e:
        print(f"Error filling 'Years of Professional Experience': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Current Role/Position').fill(kwargs['current_role'])
    except Exception as e:
        print(f"Error filling 'Current Role/Position': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Dietary Requirements').select_option(kwargs['dietary_requirements'])
    except Exception as e:
        print(f"Error selecting 'Dietary Requirements': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Accessibility Requirements').fill(kwargs['accessibility_needs'])
    except Exception as e:
        print(f"Error filling 'Accessibility Requirements': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Payment Method').select_option(kwargs['payment_method'])
    except Exception as e:
        print(f"Error selecting 'Payment Method': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Billing Address').fill(kwargs['billing_address'])
    except Exception as e:
        print(f"Error filling 'Billing Address': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='What do you hope to learn').fill(kwargs['expectations'])
    except Exception as e:
        print(f"Error filling 'What do you hope to learn': {e}")
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Any other special requests or').fill(kwargs['special_requests'])
    except Exception as e:
        print(f"Error filling 'Any other special requests or comments': {e}")
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Register Now').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/professional-business/workshop-registration"

register_func = [
    f1
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
