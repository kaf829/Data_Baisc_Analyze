try:
    from bs4 import BeautifulSoup
    print("BeautifulSoup이 정상적으로 임포트되었습니다.")
except ImportError as e:
    print("ImportError 발생:", e)