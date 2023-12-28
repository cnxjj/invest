##### 汇总投资标的收盘数据

###### 需求
1、每周五收盘后，抓取投资标地的收盘价；<br />
2、汇总基金单位净值、股票收盘价到一个汇总表内；<br />
3、添加沪深300指数、易方达沪深300指数基金收盘价作为参考；<br />
4、最终将数据放入投资收益表格内计算出当周的投资收益。

###### 抓取数据
1-1 - 使用efinance获取基金和股票数据，存入日期文件；<br />
1-2 - 通过证券宝www.baostock.com获取沪深300指数数据。<br />

###### 加工处理
2-1 - 添加汇总工作表，并生成周五日期列表；<br />
2-2 - 创建周五的日期列；<br />
2-3 - 根据周五日期列表汇总收盘数据；<br />
2-4 - 修改汇总数据表格式。
