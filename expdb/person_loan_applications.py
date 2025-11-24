
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写个人贷款申请的表单并提交",
        "experience": "",
        "parameters": {
            "first_name": "First Name of the applicant., 变量类型: str",
            "middle_name": "Middle Name of the applicant., 变量类型: str",
            "last_name": "Last Name of the applicant., 变量类型: str",
            "loan_amount": "Loan Amount in dollars., 变量类型: int",
            "loan_term": "Loan Term in months, {'12 months', '24 months', '36 months', '48 months', '60 months'}., 变量类型: str",
            "employment_status": "Employment Status, {'fullTime': 'Full-time', 'partTime': 'Part-time', 'selfEmployed': 'Self-employed', 'retired': 'Retired'}., 变量类型: str",
            "monthly_income": "Monthly Income in dollars., 变量类型: int"
        }
    }
    """
    await page.get_by_role('textbox', name='First Name').click()
    await asyncio.sleep(INTERVAL)
    if kwargs.get('first_name'):
        await page.get_by_role('textbox', name='First Name').fill(kwargs['first_name'])
    else:
        raise ValueError('First name is required')
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Middle Name').click()
    await asyncio.sleep(INTERVAL)
    if kwargs.get('middle_name'):
        await page.get_by_role('textbox', name='Middle Name').fill(kwargs['middle_name'])
    else:
        raise ValueError('Middle name is required')
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Last Name').click()
    await asyncio.sleep(INTERVAL)
    if kwargs.get('last_name'):
        await page.get_by_role('textbox', name='Last Name').fill(kwargs['last_name'])
    else:
        raise ValueError('Last name is required')
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Loan Amount ($)').click()
    await asyncio.sleep(INTERVAL)
    if kwargs.get('loan_amount') is not None:
        await page.get_by_role('spinbutton', name='Loan Amount ($)').fill(str(kwargs['loan_amount']))
    else:
        raise ValueError('Loan amount is required')
    await asyncio.sleep(INTERVAL)
    if kwargs.get('loan_term'):
        await page.get_by_label('Loan Term (months)').select_option(kwargs['loan_term'])
    else:
        raise ValueError('Loan term is required')
    await asyncio.sleep(INTERVAL)
    if kwargs.get('employment_status'):
        await page.get_by_label('Employment Status').select_option(kwargs['employment_status'])
    else:
        raise ValueError('Employment status is required')
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Monthly Income ($)').click()
    await asyncio.sleep(INTERVAL)
    if kwargs.get('monthly_income') is not None:
        await page.get_by_role('spinbutton', name='Monthly Income ($)').fill(str(kwargs['monthly_income']))
    else:
        raise ValueError('Monthly income is required')
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Submit Application').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/finance-banking/personal-loan"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
