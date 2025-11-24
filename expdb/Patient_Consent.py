
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写病人同意书表单并提交",
        "experience": "",
        "parameters": {
            "patient_name": "病人的全名, 非空字符串, 变量类型: str",
            "date_of_birth": "病人的出生日期, 格式为 YYYY-MM-DD, 变量类型: str",
            "medical_record_number": "病历号, 非空字符串, 变量类型: str",
            "procedure_name": "手术名称, 可以为空字符串, 变量类型: str",
            "surgeon_name": "外科医生/医师的名字, 可以为空字符串, 变量类型: str",
            "emergency_contact_name": "紧急联系人姓名, 可以为空字符串, 变量类型: str",
            "emergency_contact_phone": "紧急联系人电话, 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Full Name').fill(kwargs.get('patient_name'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Date of Birth').press('ArrowRight')
        await page.get_by_role('textbox', name='Date of Birth').fill(kwargs.get('date_of_birth'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Medical Record Number').fill(kwargs.get('medical_record_number'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Name of Procedure').fill(kwargs.get('procedure_name'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Surgeon/Physician Name').fill(kwargs.get('surgeon_name'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_text('I understand the nature of').click()
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_text('I have had the opportunity to').click()
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_text('I understand the alternatives').click()
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Emergency Contact Name').fill(kwargs.get('emergency_contact_name'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Emergency Contact Phone').fill(kwargs.get('emergency_contact_phone'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('button', name='Submit Consent Form').click()
    except:
        pass
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/healthcare-medical/patient-consent"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
