python
    import os
    import requests
    from playwright.sync_api import sync_playwright

    def send_telegram(message):
        token = os.environ.get('TELEGRAM_TOKEN')
        chat_id = os.environ.get('CHAT_ID')
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)

    with sync_playwright() as p:
        # Menggunakan proxy agar tidak diblokir Shopee
        browser = p.chromium.launch(headless=True, proxy={"server": "http://lum.residential.proxy:22225"})
        page = browser.new_page()
        try:
            page.goto("https://shopee.co.id/underprice_skincare")
            page.wait_for_timeout(10000)

            if "Skintific" in page.content():
                send_telegram("Produk ditemukan!")
            else:
                send_telegram("Produk tidak ada.")
        except Exception as e:
            send_telegram(f"Error: {e}")
        browser.close()
