
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "在银行账户开户表单中填写个人详细信息，选择账户类型和ID类型，并提交申请。",
        "experience": "",
        "parameters": {
            "full_name": "用户的全名, 变量类型: str",
            "date_of_birth": "用户的出生日期, 格式为 YYYY-MM-DD, 变量类型: str",
            "account_type": "账户类型, {'': 'Select account type', 'Saving Account': 'Savings Account', 'Checking Account': 'Checking Account', 'Business Account': 'Business Account', 'Student Account': 'Student Account'}, 变量类型: str",
            "id_type": "ID 类型, {'': 'Select ID type', 'Passport': 'Passport', 'Driver's License': 'Driver's License', 'State ID': 'State ID'}, 变量类型: str",
            "id_number": "用户的身份证号码, 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Full Name').click()
        await page.get_by_role('textbox', name='Full Name').fill(kwargs.get('full_name', 'ZHOU'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Date of Birth').press('ArrowRight')
        await page.get_by_role('textbox', name='Date of Birth').press('ArrowRight')
        await page.get_by_role('textbox', name='Date of Birth').fill(kwargs.get('date_of_birth', '1999-01-11'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.locator('#accountType').select_option(kwargs.get('account_type', 'Saving Account'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('ID Type').select_option(kwargs.get('id_type', "Driver's License"))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='ID Number').click()
        await page.get_by_role('textbox', name='ID Number').fill(kwargs.get('id_number', 'A121132'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('button', name='Submit Application').click()
    except:
        pass
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/finance-banking/account-opening"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
