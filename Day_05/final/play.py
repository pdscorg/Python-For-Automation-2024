import re
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv
import os
import time

load_dotenv()


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://manaslu.pcampus.edu.np:443/login")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("078bct045.krishant@pcampus.edu.np")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill(os.environ.get('PASSWORD'))
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Projects").click()
    page.get_by_role("button", name="+ Add").click()
    page.get_by_placeholder("Your Cool Project").fill("test-react-2")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="production").click()
    page.get_by_role("link", name="+ Add New Resource").click()
    page.get_by_text("Public Repository").click()
    page.locator("#repository_url").click()
    page.locator("#repository_url").fill("https://github.com/thejungwon/docker-reactjs")
    page.get_by_role("button", name="Check repository").click()
    time.delay(5)
    page.get_by_role("button", name="Disable This Popup", exact=True).click()
    page.get_by_role("button", name="Acknowledge & Disable This").click()
    page.get_by_text("Build Pack * Nixpacks Static").click()
    page.locator("select[name=\"wkow8c0\"]").select_option("Dockerfile")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Deploy", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
