
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写房产租赁申请表并提交",
        "experience": "按照以下步骤填写房地产租赁申请表：首先，在 'Full Name' 输入框中输入有效字符的全名，不能为空。在 'Email Address' 输入框中输入有效邮箱地址，必须符合邮箱格式。在 'Phone Number' 输入框中输入以纯数字表示的电话号码。在 'Date of Birth' 输入框中输入出生日期，格式为 'yyyy/mm/dd'。接下来，填写地址信息：在 'Street Address', 'City', 'State' 和 'ZIP Code' 输入框中分别填写街道、城市、州和邮政编码。对于就业信息：在 'Current Employer' 和 'Job Title' 输入框中输入雇主和职位名称。在 'Monthly Income (USD)' 和 'Length of Employment' 输入框中以数字形式填写月收入和就业时长。在租赁偏好部分：在 'Preferred Move-in Date' 输入框中输入预期搬入日期，选择 'Preferred Lease Term'，例如 '12 months'，并在 'Maximum Monthly Rent (USD)' 中以数字填写每月房租限额。在 'Preferred Area' 中输入期望区域。在附加信息部分：选择 'Do you have any pets?' 是或否，如果选择是，描述宠物。在 'References (Optional)' 填写推荐人信息，并在 'Additional Comments' 中填写其他说明。填完后，点击 'Submit Application' 按钮提交申请。确保所有输入项符合格式和限制要求。",
        "parameters": {
            "full_name": "全名, 变量类型: str",
            "email": "电子邮件地址, 变量类型: str",
            "phone": "电话号码, 变量类型: str",
            "date_of_birth": "出生日期, 格式为 YYYY-MM-DD, 变量类型: str",
            "current_street": "街道地址, 变量类型: str",
            "current_city": "城市, 变量类型: str",
            "current_state": "州/省, 变量类型: str",
            "current_zip": "邮政编码, 变量类型: str",
            "employer_name": "当前雇主, 变量类型: str",
            "job_title": "职位, 变量类型: str",
            "monthly_income": "每月收入（美元）, 变量类型: int",
            "employment_length": "就业时间长度, 变量类型: str",
            "preferred_move_date": "期望的搬入日期, 格式为 YYYY-MM-DD, 变量类型: str",
            "lease_term": "期望租期, {'6 months': '6 Months', '12 months': '12 Months', '24 months': '24 Months'}, 变量类型: str",
            "max_rent": "最高月租（美元）, 变量类型: int",
            "preferred_area": "期望居住区域, 变量类型: str",
            "pets": "是否有宠物, {'no': 'No', 'yes': 'Yes'}, 变量类型: str",
            "pet_details": "如果有宠物，请描述, 变量类型: str",
            "references": "推荐人(可选), 没有则为空, 变量类型: str",
            "additional_info": "附加评论, 变量类型: str"
        }
    }
    """
    await page.get_by_role('textbox', name='Full Name').fill(kwargs['full_name'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Email Address').fill(kwargs['email'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Phone Number').fill(kwargs['phone'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Date of Birth').fill(kwargs['date_of_birth'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Street Address').fill(kwargs['current_street'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='City').fill(kwargs['current_city'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='State').fill(kwargs['current_state'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='ZIP Code').fill(kwargs['current_zip'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Current Employer').fill(kwargs['employer_name'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Job Title').fill(kwargs['job_title'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Monthly Income (USD)').fill(str(kwargs['monthly_income']))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Length of Employment').fill(kwargs['employment_length'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Preferred Move-in Date').fill(kwargs['preferred_move_date'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_label('Preferred Lease Term').select_option(kwargs['lease_term'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Maximum Monthly Rent (USD)').fill(str(kwargs['max_rent']))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Preferred Area').fill(kwargs['preferred_area'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_label('Do you have any pets?').select_option(kwargs['pets'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='If yes, please describe your').fill(kwargs['pet_details'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='References (Optional)').fill(kwargs['references'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Additional Comments').fill(kwargs['additional_info'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Submit Application').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/professional-business/rental-application"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
