import os
import json
import base64
import pandas as pd
from pathlib import Path
from PIL import Image
import io

def parquet_to_json_with_images(parquet_path, output_dir="output"):
    """
    将 Parquet 文件还原为 JSON + 原始图片
    
    参数:
        parquet_path (str): Parquet 文件路径
        output_dir (str): 输出目录（默认 "output"）
    """
    # 创建输出目录
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    # 读取 Parquet 文件
    print(f"正在读取 {parquet_path}...")
    df = pd.read_parquet(parquet_path)
    
    # 准备存储所有记录的列表
    records = []
    
    # 处理每一行数据
    for idx, row in df.iterrows():
        # 处理图像数据
        try:
            img_data = row["image"]
            # 处理不同的图像数据格式
            if isinstance(img_data, dict) and "bytes" in img_data:
                img_bytes = img_data["bytes"]
            elif isinstance(img_data, bytes):
                img_bytes = img_data
            else:
                print(f"行 {idx}: 无法识别的图像格式: {type(img_data)}")
                continue
                
            # 保存原始图片文件
            img = Image.open(io.BytesIO(img_bytes))
            img_format = img.format.lower() if img.format else "jpg"
            img_filename = f"image_{idx}.{img_format}"
            img_path = os.path.join(images_dir, img_filename)
            img.save(img_path)
            
            # 转换为Base64（可选，JSON中存储）
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
            
            # 构建记录，使用绝对路径
            record = {
                "id": idx,
                "image_path": os.path.abspath(img_path),  # 使用绝对路径
                "image_base64": img_base64,                 # Base64编码（可选）
                "problem": row.get("problem", ""),
                "solution": row.get("solution", ""),
                "original_question": row.get("original_question", ""),
                "original_answer": row.get("original_answer", "")
            }
            records.append(record)
            
        except Exception as e:
            print(f"行 {idx}: 处理失败 - {str(e)}")
            continue
    
    # 保存为JSON
    output_json = os.path.join(output_dir, "data.json")
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    
    print(f"处理完成！结果保存在 {output_dir}")
    print(f"共处理 {len(df)} 条记录，成功 {len(records)} 条")
    print(f"JSON 文件: {output_json}")
    print(f"图片目录: {images_dir}")

if __name__ == "__main__":
    # 使用示例
    parquet_file = "train-00000-of-00001.parquet"  # 替换为实际路径
    parquet_to_json_with_images(parquet_file)
