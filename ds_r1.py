from openai import OpenAI
import os
import pandas as pd
from datetime import datetime

client = OpenAI(
    api_key = "sk-0ea9167338bc4daf945bf8a769ade25f",
    base_url="https://api.deepseek.com/v1"
)

# 读取系统提示词文件
sys_prompt_path = os.path.join(os.path.dirname(__file__), 'sysprompt.md')
with open(sys_prompt_path, 'r', encoding='utf-8') as f:
    system_content = f.read()

# 读取输入Excel文件
input_df = pd.read_excel('input.xlsx')
#input_df = pd.read_excel('input.xlsx', skiprows=1)

# 创建结果列表
results = []

# 处理每一行数据
for index, row in input_df.iterrows():
    user_content = str(row[0])  # 获取A列的内容
    reasoning_content = ""  # 定义完整思考过程
    answer_content = ""     # 定义完整回复
    is_answering = False   # 判断是否结束思考过程并开始回复

    # 创建聊天完成请求
    completion = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ],
        stream=True
    )

    print("\n处理第{}行数据...".format(index + 1))
    print("=" * 20 + "思考过程" + "=" * 20)

    for chunk in completion:
        if not chunk.choices:
            continue
        
        delta = chunk.choices[0].delta
        # 处理思考过程
        if hasattr(delta, 'reasoning_content') and delta.reasoning_content != None:
            print(delta.reasoning_content, end='', flush=True)
            reasoning_content += delta.reasoning_content
        else:
            # 处理回复内容
            if delta.content != "" and is_answering == False:
                print("\n" + "=" * 20 + "完整回复" + "=" * 20)
                is_answering = True
            print(delta.content, end='', flush=True)
            answer_content += delta.content
    
    # 将结果添加到列表中
    results.append({
        'prompt': user_content,
        'reasoning': reasoning_content,
        'answer': answer_content
    })
    print("\n")

# 创建结果DataFrame并保存到Excel
output_df = pd.DataFrame(results)
output_df.columns = ['原始提示词', '思考过程', '完整回复']
output_filename = 'output_{}.xlsx'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))
output_df.to_excel(output_filename, index=False)
print("\n结果已保存到: {}".format(output_filename))