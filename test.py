import json

TEST_FILE = f"D:/pycoding/智慧家/train.jsonl"  # 或 "validation.jsonl"

print(f"尝试读取文件：{TEST_FILE}")

try:
    # 尝试使用 UTF-8 编码读取
    with open(TEST_FILE, 'r', encoding='utf-8') as f:
        # 尝试读取第一行
        first_line = f.readline()
        
        # 尝试解析第一行 JSON
        data = json.loads(first_line)
        
        print("✅ 文件读取和 JSON 解析成功！")
        print(f"文件大小（第一行字符数）：{len(first_line)}")
        print(f"解析后的数据键（Keys）：{data.keys()}")

except FileNotFoundError:
    print(f"❌ 错误：未找到文件。请检查文件名是否正确，并在终端中再次确认运行目录。")
except UnicodeDecodeError:
    print("❌ 错误：文件编码错误。尝试使用 'latin-1' 编码重新运行。")
    try:
        with open(TEST_FILE, 'r', encoding='latin-1') as f:
            first_line = f.readline()
            json.loads(first_line)
            print("✅ 编码 'latin-1' 成功。你的文件可能需要切换编码。")
    except Exception as e:
        print(f"❌ 错误：'latin-1' 编码也失败，原始错误：{e}")
except json.JSONDecodeError as e:
    print(f"❌ 错误：JSON 格式解析失败。文件可能损坏或格式不正确。")
    print(f"JSON 错误详情：{e}")
except Exception as e:
    print(f"❌ 发生未知错误：{e}")