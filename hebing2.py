import pandas as pd

def merge_columns():
    try:
        # 读取Excel文件
        # 注意：用户需要将Excel文件放在同一目录下，并命名为'input.xlsx'
        df = pd.read_excel('input.xlsx')
        
        # 获取所需列数据
        columns = ['用例名称', '预置条件', '测试步骤', '预期结果']
        
        # 创建新的DataFrame，只保留原始数据
        new_df = pd.DataFrame()
        
        # 处理每一列数据
        for i in range(len(df)):
            row_data = []
            for col in columns:
                if col in df.columns and pd.notna(df[col][i]):
                    row_data.append(str(df[col][i]))
            # 将该行的所有数据合并后添加到新DataFrame的A列
            new_df.loc[i, '合并数据'] = '\n'.join(row_data) if row_data else ''
        
        # 创建新的DataFrame，只有一列
        new_df = pd.DataFrame(new_df, columns=['合并数据'])
        
        # 保存到新的Excel文件
        new_df.to_excel('output_abcd.xlsx', index=False)
        print('合并完成！新文件已保存为 output——abcd.xlsx')
        
    except FileNotFoundError:
        print('错误：找不到输入文件 input.xlsx')
    except Exception as e:
        print(f'发生错误：{str(e)}')

if __name__ == '__main__':
    merge_columns()