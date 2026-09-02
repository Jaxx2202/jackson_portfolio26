from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    ctx = b.new_context()
    page = ctx.new_page()
    page.goto('file:///home/claude/github_site/index.html')
    page.wait_for_timeout(300)
    with ctx.expect_page() as new_page_info:
        page.click('#card-7 .card-header')
        page.wait_for_timeout(300)
        page.click('#card-7 a.card-link')
    new_page = new_page_info.value
    new_page.wait_for_timeout(300)
    print("opened url:", new_page.url)
    print("has gate:", new_page.is_visible('#access-gate'))
    b.close()
