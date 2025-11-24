
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写并提交背景调查授权表单",
        "experience": "",
        "parameters": {
            "first_name": "First Name, 变量类型: str",
            "middle_name": "Middle Name, 变量类型: str",
            "last_name": "Last Name, 变量类型: str",
            "social_security_number": "Social Security Number, 变量类型: str",
            "date_of_birth": "Date of Birth in 'YYYY-MM-DD' format, 变量类型: str",
            "street_address": "Street Address, 变量类型: str",
            "city": "City, 变量类型: str",
            "state": "State, 变量类型: str",
            "zip_code": "ZIP Code, 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='First Name').fill(kwargs.get('first_name'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Middle Name').fill(kwargs.get('middle_name', ''))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Last Name').fill(kwargs.get('last_name'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Social Security Number').fill(kwargs.get('social_security_number'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Date of Birth').press('ArrowRight')
        await page.get_by_role('textbox', name='Date of Birth').fill(kwargs.get('date_of_birth'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Street Address').fill(kwargs.get('street_address'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='City').fill(kwargs.get('city'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='State').fill(kwargs.get('state'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='ZIP Code').fill(kwargs.get('zip_code'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_text('I authorize the complete').click()
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_text('I understand that providing').click()
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('button', name='Submit Authorization').click()
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/legal-compliance/background-check"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
