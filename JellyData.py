import requests
import re
import urllib
import xlwt

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
}

# 分析url
"""
http://www.furthertrading.co.uk/office.php/Index/jsondata?cmd=registration_list&catid=2&audit=1&_dc=1575533096799&page=2&start=30&limit=30&urlName
http://www.furthertrading.co.uk/office.php/Index/jsondata?cmd=registration_list&catid=2&audit=1&_dc=1575534354513&page=3&start=60&limit=30&urlName
http://www.furthertrading.co.uk/office.php/Index/jsondata?cmd=registration_list&catid=2&audit=1&_dc=1575534389849&page=4&start=90&limit=30&urlName
http://www.furthertrading.co.uk/office.php/Index/jsondata?cmd=registration_list&catid=2&audit=1&_dc=1575534411891&page=5&start=120&limit=30&urlName

page=1&start=0
page=2&start=30
page=3&start=60
page=4&start=90
page=5&start=120
"""
all_data_list = []


class Spider(object):
    def __init__(self):
        self.urlName = "limit=30&group=%5B%7B%22property%22%3A%22agentid%22%2C%22direction%22%3A%22desc%22%7D%5D&sort=%5B%7B%22property%22%3A%22agentid%22%2C%22direction%22%3A%22desc%22%7D%2C%7B%22property%22%3A%22creatdate%22%2C%22direction%22%3A%22desc%22%7D%5D"
        self.Page = 1
        # self.endPage = 6
        self.url = "http://www.furthertrading.co.uk/office.php/Index/jsondata?cmd=registration_list&catid=2&audit=1&_dc=1575533096799&"
        self.ua_header = header
        # self.fileName = 1

    # url + page + start + urlName

    # 构造url
    def json_data(self):
        for page in range(self.Page):
            start = (page - 1) * 30
            wd1 = {'page': page, 'start': start, 'urlName': self.urlName}
            wd2 = urllib.parse.urlencode(wd1)
            myurl = self.url + wd2
            self.loadPage(myurl)

    def loadPage(self, url):
        respones = requests.get(url, headers=self.ua_header).json()
        print(respones["plant"])
        for result in respones["plant"]:
            # print(result)
            usernames = result["username"]
            contacts = result["contact"]
            mobiles = result["mobile"]
            emails = result["email"]
            res_list = [usernames, contacts, mobiles, emails]
            all_data_list.append(res_list)
        print(all_data_list)
        return all_data_list

    def write_excel(self, all_data_list):
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('jelly_sheet1', cell_overwrite_ok=True)
        titel = ['登录账号', '账户姓名', '手机号码', '邮箱']  # 表头名称
        for t in range(len(titel)):
            sheet.write(0, t, titel[t])
        i = 1
        for list in all_data_list:
            j = 0
            for data in list:
                sheet.write(i, j, data)
                j += 1
            i += 1
        book.save('C:\/Users\/10169\Desktop\jellyData.xls')
        print("写入Excel成功...")


if __name__ == '__main__':
    mySpider = Spider()
    mySpider.json_data()
    mySpider.write_excel(all_data_list)

    # url = f"protocol://host:port/uri"
    # params = {
    #     "k": 1,
    #     "x": 2
    # }
    # import requests
    #
    # requests.get(
    #     url=url,
    #     params=params,
    #     headers=headers
    # ).json()

    # 正则匹配获取指定字段所有的值
    # result_login = re.findall(r"'username': '(.*?)'", str(respones))
    # result_contact = re.findall(r"'contact': '(.*?)'", str(respones))
    # result_phone = re.findall(r"'phone': '(.*?)'", str(respones))
    # result_email = re.findall(r"'email': '(.*?)'", str(respones))
    # print(result_login)
    # print(result_contact)
    # print(result_phone)
    # print(result_email)
    # Xpath定位
    # html = etree.HTML(respones)
    # login = html.xpath('//div[@class="x-grid-cell-inner"]')
    # print(login)
