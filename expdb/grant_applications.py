
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写用户基本信息，包括名字、邮箱、出生日期和性别。",
        "experience": "要成功填写申请表，首先需要分步骤来完成。开始时，点击 'First Name' 输入框，并输入名字。然后，选择 'Last Name' 输入框，输入姓氏。请确保在输入内容之前先点击对应的输入框。接下来，在 'Email' 输入框中填写有效的电子邮件地址。对于出生日期，点击 'Date of Birth' 输入框，并使用日期选择器选择正确的日期格式为 YYYY/MM/DD。选择性别时，点击对应的性别选项按钮。在每个步骤中确保输入格式正确，可以避免出现错误。",
        "parameters": {
            "first_name": "用户的名字, 变量类型: str",
            "last_name": "用户的姓氏, 变量类型: str",
            "email": "用户的电子邮件地址, 变量类型: str",
            "birthdate": "用户的出生日期，格式为 YYYY/MM/DD, 变量类型: str",
            "gender": "选择用户的性别, {'Male': '男', 'Female': '女'}, 变量类型: str"
        }
    }
    """
    await page.locator('input[name="first_name"]').click()
    await asyncio.sleep(0.3)
    await page.locator('input[name="first_name"]').fill(kwargs['first_name'])
    await asyncio.sleep(0.3)
    await page.locator('input[name="last_name"]').click()
    await asyncio.sleep(0.3)
    await page.locator('input[name="last_name"]').fill(kwargs['last_name'])
    await asyncio.sleep(0.3)
    await page.locator('input[name="email"]').click()
    await asyncio.sleep(0.3)
    await page.locator('input[name="email"]').fill(kwargs['email'])
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='YYYY/MM/DD').click()
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='YYYY/MM/DD').fill(kwargs['birthdate'])
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='YYYY/MM/DD').press('Enter')
    await asyncio.sleep(0.3)
    await page.locator('div').filter(has_text=re.compile(f'^{kwargs['gender']}$')).get_by_role('radio').check()
    await asyncio.sleep(0.3)

async def f2(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "选择'Subscribe to Newsletter'",
        "experience": "在'Grant Application'表单中，需要选择'订阅新闻通讯'选项。找到'Subscribe to Newsletter'文本旁边的复选框，并点击该复选框以选中它。确保复选框被成功选中以表示您的订阅意图。",
        "parameters": {
            "subscribe_to_newsletter": "选择是否订阅新闻通讯, {'checked': '订阅'}, 变量类型: str"
        }
    }
    """
    if kwargs['subscribe_to_newsletter'] == 'checked':
        await page.get_by_role('checkbox').check()
    await asyncio.sleep(0.3)

async def f3(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "点击 'Submit' 按钮",
        "experience": "在填写这个申请表之前，不要直接点击 'Submit' 按钮。需要先填写相应的输入框，包括 'First Name', 'Last Name', 'Email' 和 'Date of Birth'。另外，需要选择一个选项来表示性别，并决定是否订阅新闻通讯。完成这些步骤后，再点击 'Submit' 按钮进行提交。",
        "parameters": {}
    }
    """
    await page.get_by_role('button', name='Submit').click()
    await asyncio.sleep(0.3)

target_url = "http://127.0.0.1:5000/academic-research/grant-application"

register_func = [
    f1, f2, f3
]

dependencies = {
    f3.__name__: [f1, f2]
}

availables = {
    f1.__name__ : ['low', 'high'],
    f2.__name__ : ['low', 'high'],
    f3.__name__ : ['low', 'high'],
}
