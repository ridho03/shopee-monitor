python
    import os
    import requests
    from playwright.sync_api import sync_playwright

    def send_telegram(message):
        token = os.environ.get('TELE')
        chat_id = os.environ.get('CHAT_ID')
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://shopee.co.id/underprice_skincare")
        page.wait_for_timeout(10000) # Tunggu 10 detik agar data loading

        if "Skintific" in page.content():
            send_telegram("🔥 Ada produk Skintific di toko!")
        else:
            print("Tidak ditemukan.")
        browser.close()

 
