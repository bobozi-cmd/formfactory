# grant_application.py

## f1
### record
```python
import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("http://127.0.0.1:5000/academic-research/grant-application")
    await page.locator("input[name=\"first_name\"]").click()
    await page.locator("input[name=\"first_name\"]").fill("zhou")
    await page.locator("input[name=\"last_name\"]").click()
    await page.locator("input[name=\"last_name\"]").fill("xiaoming")
    await page.locator("input[name=\"email\"]").click()
    await page.locator("input[name=\"email\"]").fill("1210611257@qq.com")
    await page.get_by_role("textbox", name="YYYY/MM/DD").click()
    await page.get_by_role("textbox", name="YYYY/MM/DD").fill("2025/10/01")
    await page.get_by_role("textbox", name="YYYY/MM/DD").press("Enter")
    await page.locator("div").filter(has_text=re.compile(r"^Male$")).get_by_role("radio").check()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
```

### summarize
```bash
python ./summarize.py playwright -f ./tmp_record.py -o ./tmp_out.py -u "http://127.0.0.1:5000/academic-research/grant-application" 
INFO     [browser_use] BrowserUse logging setup complete with level error
INFO     [telemetry] Anonymized telemetry enabled. See https://docs.browser-use.com/development/telemetry for more information.
⚠️ [Low level] 你的任务要求: 
[INFO] 2025-10-29 19:54:07 Create a new browser instance
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 19:54:07 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 19:54:07 Set timeout to 5000ms
Enter anything after login > 
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 19:54:26 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 19:54:27 Set timeout to 5000ms
Enter anything to continue >
⚠️ [Low level] 当前阶段生成的代码:

from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime
from replayer.playwright.tools import ToolBox

async def run(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写用户基本信息，包括名字、邮箱、出生日期和性别。",
        "experience": "",
        "parameters": {
            "first_name": "用户的名字, 变量类型: str",
            "last_name": "用户的姓氏, 变量类型: str",
            "email": "用户的电子邮件地址, 变量类型: str",
            "birth_date": "用户的出生日期，格式为 YYYY/MM/DD, 变量类型: str",
            "gender": "用户的性别选项，是否选择 'Male', 变量类型: str"
        }
    }
    """
    await page.locator('input[name="first_name"]').click()
    await asyncio.sleep(0.3)
    await page.locator('input[name="first_name"]').fill(kwargs.get('first_name', 'zhou'))
    await asyncio.sleep(0.3)
    await page.locator('input[name="last_name"]').click()
    await asyncio.sleep(0.3)
    await page.locator('input[name="last_name"]').fill(kwargs.get('last_name', 'xiaoming'))
    await asyncio.sleep(0.3)
    await page.locator('input[name="email"]').click()
    await asyncio.sleep(0.3)
    await page.locator('input[name="email"]').fill(kwargs.get('email', '1210611257@qq.com'))
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='YYYY/MM/DD').click()
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='YYYY/MM/DD').fill(kwargs.get('birth_date', '2025/10/01'))
    await asyncio.sleep(0.3)
    await page.get_by_role('textbox', name='YYYY/MM/DD').press('Enter')
    await asyncio.sleep(0.3)
    if kwargs.get('gender', 'Male') == 'Male':
        await page.locator('div').filter(has_text=re.compile('^Male$')).get_by_role('radio').check()
    await asyncio.sleep(0.3)
[Low level] 如果生成的结果不满意, 请输入新的需求来重新生成; 如果满意生成的结果, 输入 c 进入下一步生成 > 对于性别，你需要可以根据参数选择male还是female
⚠️ [Low level] 你的任务要求: 对于性别，你需要可以根据参数选择male还是female
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 19:55:19 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 19:55:20 Set timeout to 5000ms
Enter anything after login > 
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 19:55:38 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 19:55:38 Set timeout to 5000ms
Enter anything to continue >
⚠️ [Low level] 当前阶段生成的代码:

from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime
from replayer.playwright.tools import ToolBox

async def run(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "填写用户基本信息，包括名字、邮箱、出生日期和性别。",
        "experience": "",
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
[Low level] 如果生成的结果不满意, 请输入新的需求来重新生成; 如果满意生成的结果, 输入 c 进入下一步生成 > c
⚠️ [High level] 你的任务要求: 
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 19:55:56 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 19:55:56 Set timeout to 5000ms
Enter anything after prepared > 
[DEBUG] 2025-10-29 19:55:58 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:55:58 Resize Image 88412 -> 63504
⚠️ Please execute step:
await page.locator('input[name="first_name"]').click()
Enter anything after executed > 
[DEBUG] 2025-10-29 19:56:04 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:56:04 Resize Image 89356 -> 64320
⚠️ Please execute step:
await page.locator('input[name="first_name"]').fill('zhou')
Enter anything after executed > 
[DEBUG] 2025-10-29 19:56:08 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:56:08 Resize Image 91688 -> 66116
⚠️ Please execute step:
await page.locator('input[name="last_name"]').click()
Enter anything after executed > 
[DEBUG] 2025-10-29 19:56:12 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:56:12 Resize Image 91324 -> 65800
⚠️ Please execute step:
await page.locator('input[name="last_name"]').fill('xiaoming')
Enter anything after executed > 
[DEBUG] 2025-10-29 19:56:16 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:56:16 Resize Image 95660 -> 68920
⚠️ Please execute step:
await page.locator('input[name="email"]').click()
Enter anything after executed > 
[DEBUG] 2025-10-29 19:56:21 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:56:21 Resize Image 95236 -> 68756
⚠️ Please execute step:
await page.locator('input[name="email"]').fill('1210611257@qq.com')
Enter anything after executed > 
[DEBUG] 2025-10-29 19:56:27 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:56:27 Resize Image 105124 -> 75076
⚠️ Please execute step:
await page.get_by_role('textbox', name='YYYY/MM/DD').click()
Enter anything after executed > 
[DEBUG] 2025-10-29 19:56:30 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:56:30 Resize Image 158092 -> 111372
⚠️ Please execute step:
await page.get_by_role('textbox', name='YYYY/MM/DD').fill('2025/10/01')
Enter anything after executed > 
[DEBUG] 2025-10-29 19:56:37 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:56:37 Resize Image 157664 -> 110604
⚠️ Please execute step:
await page.get_by_role('textbox', name='YYYY/MM/DD').press('Enter')
Enter anything after executed > 
[DEBUG] 2025-10-29 19:56:41 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:56:41 Resize Image 103568 -> 73588
⚠️ Please execute step:
await page.locator('div').filter(has_text=re.compile('^Male$')).get_by_role('radio').check()
Enter anything after executed > 
[DEBUG] 2025-10-29 19:56:45 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 19:56:45 Resize Image 103988 -> 73684
⚠️ [High level] 当前阶段生成的代码:

from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime
from replayer.playwright.tools import ToolBox

async def run(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
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
[High level] 如果生成的结果不满意, 请输入新的需求来重新生成; 如果满意生成的结果, 输入 c 进入下一步生成 > c
```

## f2
### record
```python
import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("http://127.0.0.1:5000/academic-research/grant-application")
    await page.get_by_role("checkbox").check()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
```

### summarize
```bash
python ./summarize.py playwright -f ./tmp_record.py -o ./tmp_out.py -u "http://127.0.0.1:5000/academic-research/grant-application" -r "选择'Subscribe to Newsletter'"
INFO     [browser_use] BrowserUse logging setup complete with level error
INFO     [telemetry] Anonymized telemetry enabled. See https://docs.browser-use.com/development/telemetry for more information.
⚠️ [Low level] 你的任务要求: 选择'Subscribe to Newsletter'
[INFO] 2025-10-29 20:03:46 Create a new browser instance
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 20:03:46 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 20:03:46 Set timeout to 5000ms
Enter anything after login > 
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 20:03:56 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 20:03:56 Set timeout to 5000ms
Enter anything to continue >
⚠️ [Low level] 当前阶段生成的代码:

from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime
from replayer.playwright.tools import ToolBox

async def run(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "选择'Subscribe to Newsletter'",
        "experience": "",
        "parameters": {
            "subscribe_to_newsletter": "选择是否订阅新闻通讯, {'checked': '订阅'}, 变量类型: str"
        }
    }
    """
    if kwargs['subscribe_to_newsletter'] == 'checked':
        await page.get_by_role('checkbox').check()
    await asyncio.sleep(0.3)
[Low level] 如果生成的结果不满意, 请输入新的需求来重新生成; 如果满意生成的结果, 输入 c 进入下一步生成 > c
⚠️ [High level] 你的任务要求: 选择'Subscribe to Newsletter'
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 20:04:17 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 20:04:17 Set timeout to 5000ms
Enter anything after prepared > 
[DEBUG] 2025-10-29 20:04:25 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 20:04:25 Resize Image 88436 -> 63484
⚠️ Please execute step:
await page.get_by_role('checkbox').check()
Enter anything after executed > 
[DEBUG] 2025-10-29 20:04:32 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 20:04:32 Resize Image 88420 -> 63476
⚠️ [High level] 当前阶段生成的代码:

from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime
from replayer.playwright.tools import ToolBox

async def run(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
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
[High level] 如果生成的结果不满意, 请输入新的需求来重新生成; 如果满意生成的结果, 输入 c 进入下一步生成 > c
```

## f3
### record
```python
import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("http://127.0.0.1:5000/academic-research/grant-application")
    await page.get_by_role("button", name="Submit").click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
```

### summarize
```bash
python ./summarize.py playwright -f ./tmp_record.py -o ./tmp_out.py -u "http://127.0.0.1:5000/academic-research/grant-application"
INFO     [browser_use] BrowserUse logging setup complete with level error
INFO     [telemetry] Anonymized telemetry enabled. See https://docs.browser-use.com/development/telemetry for more information.
⚠️ [Low level] 你的任务要求: 
[INFO] 2025-10-29 20:08:44 Create a new browser instance
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 20:08:44 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 20:08:45 Set timeout to 5000ms
Enter anything after login > 
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 20:08:52 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 20:08:53 Set timeout to 5000ms
Enter anything to continue >
⚠️ [Low level] 当前阶段生成的代码:

from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime
from replayer.playwright.tools import ToolBox

async def run(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "点击 'Submit' 按钮",
        "experience": "",
        "parameters": {}
    }
    """
    await page.get_by_role('button', name='Submit').click()
    await asyncio.sleep(0.3)
[Low level] 如果生成的结果不满意, 请输入新的需求来重新生成; 如果满意生成的结果, 输入 c 进入下一步生成 > c
⚠️ [High level] 你的任务要求: 
INFO     [browser] 🔌  Connecting to remote browser via CDP http://localhost:9222
[INFO] 2025-10-29 20:09:03 http://localhost:9222 -> ws://localhost:9222/devtools/browser/f1a1df20-2498-4aad-bfb0-7460be673e77
INFO     [browser] 🍪  Loaded 735 cookies from ./.save/cookies.json
[DEBUG] 2025-10-29 20:09:03 Set timeout to 5000ms
Enter anything after prepared > 
[DEBUG] 2025-10-29 20:09:15 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 20:09:15 Resize Image 91964 -> 67504
⚠️ Please execute step:
await page.get_by_role('button', name='Submit').click()
Enter anything after executed > 
[DEBUG] 2025-10-29 20:09:20 Screenshot scale factor: 0.5
[DEBUG] 2025-10-29 20:09:20 Resize Image 92632 -> 67932
⚠️ [High level] 当前阶段生成的代码:

from playwright.async_api import expect, Browser, BrowserContext, Page
import asyncio
import re
from datetime import datetime
from replayer.playwright.tools import ToolBox

async def run(browser: Browser, context: BrowserContext, page: Page, **kwargs) -> None:
    r"""
    {
        "desc": "点击 'Submit' 按钮",
        "experience": "在填写这个申请表之前，不要直接点击 'Submit' 按钮。需要先填写相应的输入框，包括 'First Name', 'Last Name', 'Email' 和 'Date of Birth'。另外，需要选择一个选项来表示性别，并决定是否订阅新闻通讯。完成这些步骤后，再点击 'Submit' 按钮进行提交。",
        "parameters": {}
    }
    """
    await page.get_by_role('button', name='Submit').click()
    await asyncio.sleep(0.3)
[High level] 如果生成的结果不满意, 请输入新的需求来重新生成; 如果满意生成的结果, 输入 c 进入下一步生成 > c
```
