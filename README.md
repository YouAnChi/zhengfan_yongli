# 正反用例处理工具集

这是一个用于处理和转换测试用例的Python工具集，包含多个功能模块用于不同的用例处理场景。

## 项目结构

```
├── ds_r1.py          # DeepSeek API调用模块
├── hebing.py         # 双列合并工具
├── hebing2.py        # 四列合并工具
├── input.xlsx        # 输入文件
├── sysprompt.md      # 系统提示词配置
└── myenv/            # Python虚拟环境
```

## 功能模块

### 1. DeepSeek API调用模块 (ds_r1.py)

这个模块用于通过DeepSeek API处理测试用例，主要功能包括：

- 读取系统提示词配置
- 批量处理Excel中的测试用例
- 通过DeepSeek API进行推理
- 将处理结果保存为新的Excel文件

### 2. 双列合并工具 (hebing.py)

用于合并Excel文件中的两列数据：

- 合并"【请提供】"和"用例名称"列
- 保留非空数据
- 输出到新的Excel文件

### 3. 四列合并工具 (hebing2.py)

用于合并Excel文件中的四列数据：

- 合并"用例名称"、"预置条件"、"测试步骤"和"预期结果"列
- 使用换行符分隔各列内容
- 输出到新的Excel文件

## 安装说明

1. 克隆项目到本地

2. 创建并激活虚拟环境：
```bash
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate    # Windows
```

3. 安装依赖：
```bash
pip install openai pandas openpyxl
```

## 使用说明

### DeepSeek API处理

1. 准备input.xlsx文件，确保包含需要处理的数据
2. 配置sysprompt.md中的系统提示词
3. 在ds_r1.py中配置您的API密钥
4. 运行程序：
```bash
python ds_r1.py
```

### 双列合并

1. 准备input.xlsx文件，确保包含"【请提供】"和"用例名称"列
2. 运行程序：
```bash
python hebing.py
```

### 四列合并

1. 准备input.xlsx文件，确保包含所需的四列数据
2. 运行程序：
```bash
python hebing2.py
```

## 输出文件

- DeepSeek API处理：输出文件名格式为 `output_YYYYMMDD_HHMMSS.xlsx`
- 双列合并：输出文件名为 `outputab.xlsx`
- 四列合并：输出文件名为 `output_abcd.xlsx`

## 注意事项

1. 确保input.xlsx文件位于程序同一目录下
2. 运行程序前请确认已正确配置虚拟环境和依赖
3. 使用DeepSeek API时需要有效的API密钥
4. 处理大量数据时请注意API调用限制

## 依赖项

- Python 3.9+
- openai
- pandas
- openpyxl

## 错误处理

所有模块都包含基本的错误处理机制：

- 文件不存在的处理
- API调用异常处理
- 数据处理异常的捕获和提示