from genericpath import isfile
import json
import os

"""
@create_time: 2022-10-07
"""

class JsonUtils:
    def __init__(self, filename:str = 'output.json', save_root_path = './', init_dict:dict = {}) -> None:
        '''
            这一段代码其实没有什么意义，基本上只要使用静态函数即可
        '''
        self.save_root_path = save_root_path
        self.filename = os.path.join(self.save_root_path + filename)
        
        if os.path.isfile(filename):        # 如果指定目录存在该文件，则读取
            self.content = JsonUtils.load_json_4dict(filename=filename)
        else:
            self.content = init_dict
        
    def close(self):
        JsonUtils.mkdir(self.save_root_path)
        JsonUtils.save_json_4dict(self.content, self.filename)


    # 新建文件夹
    @staticmethod
    def mkdir(path: str) -> None:
        path.strip()
        path.rstrip('\\')
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)

    @staticmethod
    def load_json_4dict(filename: str) -> dict:
        '''
            @function:      读取json文件到 字典 , UTF-8格式
            @desciption:    UTF-8格式字符
        '''
        file = open(filename, 'r', encoding='UTF-8')
        js = file.read()
        file.close()
        dic = json.loads(js)
        return dic

    @staticmethod
    def save_json_4dict(data: dict, filename: str, is_ensure_ascii=False, is_indent=4) -> None:
        '''
            @function:      从 字典 到json
            @desciption:    默认带缩进；UTF-8格式字符默认不转成 ASCII码格式（即json文件内容可以显示中文）
        '''
        js_content = json.dumps(data, ensure_ascii=is_ensure_ascii, indent=is_indent, sort_keys=False)
        file = open(filename, 'w', encoding='UTF-8')
        file.write(js_content)
        file.close()


if __name__=="__main__":
    """
        测试使用方法
    """
    test = JsonUtils(init_dict={'1': 333})
    test.close()

    data = JsonUtils.load_json_4dict('output.json')
    data['2'] = 21321321

    JsonUtils.save_json_4dict(data, './output.json')