def clean_email(email):
    """清洗邮箱地址:"""
    cleaned = email.strip().lower()
    return cleaned

#测试
raw_emails = [" John@EXAMPLE.COM " ," Alice@Test.IO","BOB@GMAIL.CO,"]

for email in raw_emails:
    print(f"原始:'{email}'\n清洗后:'{clean_email(email)}")

#任务2-URL域名提取器
def extract_domain(url):
    """从URL中提取域名部分"""
    cleaned = url.removeprefix("https://").removeprefix("http://")
    domain = cleaned.split("/")[0]
    return domain

#测试
test_urls = [
     "https://www.baidu.com/search?q=python",
    "http://example.org/page",
    "https://github.com/python/cpython"
]

for url in test_urls:
    print(f"清洗前:{url}\n清洗后:{extract_domain(url)}")

#任务3:格式化打印表格
students = ["Alice","Bob","Charlie","Diana"]
scores = [92,78,85,96]

print('='*30)
print(f"{'姓名':<12}{'成绩':>8}")
print('-'*30)
for name,score in zip(students,scores):
    print(f"{name:<12}{score:>8}")
print('='*30)



print()
str1 = "ABCDEFG"
result = " "
for i in str1:
    result += i.lower()
print(result)