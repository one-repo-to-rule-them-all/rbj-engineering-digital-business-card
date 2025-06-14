import qrcode
ip_address = "one-repo-to-rule-them-all.github.io/rbj-digital-business-card/"  # Replace with your actual local IP
url = f"http://{ip_address}"
img = qrcode.make(url)
img.save("business_card_qr.png")