import pandas as pd

def merge_columns():
    try:
        # 读取Excel文件
        # 注意：用户需要将Excel文件放在同一目录下，并命名为'input.xlsx'
        df = pd.read_excel('input.xlsx')
        
        # 获取所需列数据，按照指定顺序
        columns = ['【请提供】', '用例名称']
        
        # 初始化结果数据框
        result_data = ['' for _ in range(len(df))]
        
        # 按行处理数据
        for i in range(len(df)):
            row_data = []
            for col in columns:
                if pd.notna(df[col][i]):
                    row_data.append(str(df[col][i]))
            result_data[i] = ''.join(row_data) if row_data else ''
        
        # 创建新的DataFrame，只有一列
        new_df = pd.DataFrame(result_data, columns=['合并数据'])
        

        # 保存到新的Excel文件
        new_df.to_excel('outputab.xlsx', index=False)
        print('合并完成！新文件已保存为 output.xlsx')
        
    except FileNotFoundError:
        print('错误：找不到输入文件 input.xlsx')
    except Exception as e:
        print(f'发生错误：{str(e)}')

if __name__ == '__main__':
    merge_columns()