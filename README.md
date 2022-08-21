### feign-python
### 项目介绍
```markdown
   项目描述: 本项目为feign的python实现，方便python项目与微服务项目快捷集成,目前只实现与注册中心nacos2集成,客户端负载支持(HASH,RANDOM,ROUND_ROBIN)默认IP-HASH
   作者: 黑肱
   邮箱: zuiwoxing@qq.com
```

### 项目安装
```
pip install feign-python
```
### 使用示例
#### 一. 第一种使用方式
```python
from requests import Response
from ldj.feign.decorator.FeignApi import FeignApi
from ldj.example.dto.models import QueryDto
from ldj.feign.enums.Method import Method

class DictApi:

    @staticmethod
    @FeignApi(method=Method.POST, uri="/shared/dict/api/dict/list",serviceId="shared", name="字典数据")
    def list(queryDto: QueryDto) -> Response: ...

    @staticmethod
    @FeignApi(method=Method.GET, uri="/shared/dict/api/dict/single",serviceId="shared",  name="查询枚举详情")
    def single(tenantKey:str,namespaceCode:str,
                    appCode: str, dictCode: str) -> Response: ...
                    
                    
 
#测试示例
from ldj.example import ExampleConfig
from ldj.example.DictApi import DictApi
from ldj.example.dto.models import QueryDto
from ldj.feign.model.Response import Response
def list_all():
    queryDto = QueryDto()
    queryDto.appCode = "shared"
    queryDto.namespaceCode = "default"
    queryDto.tenantKey = "05766005256305607631060124224200"
    print(queryDto.json())
    res: Response = DictApi.list(queryDto)
    print(res)

def dict_detail():
    res: Response = DictApi.single("05766005256305607631060124224200", "default", "shared", "PersonalStatus")
    print(res)
    data = res.result
    print(data)

ExampleConfig.init_nacos_config()
list_all()
dict_detail()

```
#### 二. 第二种使用方式 
```python
from requests import Response
from ldj.example.dto.models import QueryDto
from ldj.feign.decorator.Api import Api
from ldj.feign.decorator.Feign import Feign
from ldj.feign.enums.Method import Method

@Feign(prefix="/shared/dict/api/dict", serviceId="shared", name="共享服务-字典服务")
class DictApi2:

    @Api(method=Method.GET, uri="single", name="查询枚举详情")
    def single(self, tenantKey: str, namespaceCode: str,
               appCode: str, dictCode: str) -> Response: ...

    @Api(method=Method.POST, uri="list", name="查询字典列表数据")
    def list(self, queryDto: QueryDto) -> Response: ...
    
#测试示例
from ldj.example import ExampleConfig
from ldj.example.DictApi2 import DictApi2
from ldj.example.dto.models import QueryDto
from ldj.feign.model.Response import Response


def list_all():
    mydict = DictApi2()
    queryDto = QueryDto()
    queryDto.appCode = "shared"
    queryDto.namespaceCode = "default"
    queryDto.tenantKey = "05766005256305607631060124224200"
    print(queryDto.json())
    res = mydict.list(queryDto)
    print(res)


def dict_detail():
    mydict: DictApi2 = DictApi2()
    res: Response = mydict.single("05766005256305607631060124224200", "default", "shared", "PersonalStatus")
    print(res)
    data = res.result
    print(data)


ExampleConfig.init_nacos_config()
list_all()
dict_detail()
```
### 服务注册
```
   如果需要将本机服务发布到注册中心,可调用如下方法
   RegisterCenterHelper.init_register_center()
```
#### 三. 第三种使用方式-无注册中心
```python
 #直接调用方式,只需要配置serverUrl,如果serverUrl与serviceId同时存在，则以serverUrl为准,除非serverUrl被设置为None,则无效
from requests import Response
from ldj.example import ExampleConfig
from ldj.feign.decorator.FeignApi import FeignApi
from ldj.example.dto.models import QueryDto
from ldj.feign.enums.Method import Method


class DictApiNoCenter:

    @staticmethod
    @FeignApi(method=Method.POST, uri="/shared/dict/api/dict/list",serviceId="shared",
              serviceUrl=ExampleConfig.SERVER_URL, name="字典数据")
    def list(queryDto: QueryDto) -> Response: ...

    @staticmethod
    @FeignApi(method=Method.GET, uri="/shared/dict/api/dict/single",serviceId="shared",
              serviceUrl=ExampleConfig.SERVER_URL,  name="查询枚举详情")
    def single(tenantKey:str,namespaceCode:str,
                    appCode: str, dictCode: str) -> Response: ...
```

#### 四. 第四种使用方式-无注册中心
```python
from requests import Response
from ldj.example import ExampleConfig
from ldj.example.dto.models import QueryDto
from ldj.feign.decorator.Api import Api
from ldj.feign.decorator.Feign import Feign
from ldj.feign.enums.Method import Method


@Feign(prefix="/shared/dict/api/dict",serviceId="shared", serviceUrl=ExampleConfig.SERVER_URL, name="共享服务-字典服务")
class DictApi2NoCenter:

    @Api(method=Method.GET, uri="single", name="查询枚举详情")
    def single(self, tenantKey: str, namespaceCode: str,
               appCode: str, dictCode: str) -> Response: ...

    @Api(method=Method.POST, uri="list", name="查询字典列表数据")
    def list(self, queryDto: QueryDto) -> Response: ...
```
#### 五. 编码与解码规则
```markdown
   使用默认的 DefaultInterceptor,自己可根据需要继承 Interceptor,实现encode与decode即可。然后在Fegin中添加自己的实现即可
import requests
from ldj.feign.enums.Method import Method
from ldj.feign.interceptor.Interceptor import Interceptor, ProcessRequest
class MyInterceptor(Interceptor):
    def decode(self, resp: requests.Response) -> object:
        pass

    def encode(self, method: Method, headers: dict = None,
               params: dict = None, body: dict = None,
               data: object = None) -> ProcessRequest:
        pr = ProcessRequest()
        pr.method = method
        pr.headers = headers
        pr.params = params
        pr.body = body
        pr.data = data
        return pr

my_interceptor = MyInterceptor()
@Feign(prefix="/shared/dict/api/dict", serviceId="shared", interceptor=my_interceptor, name="共享服务-字典服务")
class DictApi2:
 pass
具体可参考DefaultInterceptor实现

默认响应体为(仅供参考):
class Response(BaseModel):
    """
    :param status 为http状态
    :param msg 响应消息
    :param code 业务编码
    :param data 业务数据
    """
    status: int = Constant.HTTP_SUCCESS
    message: str = ""
    code: int = Constant.BIZ_SUCCESS
    result: object = None
 pass
```
#### 六. 异常处理

```markdown
 异常默认是通过loguru来做日志记录,其默认实现 DefaultExceptionHandler。如果需要自定义异常处理只需要继承ExceptionHandler
 然后重写 handler 方法就可以（具体可参考 DefaultExceptionHandler实现)。 然后再将自定义异常配置到Feign中即可

my_exception_handler = MyExceptionHandler()
@Feign(prefix="/shared/dict/api/dict", serviceId="shared", exceptionHandler=my_exception_handler, name="共享服务-字典服务")
class DictApi2:
 pass
```




#### 交流

<div>
  <span>
  <img src="images/weixin.jpg" width="200" height="200">
  </span>
</div>

#### 打赏

<div>
  <span>
  <img src="images/support.jpg" width="200" height="200">
  </span>
</div>



