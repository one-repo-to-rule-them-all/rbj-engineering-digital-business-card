import qrcode
ip_address = "one-repo-to-rule-them-all.github.io/rbj-engineering-digital-business-card/"  # Replace with your actual local IP
url = f"https://{ip_address}"
img = qrcode.make(url)
img.save("business_card_qr.png")