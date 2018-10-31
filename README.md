
<!-- TOC -->

- [1. disease_dashboard](#1-disease_dashboard)
    - [1.1. django_web](#11-django_web)
        - [1.1.1. django_web](#111-django_web)
        - [1.1.2. dis_dashboard](#112-dis_dashboard)
        - [1.1.3. home](#113-home)
        - [1.1.4. static](#114-static)
        - [1.1.5. templates](#115-templates)
        - [1.1.6. data_normal](#116-data_normal)
- [gen_dem_data](#gen_dem_data)
    - [ReportZoneMonth16_01.csv](#reportzonemonth16_01csv)
    - [gen_test_data.R](#gen_test_datar)
    - [demo_hiv_aids_05_15.csv](#demo_hiv_aids_05_15csv)

<!-- /TOC -->

共享杯仪表盘艾迪宝系统简介
这是一个传染病药品仪表板系统，使用的技术栈为django,postgre,D3，ledflet
部署网址为：  
源码保存在海宇技术组的github上，目前由技术组负责维护和更新
# 1. disease_dashboard
disease_dashboard为整个文件目录
## 1.1. django_web
为一个标准的django网页目录，通过mvc的方式控制网站
### 1.1.1. django_web
django的总控制目录，setting.py，里面进行总体设置
### 1.1.2. dis_dashboard
仪表盘页面的app，可视化数据
### 1.1.3. home
主页和控制页面app，负责注册、登陆和首页等内容
### 1.1.4. static
静态文件，主要存储图片js与css，内部文件树与app的命名空间一致
### 1.1.5. templates
模板文件，存储html模板，内部文件树与app的命名空间一致
### 1.1.6. data_normal
储存网站需要用的一些普通数据，如省列表，病名列表
# gen_dem_data
因为涉及数据保密和格式问题，这里使用了一个demo数据生成器，一个生成demo数据的工具，用r语言写成
## ReportZoneMonth16_01.csv
一个原始数据，取自网站2016年1月的艾滋病与hiv的发病数据，为0的部分替换为1，避免null的错误  
另外根据发病率和发病人数计算了一个all_pop字段，为各省与全国的人口数量，为了R脚本中的计算
## gen_test_data.R
一个r语言的脚本，根据取自网站2016年1月的原始数据，根据这个月数据的方差与每个省的取值，随机生成其他月份的数据
## demo_hiv_aids_05_15.csv
最后生成的数据demo，有2005年-2015年各个月的艾滋病与hiv的发病数据，涉及的字段为

| 变量名 | 标签 | 备注 |
| :------| ------: | :------: |
| area_name | 区域名字 | 采用了原始的数据的命名方式，全国为”全    国“ |
| year | 年份2005-2015 | —— |
| month | 月份1-12 | 个位的月份前面没有0 |
| dis_name | disease_name疾病名字 | 此项目中使用艾滋病与HIV |
| case_num | case_number发病人数 | —— |
| death_num | death_number死亡人数 | —— |
| ici_rate | incidence_rate发病率 | —— |
| mort_rate | mortality_rate死亡率 | —— |