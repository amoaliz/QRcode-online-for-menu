
import qrcode

# لینک گوگل درایو را اینجا بگذار
link = "https://drive.google.com/file/d/184zuzYD79FN0dOrPFf4qyuBki-xzpC28/view?usp=drive_link"

# QR بساز
file = qrcode.make(link)

# ذخیره کن
file.save("s.png")
file.show()