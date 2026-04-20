import pandas as pd
import json
import re
import os
from typing import List, Dict, Any

# --- 配置参数 (请确保绝对路径正确) ---
# 请使用你当前正在使用的绝对路径
LOCAL_TRAIN_FILE = "D:/pycoding/智慧家/train.jsonl" 
LOCAL_VALID_FILE = "D:/pycoding/智慧家/validation.jsonl"
OUTPUT_FILENAME = "luojia_openmath_local_corpus_final.json"

# 🎯 核心修正：超全面关键词列表
TARGET_KEYWORDS = [
    # 微积分 (Calculus)
    'integral', 'integration', 'derivative', 'differentiation', 'limit', 'limits', 
    'series', 'Taylor series', 'partial derivative', 'multiple integral', 'multivariable',
    'gradient', 'curl', 'divergence', 'chain rule', "L'Hôpital", 
    # 线性代数 (Linear Algebra)
    'eigenvalue', 'matrix', 'vector', 'determinant', '方程组', 'rank', 'basis', 
    'eigenspace', 'invertible', 'transpose', 'null space', 'column space', 
    'linear transformation', 'orthonormal', 'singular value',
    # 概率论与数理统计 (Probability & Statistics)
    'probability', 'random variable', 'distribution', 'variance', 'mean', 
    'hypothesis test', 'confidence interval', 'regression', 'Poisson', 'Binomial', 
    'Normal distribution', 'CDF', 'PDF', 'p-value', 'sample', 'statistic',
    # 常微分方程 (ODE)
    'differential equation', 'ODE', 'Laplace transform', 'solution curve', 
    'initial condition', 'first order', 'second order', 'homogeneous', 
    'nonhomogeneous', 'separation of variables',
    # 离散数学/组合数学 (Discrete/Combinatorics)
   # 'combinatorics', 'graph theory', 'permutation', 'combination', 'set theory', 
    #'induction', 'pigeonhole', 'recurrence relation', 'modulo', 'binary'
]

# 强制最大提取数量（可以根据你的机器性能和对数据量的需求进行调整）
MAX_RECORDS = 50000 

# ====================================================================
# 清洗与筛选函数
# ====================================================================

def clean_text_and_code(text: str) -> str:
    """对文本进行清洗，并保留其中的代码块标签。"""
    if not text: return ""
    text = str(text) 
    text = re.sub(r'\n+', ' ', text).strip()
    
    # 保持代码块标签原样
    text = re.sub(r'\s*<llm-code>\s*', ' <llm-code> ', text)
    text = re.sub(r'\s*</llm-code>\s*', ' </llm-code> ', text)
    text = re.sub(r'\s*<llm-code-output>\s*', ' <llm-code-output> ', text)
    text = re.sub(r'\s*</llm-code-output>\s*', ' </llm-code-output> ', text)
    
    # 移除答案中的 \boxed{} 标记
    text = text.replace("\\boxed", "")
    return text

def check_keywords(text: str) -> bool:
    """检查问题中是否包含目标关键词"""
    if not text: return False
    text_lower = str(text).lower()
    return any(kw in text_lower for kw in TARGET_KEYWORDS)

# ====================================================================
# 核心处理函数：使用 Pandas 优化
# ====================================================================

def process_with_pandas_optimization(file_paths: List[str]) -> List[Dict[str, Any]]:
    final_corpus = []
    
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"FATAL ERROR: 文件 {file_path} 未找到。请检查绝对路径是否正确。")
            continue
            
        print(f"--- 1. 正在使用 Pandas 读取文件: {file_path} ---")
        
        try:
            # 使用 Pandas 的 read_json 快速读取 JSONL 文件
            df = pd.read_json(file_path, lines=True)
            print(f" - 文件 {file_path} 成功加载 {len(df)} 条记录。")
            
        except Exception as e:
            print(f"FATAL ERROR: Pandas 读取文件 {file_path} 失败，可能是 JSON 格式问题。\n错误信息: {e}")
            continue

        print("--- 2. 正在进行筛选和清洗 ---")

        REQUIRED_COLS = ['question', 'generated_solution']
        if not all(col in df.columns for col in REQUIRED_COLS):
            print(f"警告：文件 {file_path} 缺少必要的列 {REQUIRED_COLS}，已跳过。")
            continue
        
        # 1. 筛选：问题包含目标关键词 
        df_filtered_keywords = df[
            df['question'].apply(lambda x: check_keywords(str(x)))
        ].copy()
        
        # 2. 筛选：答案包含代码块 (<llm-code>)
        df_filtered_code = df_filtered_keywords[
            df_filtered_keywords['generated_solution'].str.contains('<llm-code>', na=False, case=False)
        ].copy()
        
        print(f" - 关键词筛选后剩余: {len(df_filtered_keywords)} 条")
        print(f" - 最终代码/关键词筛选后剩余: {len(df_filtered_code)} 条")
        
        # 3. 强制限制记录数
        df_final = df_filtered_code.head(MAX_RECORDS - len(final_corpus))
        
        # 4. 应用清洗逻辑并格式化
        for index, row in df_final.iterrows():
            clean_question = clean_text_and_code(row['question'])
            clean_solution = clean_text_and_code(row['generated_solution'])
            
            corpus_entry = {
                "id": f"OM_CODE_{os.path.basename(file_path).split('.')[0]}_{index}",
                # 记录命中哪些关键词
                "tag_keywords": [kw for kw in TARGET_KEYWORDS if kw in str(row['question']).lower()],
                "question": clean_question,
                "solution_with_code": clean_solution, 
                "meta_info": f"Source: OpenMathInstruct-1 - {os.path.basename(file_path)}"
            }
            final_corpus.append(corpus_entry)
            
            if len(final_corpus) >= MAX_RECORDS:
                print(f"已达到设定的最大记录数 {MAX_RECORDS}，停止处理。")
                break
                
    return final_corpus

def save_to_json(data: List[Dict[str, Any]]):
    """将数据保存为最终的 JSON 文件"""
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"--- 3. 成功！最终语料库 ({len(data)} 条记录) 已保存到 {OUTPUT_FILENAME} ---")


if __name__ == "__main__":
    
    all_files = [LOCAL_TRAIN_FILE, LOCAL_VALID_FILE]
    
    corpus = process_with_pandas_optimization(all_files)
    
    if corpus:
        save_to_json(corpus)