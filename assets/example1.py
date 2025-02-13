import time
from colorama import init, Fore, Style
from playwright.sync_api import sync_playwright

# Initialize colorama for colored output
init()

def main():
    print(f"{Fore.BLUE}Starting browser...{Style.RESET_ALL}")
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(
            headless=False,  # Set to True if you don't want to see the browser
            args=['--disable-blink-features=AutomationControlled']
        )
        
        # Create a new context
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        )
        
        # Create a new page
        page = context.new_page()
        
        try:
            # Navigate to Index Oglasi
            print(f"{Fore.BLUE}Navigating to Index Oglasi...{Style.RESET_ALL}")
            page.goto("https://www.index.hr/oglasi/auto-moto/osobni-automobili", wait_until='networkidle')
            
            # Handle cookie popup
            try:
                cookie_button = page.locator('button#didomi-notice-agree-button')
                if cookie_button.is_visible(timeout=3000):
                    cookie_button.click()
                    print(f"{Fore.GREEN}Successfully accepted cookies{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.YELLOW}Cookie popup not found or already accepted: {e}{Style.RESET_ALL}")
            
            # Wait for 5 seconds
            print(f"{Fore.BLUE}Waiting for 5 seconds...{Style.RESET_ALL}")
            time.sleep(5)
            
        finally:
            # Close the browser
            print(f"{Fore.BLUE}Closing browser...{Style.RESET_ALL}")
            browser.close()

if __name__ == "__main__":
    main()