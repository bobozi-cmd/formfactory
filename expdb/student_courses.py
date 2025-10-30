
import os
from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime

INTERVAL = float(os.getenv('STEP_INTERVAL', 0.1))

async def f1(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "注册课程",
        "experience": "在进行课程注册时，用户需要依次填写相关信息。首先，点击并填写'Full Name'文本框，输入全名；然后依次点击并填写'Student ID'、'Email'和'Phone Number'文本框，分别输入学号、电子邮箱和电话号码。在课程选择部分，用户可以选择'Semester'和'Program'的下拉框，选择学期和专业。接着，在'课程选择'部分，用户可以勾选想要注册的课程，这些课程是可多选的，也可以不选任何课程。如果有特殊要求或评论，可在'Special Requirements or Comments'文本框进行填写。所有信息填写完成后，点击'Submit Registration'按钮提交注册。确保每一步操作前正确选中对应的输入框或复选框，确保选择和输入的信息准确无误。",
        "parameters": {
            "full_name": "填写的全名, 变量类型: str",
            "student_id": "学号, 变量类型: str",
            "email": "电子邮件地址, 变量类型: str",
            "phone_number": "电话号码, 变量类型: str",
            "semester": "学期, 变量类型: str, 可选: 'Fall 2025', 'Spring 2025', 'Summer 2025'",
            "program": "课程专业, 变量类型: str, 可选: 'Software Engineering', 'Computer Science', 'Data Science', 'Information Technology'",
            "special_requirements": "特殊要求, 变量类型: str",
            "courses": "选择的课程, 变量类型: list, 可选: 'CS101 - Introduction to', 'CS102 - Data Structures', 'CS103 - Database Systems', 'CS104 - Web Development'"
        }
    }
    """
    await page.get_by_role('textbox', name='Full Name').click()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Full Name').fill(kwargs.get('full_name'))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Student ID').click()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Student ID').fill(kwargs.get('student_id'))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Email').click()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Email').fill(kwargs.get('email'))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Phone Number').click()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Phone Number').fill(kwargs.get('phone_number'))
    await asyncio.sleep(INTERVAL)
    await page.get_by_label('Semester').select_option(kwargs.get('semester'))
    await asyncio.sleep(INTERVAL)
    await page.get_by_label('Program', exact=True).select_option(kwargs.get('program'))
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Special Requirements or').click()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('textbox', name='Special Requirements or').fill(kwargs.get('special_requirements'))
    await asyncio.sleep(INTERVAL)
    for course in kwargs.get('courses', []):
        await page.get_by_role('checkbox', name=course).check()
    await asyncio.sleep(INTERVAL)
    await page.get_by_role('button', name='Submit Registration').click()
    await asyncio.sleep(INTERVAL)

target_url = "http://127.0.0.1:5000/academic-research/course-registration"

register_func = [
    f1, 
]

dependencies = {
}

availables = {
    f1.__name__ : ['low', 'high'],
}
