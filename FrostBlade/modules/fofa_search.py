import threading
import subprocess
import modules
import requests
import base64
import xlwt
from lib import config
from lib import output

class MOD(modules.module):

    def __init__(self) -> None:
        super().__init__()
        self.output= output.cmd_output()
        self.module_name= 'fofa查询'
        self.module_author = 'haochen'
        self.module_explain = '通过fofaapi进行查询，并将结果输出到xlsx文件中'
        self.must_parameter={
            'search_msg' : ''
        }
        self.choo_parameter={
            'result_path': '',
            'fields' : 'host,ip,port,protocol,server,title,country_name'
        }

    def run(self):
        '''     
            运行函数      
        '''
        if self.choo_parameter['result_path'] != '':
            self.fofa_search(self.must_parameter['search_msg'],self.choo_parameter['fields'],self.choo_parameter['result_path'])
        else:
            self.fofa_search(self.must_parameter['search_msg'],self.choo_parameter['fields'])
    
    def fofa_search(self,search,fields = 'host,ip,port,protocol,server,title,country_name',result_path = 'result.xlsx'):
        username = config.fofa_username
        key = config.fofa_key
        search = base64.b64encode(search.encode()).decode()
        if username == '' or key == '':
            self.output.output_error('请先配置fofa用户名与key')
        else :
            url = "https://fofa.info/api/v1/search/all?email={}&key={}&qbase64={}&fields={}&full=true".format(username,key,search,fields)
            try:
                html = requests.get(url=url,timeout=5)
                out = html.json() 
                if out['error'] == True:
                    self.output.output_error('fofa访问出错！'+out['errmsg'])
                msg_list = out['results']
                title = fields.split(',')
                judge = self.write_xlsx(title,msg_list,result_path)
                if judge == True:
                    self.output.output_info('查询成功！请进入文件'+result_path+'查看')
                else:
                    self.output.output_error('写入文件失败！')
            except:
                self.output.output_error('fofa访问出错！')

    def write_xlsx(self,title,fofa_data,result_path):
        try:
            work = xlwt.Workbook(result_path)
            worksheet1 = work.add_sheet('result', cell_overwrite_ok=False)
            for i in range(len(title)):
                col = worksheet1.col(i)
                col.width = 256*20
            for i in range(0,len(title)):
                worksheet1.write(0,i,title[i])
            num_y = 1
            for i in fofa_data:
                num_x = 0
                for j in i:
                    worksheet1.write(num_y,num_x,j)
                    num_x+=1
                num_y+=1
            work.save(result_path)
            return True
        except:
            return False
            
        
        
