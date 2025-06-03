import qrcode


data = "http://172.20.10.2"


qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)

# 데이터 추가
qr.add_data(data)
qr.make(fit=True)

# QR 코드 이미지를 생성
img = qr.make_image(fill='black', back_color='white')

# 이미지 저장
img.save("example_qr_code.png")