
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写承包商入职表单并提交",
        "experience": "",
        "parameters": {
            "full_name": "全名, 变量类型: str",
            "business_name": "业务名称,如果适用, 变量类型: str",
            "email": "电子邮件地址, 变量类型: str",
            "phone": "电话号码, 变量类型: str",
            "tax_id": "税号/雇主识别号, 变量类型: str",
            "business_type": "业务类型, {'': 'Select business type', 'Sole Proprietorship': 'Sole Proprietorship', 'LLC': 'LLC', 'Corporation': 'Corporation', 'Partnership': 'Partnership'}, 变量类型: str",
            "service_description": "提供的服务描述, 变量类型: str",
            "start_date": "开始日期, 格式为 YYYY-MM-DD, 变量类型: str",
            "end_date": "预计结束日期, 格式为 YYYY-MM-DD, 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Full Name').fill(kwargs.get('full_name'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Business Name (if applicable)').fill(kwargs.get('business_name'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Email Address').fill(kwargs.get('email'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Phone Number').fill(kwargs.get('phone'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Tax ID/EIN').fill(kwargs.get('tax_id'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Business Type').select_option(kwargs.get('business_type'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Services to be Provided').fill(kwargs.get('service_description'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Start Date').press('ArrowRight')
        await page.get_by_role('textbox', name='Start Date').fill(kwargs.get('start_date'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Expected End Date').press('ArrowRight')
        await page.get_by_role('textbox', name='Expected End Date').fill(kwargs.get('end_date'))
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_text('I agree to the terms and').click()
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_text('I agree to maintain').click()
    except Exception:
        pass
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Submit Onboarding Form').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/legal-compliance/contractor-onboarding"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
