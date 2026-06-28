python
    import os
    import requests
    from playwright.sync_api import sync_playwright

    def send_telegram(message):
        token = os.environ.get('TELE_TOKEN')
        chat_id = os.environ.get('CHAT_ID')

        if not token or not chat_id:
            print("Error: TELE_TOKEN atau CHAT_ID tidak ditemukan di sistem!")
            return

        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        try:
            requests.get(url)
            print("Pesan terkirim ke Telegram.")
        except Exception as e:
            print(f"Gagal kirim ke Telegram: {e}")

    try:
        with sync_playwright() as p:
            # Menjalankan browser
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Buka link
            print("Membuka Shopee...")
            page.goto("https://shopee.co.id/underprice_skincare")

            # Tunggu agar loading selesai
            page.wait_for_timeout(15000)

            # Cek konten
            content = page.content()
            if "Skintific" in content:
                print("Berhasil: Produk Skintific ditemukan!")
                send_telegram("🔥 Ada produk Skintific di toko underprice_skincare!")
            else:
                print("Gagal: Produk Skintific tidak ditemukan di halaman utama.")
                # Opsional: kirim pesan kalau bot jalan tapi produk tidak ada
                send_telegram("Bot berjalan, tapi Skintific tidak ditemukan di halaman depan.")

            browser.close()
    except Exception as e:
        print(f"Error pada skrip: {e}")
