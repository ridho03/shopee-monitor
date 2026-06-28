python
    import os
    import requests
    from playwright.sync_api import sync_playwright

    def send_telegram(message):
        token = os.environ.get('TELEGRAM_TOKEN')
        chat_id = os.environ.get('CHAT_ID')

        if not token or not chat_id:
            print("Error: TELEGRAM_TOKEN atau CHAT_ID tidak diset di Secrets!")
            return

        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        try:
            requests.get(url)
        except Exception as e:
            print(f"Gagal kirim: {e}")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://shopee.co.id/underprice_skincare")
            page.wait_for_timeout(15000)

            if "Skintific" in page.content():
                send_telegram("🔥 Produk Skintific ditemukan!")
            else:
                send_telegram("Bot jalan, Skintific tidak ditemukan.")
            browser.close()
    except Exception as e:
        print(f"Error sistem: {e}")
