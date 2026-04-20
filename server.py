from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    """从本地 data.json 获取数据并返回 JSON"""
    try:
        # 确保文件在当前目录
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'luojia_openmath_local_corpus_final_v5.json')
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    
    except FileNotFoundError:
        return jsonify({"error": "data.json not found. Place it in the same folder as this script!"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data.json"}), 400

if __name__ == '__main__':
    # 重要：host='0.0.0.0' 允许局域网访问（手机/平板也能用）
    app.run(host='0.0.0.0', port=5000, debug=True)