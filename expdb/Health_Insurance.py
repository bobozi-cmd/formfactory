
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写等待保险索赔表单并提交",
        "experience": "",
        "parameters": {
            "policy_number": "保险单号, 文字框输入值, 变量类型: str",
            "policy_holder_name": "投保人姓名, 文字框输入值, 变量类型: str",
            "service_date": "服务日期, 日期框输入值, 格式为 'YYYY-MM-DD', 变量类型: str",
            "claim_amount": "索赔金额, 数字框输入值, 可以有小数, 变量类型: float",
            "service_type": "服务类型, {'': 'Select service type', 'Doctor Consultation': 'Doctor Consultation', 'Medical Procedure': 'Medical Procedure', 'Prescription Medication': 'Prescription Medication', 'Laboratory Tests': 'Laboratory Tests', 'Emergency Care': 'Emergency Care'}, 变量类型: str",
            "diagnosis_condition": "诊断/病情, 文字框输入值, 变量类型: str",
            "provider_name": "服务提供者姓名, 文字框输入值, 变量类型: str",
            "provider_id_number": "服务提供者ID号, 文字框输入值, 变量类型: str"
        }
    }
    """
    try:
        await page.get_by_role('textbox', name='Policy Number').fill(kwargs.get('policy_number', '1221'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Policy Holder Name').fill(kwargs.get('policy_holder_name', '2112'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Date of Service').fill(kwargs.get('service_date', '1234-11-11'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('spinbutton', name='Claim Amount ($)').fill(str(kwargs.get('claim_amount', 1234)))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_label('Type of Service').select_option(kwargs.get('service_type', 'Medical Procedure'))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Diagnosis/Condition').fill(kwargs.get('diagnosis_condition', '   '))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Provider Name').fill(kwargs.get('provider_name', '    '))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('textbox', name='Provider ID Number').fill(kwargs.get('provider_id_number', '  '))
    except:
        pass
    await asyncio.sleep(INTERVAL)
    try:
        await page.get_by_role('button', name='Submit Claim').click()
    except:
        pass
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/healthcare-medical/insurance-claim"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
