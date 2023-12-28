# https://zhuanlan.zhihu.com/p/358782751
# 获取基金历史净值
# 获取 161725 和 005827 这两个基金的历史净值信息，并将之存储到以基金代码命名的 csv 文件中

import pandas as pd
import requests


def get_fund_k_history(fund_code: str, pz: int = 40000) -> pd.DataFrame:
    '''
    根据基金代码和要获取的页码抓取基金净值信息

    Parameters
    ----------
    fund_code : 6位基金代码
    page : 页码 1 为最新页数据

    Return
    ------
    DataFrame : 包含基金历史k线数据
    '''
    # 请求头
    EastmoneyFundHeaders = {
        'User-Agent': 'EMProjJijin/6.2.8 (iPhone; iOS 13.6; Scale/2.00)',
        'GTOKEN': '98B423068C1F4DEF9842F82ADF08C5db',
        'clientInfo': 'ttjj-iPhone10,1-iOS-iOS13.6',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'fundmobapi.eastmoney.com',
        'Referer': 'https://mpservice.com/516939c37bdb4ba2b1138c50cf69a2e1/release/pages/FundHistoryNetWorth',
    }
    # 请求参数
    data = {
        'FCODE': f'{fund_code}',
        'appType': 'ttjj',
        'cToken': '1',
        'deviceid': '1',
        'pageIndex': '1',
        'pageSize': f'{pz}',
        'plat': 'Iphone',
        'product': 'EFund',
        'serverVersion': '6.2.8',
        'version': '6.2.8'
    }
    url = 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNHisNetList'
    json_response = requests.get(
        url, headers=EastmoneyFundHeaders, data=data).json()
    rows = []
    columns = ['日期', '单位净值', '累计净值', '涨跌幅']
    if json_response is None:
        return pd.DataFrame(rows, columns=columns)
    datas = json_response['Datas']
    if len(datas) == 0:
        return pd.DataFrame(rows, columns=columns)
    rows = []
    for stock in datas:
        date = stock['FSRQ']
        rows.append({
            '日期': date,
            '单位净值': stock['DWJZ'],
            '累计净值': stock['LJJZ'],
            '涨跌幅': stock['JZZZL']
        })

    df = pd.DataFrame(rows)
    df['单位净值'] = pd.to_numeric(df['单位净值'], errors='coerce')

    df['累计净值'] = pd.to_numeric(df['累计净值'], errors='coerce')

    df['日期'] = pd.to_datetime(df['日期'], errors='coerce')
    return df


# 多个 6 位基金代码构成的列表
fund_codes = ['162412','110031','006327','000961','012348','501029','003318']
fund_names = ['华宝中证医疗', '易方达恒生国企','易方达中概互联','天弘沪深300','天弘恒生科技','华宝红利基金','景顺中证500低波动']
fund_count = 0


# 遍历基金代码列表获取数据
for fund_code in fund_codes:
    # 调用函数获取基金历史净值数据
    fund_data = get_fund_k_history(fund_code)
    # 将数据存储到表格文件中
    fund_data.to_csv(f'20_Invest/fund/0{fund_count+1} - {fund_code} - {fund_names[fund_count]}.csv', index=None, encoding='utf-8-sig')
    print(f'基金 {fund_code} - {fund_names[fund_count]} 的历史净值数据已存储到文件中！')
    fund_count = fund_count+1
print('全部获取完毕！')