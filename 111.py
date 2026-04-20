import json
import os

INPUT_FILE = "luojia_openmath_local_corpus_final_v5.json"
OUTPUT_FILE = "luojia_openmath_platform_safe_ascii.json"

def convert_to_ascii(input_file, output_file):
    print(f"--- 1. 正在加载文件：{input_file} ---")
    try:
        # 使用 UTF-8 编码读取你之前生成的文件
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"FATAL ERROR: 加载文件失败。请检查文件名是否正确或文件是否损坏。\n错误信息: {e}")
        return

    print(f"--- 2. 正在转换为平台兼容性最高的 ASCII 编码文件：{output_file} ---")

    # 核心转换：
    # 1. ensure_ascii=True: 强制将所有非 ASCII 字符（如中文）转义
    # 2. encoding='ascii': 使用 ASCII 编码写入，保证文件中不含任何中文或特殊字符
    with open(output_file, 'w', encoding='ascii') as f:
        json.dump(data, f, ensure_ascii=True, indent=2)
    
    print(f"--- 3. 成功！文件已转换为纯 ASCII 编码并保存至 {output_file} ---")
    print("请尝试上传这个新的文件。")

if __name__ == "__main__":
    convert_to_ascii(INPUT_FILE, OUTPUT_FILE)