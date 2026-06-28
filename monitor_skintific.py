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

    4. Klik Commit changes.

    4. Buat File Otomatisasi (Agar jalan tiap jam)
    1. Di repository, klik Add file > Create new file.
    2. Di kolom nama file, ketik persis: .github/workflows/monitor.yml (GitHub akan otomatis buat foldernya).
    3. Paste kode ini:

    yaml
    name: Monitor Shopee
    on:
      schedule:
        - cron: "0 * * * *" # Jalan tiap jam
      workflow_dispatch: # Bisa diklik tombol "Run" manual

    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
          - name: Install Python
            uses: actions/setup-python@v4
            with: {python-version: '3.9'}
          - name: Install & Run
            env:
              TELE: ${{ secrets.TELE }}
              CHAT_ID: ${{ secrets.CHAT_ID }}
            run: |
              pip install playwright requests
              playwright install chromium
              python monitor_skintific.py
