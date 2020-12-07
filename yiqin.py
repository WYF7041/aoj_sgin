import requests
import re

user = "2701200522"
pwd = "214015"
sckey = 'SCU88565T86438ff48954bbd839e4d47b80c21e7c5e659f4116728'

login_url = 'http://xgb.ahstu.edu.cn/SPCP/Web/'
sign_url = 'http://xgb.ahstu.edu.cn/SPCP/Web/Report/Index'
push_url = 'https://sc.ftqq.com/' + sckey + '.send'
login_data = {
    "StuLoginMode": "1",
    "txtUid": user,
    "txtPwd": pwd,
    "codeInput": "不讲武德"
}
login_header = {
    "Host": "xgb.ahstu.edu.cn",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Accept": "ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "112",
    "Origin": "http://xgb.ahstu.edu.cn",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "http://xgb.ahstu.edu.cn/SPCP/Web/",
    "Upgrade-Insecure-Requests": "1"}
sign_data = {
    "StudentId": "2701200522",
    "Name": "许可",
    "Sex": "男",
    "SpeType": "B",
    "CollegeNo": "315",
    "SpeGrade": "2020",
    "SpecialtyName": "计算机科学与技术",
    "ClassName": "计算机科学与技术205",
    "MoveTel": "13335561963",
    "Province": "340000",
    "City": "340300",
    "County": "340303",
    "ComeWhere": "安徽科技学院",
    "FaProvince": "340000",
    "FaCity": "340800",
    "FaCounty": "340802",
    "FaComeWhere": "山水云间256-2",
    "radio_1": "71a16876-3d52-4510-8c96-09b232a0161b",
    "radio_2": "083d90f5-5fa2-4a6d-a231-fe315b5104a3",
    "radio_3": "994c60eb-6f68-48bd-8bda-49a8a7ea812c",
    "radio_4": "a99d5cba-f691-4372-9487-4988dba252f1",
    "radio_5": "a48da759-c31e-4939-bb67-de7652913f15",
    "radio_6": "f32a114c-1dca-46eb-9f02-ef8c11a22c98",
    "radio_7": "afcfb6e2-ec9f-457d-8b72-37d13e958ace",
    "radio_8": "4c7e1f35-0c15-48f4-bbf3-49cd657c6553",
    "radio_9": "6dd9b137-651c-4d18-9479-44854666f57e",
    "radio_10": "558acb85-cb5c-451a-af77-573c4df8856c",
    "radio_11": "3e991072-cb63-40d5-8aef-7fdc4bc02cda",
    "radio_12": "669acedd-9e94-48e7-abe9-e90c5bcf75d7",
    "radio_13": "e742629f-8cb7-4533-bf6e-7141befe77e1",
    "Other": "",
    "GetAreaUrl": "/SPCP/Web/Report/GetArea",
    "IdCard": "340811200107214015",
    "ProvinceName": "安徽省",
    "CityName": "蚌埠市",
    "CountyName": "蚌山区",
    "FaProvinceName": "安徽省",
    "FaCityName": "安庆市",
    "FaCountyName": "迎江区",
    "radioCount": "13",
    "checkboxCount": "0",
    "blackCount": "0",
    "PZData": "[{\"OptionName\":\"以上症状都没有\",\"SelectId\":\"71a16876-3d52-4510-8c96-09b232a0161b\","
              "\"TitleId\":\"eb0c8db7-b4dd-4ad6-b58a-626fc3336f16\",\"OptionType\":\"0\"},{\"OptionName\":\"否，身体健康\","
              "\"SelectId\":\"083d90f5-5fa2-4a6d-a231-fe315b5104a3\","
              "\"TitleId\":\"a9a30b10-f88e-4776-ac74-b5a10fa11886\",\"OptionType\":\"0\"},"
              "{\"OptionName\":\"否，不是疑似感染者\",\"SelectId\":\"994c60eb-6f68-48bd-8bda-49a8a7ea812c\","
              "\"TitleId\":\"37e33b7d-5575-48c3-b59b-d4b7f6a6a0b5\",\"OptionType\":\"0\"},{\"OptionName\":\"否\","
              "\"SelectId\":\"a99d5cba-f691-4372-9487-4988dba252f1\","
              "\"TitleId\":\"a411c056-62c8-40a7-bce5-5b34cccf0a1f\",\"OptionType\":\"0\"},{\"OptionName\":\"否\","
              "\"SelectId\":\"a48da759-c31e-4939-bb67-de7652913f15\","
              "\"TitleId\":\"0c9e5609-6772-45d4-9109-ed0fbfdde79a\",\"OptionType\":\"0\"},{\"OptionName\":\"否\","
              "\"SelectId\":\"f32a114c-1dca-46eb-9f02-ef8c11a22c98\","
              "\"TitleId\":\"a1d15ae0-1f68-41a0-a546-a6a6a947fb2c\",\"OptionType\":\"0\"},{\"OptionName\":\"否\","
              "\"SelectId\":\"afcfb6e2-ec9f-457d-8b72-37d13e958ace\","
              "\"TitleId\":\"c7158ce4-96c6-445f-b47c-47729026183b\",\"OptionType\":\"0\"},{\"OptionName\":\"否\","
              "\"SelectId\":\"4c7e1f35-0c15-48f4-bbf3-49cd657c6553\","
              "\"TitleId\":\"c7f95504-e765-48c3-8102-251fdcfa3c61\",\"OptionType\":\"0\"},{\"OptionName\":\"否\","
              "\"SelectId\":\"6dd9b137-651c-4d18-9479-44854666f57e\","
              "\"TitleId\":\"1f8d7172-5ab4-40bf-8345-50e84030e803\",\"OptionType\":\"0\"},{\"OptionName\":\"否\","
              "\"SelectId\":\"558acb85-cb5c-451a-af77-573c4df8856c\","
              "\"TitleId\":\"fde86af0-b7b7-4cce-be73-9f1e071bf7fc\",\"OptionType\":\"0\"},"
              "{\"OptionName\":\"未接触不用隔离\",\"SelectId\":\"3e991072-cb63-40d5-8aef-7fdc4bc02cda\","
              "\"TitleId\":\"67f4f1c7-961e-423f-a102-18fd53722285\",\"OptionType\":\"0\"},"
              "{\"OptionName\":\"未接触不用隔离\",\"SelectId\":\"669acedd-9e94-48e7-abe9-e90c5bcf75d7\","
              "\"TitleId\":\"3bc5e2d3-e3c1-4b27-a789-e2f8921798ef\",\"OptionType\":\"0\"},{\"OptionName\":\"否\","
              "\"SelectId\":\"e742629f-8cb7-4533-bf6e-7141befe77e1\","
              "\"TitleId\":\"031aa1ff-e97a-40bf-a8ee-f6808d99016f\",\"OptionType\":\"0\"}]"
}


def server_push(push_information, push_context, server_url):
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"}
    requests.get(server_url + '?text=' + push_information + '&desp=' + push_context, headers=header)


login = requests.post(login_url, data=login_data, headers=login_header, allow_redirects=False).cookies
sign = requests.post(sign_url, cookies=login, data=sign_data).text
response = re.search(r'content: \'(.*?)\'', sign).group()[10:-1]
if response == '提交成功！':
    server_push('疫情填报完成', response, push_url)
else:
    server_push('疫情填报出问题了', response, push_url)
