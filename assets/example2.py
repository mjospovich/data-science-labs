import time
from colorama import init, Fore, Style
from playwright.sync_api import sync_playwright

# Initialize colorama for colored output
init()

def smooth_scroll(page, direction='down'):
    """Perform smooth scrolling"""
    if direction == 'down':
        # Scroll down smoothly in small steps
        for i in range(0, 1000, 100):  # Scroll down 1000 pixels total
            page.evaluate(f"window.scrollTo({{top: {i}, behavior: 'smooth'}})")
            time.sleep(0.15)  # Small delay between each scroll step
    else:
        # Scroll up smoothly in small steps
        for i in range(1000, 0, -100):  # Scroll back to the top 1000 pixels
            page.evaluate(f"window.scrollTo({{top: {i}, behavior: 'smooth'}})")
            time.sleep(0.20)

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
            
            # Wait 1 second after accepting cookies
            time.sleep(1)
            
            # Perform smooth scrolling down
            print(f"{Fore.BLUE}Scrolling down...{Style.RESET_ALL}")
            smooth_scroll(page, 'down')
            
            # Perform smooth scrolling up
            print(f"{Fore.BLUE}Scrolling up...{Style.RESET_ALL}")
            smooth_scroll(page, 'up')

            # Wait for 1 second
            print(f"{Fore.BLUE}Waiting for 1 second...{Style.RESET_ALL}")
            time.sleep(1)
            
            # Click the search button
            print(f"{Fore.BLUE}Clicking search button...{Style.RESET_ALL}")
            search_button = page.locator('button.ant-btn.uppercase.style__searchButton___2NiBR')
            if search_button.is_visible():
                search_button.click()
                print(f"{Fore.GREEN}Successfully clicked search button{Style.RESET_ALL}")
            
            # Wait for 5 seconds before closing
            print(f"{Fore.BLUE}Waiting for 5 seconds...{Style.RESET_ALL}")
            time.sleep(5)
            
        finally:
            # Close the browser
            print(f"{Fore.BLUE}Closing browser...{Style.RESET_ALL}")
            browser.close()

if __name__ == "__main__":
    main()