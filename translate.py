import json
import requests
import sys
import urllib

class NetworkError(Exception):
    '''网络连接异常类'''
    def __init__(self, why):
        print(why)
        self.why = why

class RequestError(Exception):
    '''获取响应错误类'''
    def __init__(self, why):
        print(why)
        self.why = why

class translate_class:
    '''翻译类'''
    def __init__(self):
        pass

    def translate(self, text) -> str:
        '''使用Kate·Api进行翻译'''
        try:
            ans = requests.get("https://api.66mz8.com/api/translation.php" + "?info=" + text) #获取响应
        except requests.exceptions.ConnectionError:
            raise NetworkError("[ERROR]Didn't connect to Internet") #没有网络连接
        
        if (ans.status_code != 200):
            raise RequestError("[ERROR]Request code " + ans.status_code) #响应错误

        ans = ans.json()

        try:
            ans = json.dumps(ans["fanyi"], ensure_ascii = False) #校对数据
        except KeyError:
            raise RequestError(ans["msg"])  #反馈错误原因
        
        ans = urllib.parse.unquote(ans) #UTF-8字符解析
        ans = eval(ans) #去除双引号
        
        return ans

##########################进行测试################################
import unittest
    
class test_translate_class(unittest.TestCase):
    def test(self):
        T = translate_class()
        for i in range(0, len(test) - 1):
            self.assertEqual(T.translate(test[i]), ans[i])

# 存放问题与答案
test = ['中国人', 'Chinese', '123', 'test', '测试']
ans  = ['Chinese', '中国人', '123', '测试', 'test']

if __name__ == "__main__":
    unittest.main()