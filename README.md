# NotionBillTools



## Description

该项目主要运用于将支付宝和微信所生成账单的csv文件自动上传到Notion笔记之中。但限制于支付宝与微信并未开放接口让用户自动导出账单，因此仍需要用户手动去平台上下载账单，并放入到工程文件之中。



## How to use it

1. 下载好你的账单文件，并把两个文件放入到工程下的bills文件夹内，若没有该文件夹则自行创建一个
2. 更新conf.json文件内的各项配置，共六项
   - secret：可访问你的父页面的Integration的secret key
   - parent_page_id：你希望将数据库放在的页面下的页面id
   - title：新页面的标题
   - path：存放账单文件的文件夹名，默认为bills，你也可以进行自定义
   - wechat：微信账单文件名
   - alipay：支付宝账单文件名
3. 运行run.py



## Q&A

Q：我的secret key在哪里看？

A：请参照[链接](https://developers.notion.com/docs/getting-started)进行Integrations的申请，并确保该Integrations可以访问你想要创建账单的父文件夹

Q：page的id怎么看

A：在notion上右键页面并复制链接，id为https://www.notion.so/ 后以及？前的一串字符串

