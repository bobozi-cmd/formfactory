
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写创业公司融资申请表并提交",
        "experience": "在填写创业资助申请表时，请遵循以下步骤以确保输入的数据满足格式和限制要求：\n\n1. **公司信息**：\n   - 点击 'Company Name' 输入框，输入公司的名称。\n   - 点击 'Company Website' 输入框，确保输入格式为 'http://www.example.com' 或 'https://www.example.com'。\n   - 选择 'Business Stage' 下拉框，从选项中选择，例如 'Startup', 'Growth', 'Established'。\n   - 点击 'Founding Date' 输入框，以 'yyyy/mm/dd' 格式输入成立日期。\n\n2. **创始人信息**：\n   - 在 'Founder Name' 输入框中输入姓名。\n   - 在 'Email' 输入框中输入有效电子邮件地址，格式为 'username@example.com'。\n   - 在 'Phone Number' 输入框中输入有效的电话号码。\n   - 在 'LinkedIn Profile' 输入框中输入完整的 URL 网址。\n\n3. **公司需求**：\n   - 在 'Funding Amount Required (USD)' 输入框中，输入正数，代表所需的资金金额。\n   - 在 'Equity Offered (%)' 输入框中，输入0到100之间的有效百分比。\n   - 在 'Current Company Valuation (USD)' 输入框中，输入公司的估值，应为正数。\n   - 在 'Purpose of Funding' 输入框中，输入对资金用途的简洁描述。\n\n4. **业务概览**：\n   - 在 'Business Model' 输入框中输入适当的业务模型描述。\n   - 在 'Target Market' 输入框中输入目标市场的名称。\n   - 在 'Current Monthly Revenue (USD)' 输入框中，输入不低于0的月收入数值。\n   - 在 'Current Team Size' 输入框中，输入代表团队规模的大于零的整数。\n\n5. **附加信息**：\n   - 在 'Additional Comments' 输入框中填入额外的说明或信息。\n\n完成以上步骤后，点击 'Submit Application' 按钮提交申请。确保所有字段的数据均正确无误，以顺利提交申请并获得确认返回消息。",
        "parameters": {
            "company_name": "公司名称, 变量类型: str",
            "company_website": "公司网站, 确保输入格式为 'http://www.example.com' 或 'https://www.example.com', 变量类型: str",
            "business_stage": "公司业务阶段, {'Idea': 'Idea', 'MVP': 'MVP', 'Early Revenue': 'Early Revenue', 'Growth': 'Growth'}, 变量类型: str",
            "founding_date": "公司成立日期, 格式: YYYY-MM-DD, 变量类型: str",
            "founder_name": "创始人名字, 变量类型: str",
            "founder_email": "创始人邮箱, 变量类型: str",
            "founder_phone": "创始人联系电话, 变量类型: str",
            "linkedin_profile": "创始人 LinkedIn 网址, 确保输入格式为 'http://www.example.com' 或 'https://www.example.com', 变量类型: str",
            "funding_amount": "所需融资金额 (USD), 变量类型: int",
            "equity_offered": "提供的股权 (%)，范围：0-100, 变量类型: int",
            "current_valuation": "当前公司估值 (USD), 变量类型: int",
            "funding_purpose": "融资用途, 变量类型: str",
            "business_model": "商业模式, 变量类型: str",
            "target_market": "目标市场, 变量类型: str",
            "current_revenue": "当前每月收入 (USD), 变量类型: int",
            "team_size": "现有团队规模, 变量类型: int",
            "additional_comments": "附加备注, 变量类型: str"
        }
    }
    """
    await page.get_by_role('textbox', name='Company Name').fill(kwargs['company_name'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Company Website').fill(kwargs['company_website'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_label('Business Stage').select_option(kwargs['business_stage'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Founding Date').fill(kwargs['founding_date'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Founder Name').fill(kwargs['founder_name'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Email').fill(kwargs['founder_email'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Phone Number').fill(kwargs['founder_phone'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='LinkedIn Profile').fill(kwargs['linkedin_profile'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Funding Amount Required (USD)').fill(str(kwargs['funding_amount']))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Equity Offered (%)').fill(str(kwargs['equity_offered']))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Current Company Valuation (').fill(str(kwargs['current_valuation']))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Purpose of Funding').fill(kwargs['funding_purpose'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Business Model').fill(kwargs['business_model'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Target Market').fill(kwargs['target_market'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Current Monthly Revenue (USD)').fill(str(kwargs['current_revenue']))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Current Team Size').fill(str(kwargs['team_size']))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Additional Comments').fill(kwargs['additional_comments'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Submit Application').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/professional-business/startup-funding"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
