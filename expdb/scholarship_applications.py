
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写奖学金申请表",
        "experience": "首先在 'First Name' 文本框中输入名字，然后在 'Middle Name' 和 'Last Name' 文本框中逐一输入中间名和姓氏。接下来，在 'Student ID' 文本框中键入学号。在 'Current GPA' 文本框中填写当前 GPA，并在 'Major/Field of Study' 文本框中输入所学专业。对于选择框 'Academic Year'，可选项包括 'Freshman', 'Sophomore', 'Junior', 'Senior'；确保选择最符合实际情况的一项。在选择 'Current Financial Aid' 时，可选项包括 'None', 'Partial', 'Full' 等。然后，在 'Annual Family Income' 文本框中输入年家庭收入。在 'Academic Achievements' 文本框中输入学术成就，使用换行符分隔不同条目。在 'Extracurricular Activities' 文本框中输入课外活动，也使用换行符分隔。在 'Statement of Purpose (500 words max)' 文本框中输入个人陈述，注意字数限制。最后，在 'Academic Reference' 输入推荐人姓名，并在 'Reference Email' 里填写推荐人邮箱。完成后，点击 'Submit Application' 按钮提交申请。",
        "parameters": {
            "first_name": "申请者的名字, 变量类型: str",
            "middle_name": "申请者的中间名, 变量类型: str",
            "last_name": "申请者的姓, 变量类型: str",
            "student_id": "学生证号码, 变量类型: str",
            "current_gpa": "当前 GPA, 变量类型: float",
            "major": "主修专业, 变量类型: str",
            "academic_year": "学年, {'': 'Select year', 'freshman': 'Freshman', 'sophomore': 'Sophomore', 'junior': 'Junior', 'senior': 'Senior', 'graduate': 'Graduate'}, 变量类型: str",
            "financial_aid": "当前的经济资助情况, {'': 'Select option', 'none': 'None', 'loans': 'Student Loans', 'grants': 'Grants', 'other': 'Other Scholarships'}, 变量类型: str",
            "annual_family_income": "家庭年收入, 变量类型: str",
            "academic_achievements": "学术成就, 使用换行符分隔不同条目, 变量类型: str",
            "extracurricular_activities": "课外活动, 使用换行符分隔不同条目, 变量类型: str",
            "statement_of_purpose": "Purpose 陈述, 变量类型: str",
            "academic_reference": "学术推荐人, 变量类型: str",
            "reference_email": "推荐人的邮箱, 变量类型: str"
        }
    }
    """
    await page.get_by_role('textbox', name='First Name').fill(kwargs['first_name'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Middle Name').fill(kwargs['middle_name'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Last Name').fill(kwargs['last_name'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Student ID').fill(kwargs['student_id'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('spinbutton', name='Current GPA').fill(str(kwargs['current_gpa']))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Major/Field of Study').fill(kwargs['major'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_label('Academic Year').select_option(kwargs['academic_year'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_label('Current Financial Aid').select_option(kwargs['financial_aid'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Annual Family Income').fill(kwargs['annual_family_income'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Academic Achievements').fill(kwargs['academic_achievements'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Extracurricular Activities').fill(kwargs['extracurricular_activities'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Statement of Purpose (500').fill(kwargs['statement_of_purpose'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Academic Reference').fill(kwargs['academic_reference'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Reference Email').fill(kwargs['reference_email'])
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Submit Application').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/academic-research/scholarship-application"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
