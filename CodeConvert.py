import os
import glob

def replace_bytes_in_file(filepath):
    # 要查找的目标字节序列
    target1 = bytes([0x99, 0x20, 0xa9])
    target2 = bytes([0xe2, 0x84, 0xa2, 0x20, 0xc2, 0xa9])
    # 替换为的字节序列
    replacement = bytes([0x20, 0x20, 0x20])
    
    try:
        # 以二进制模式读取文件
        with open(filepath, 'rb') as f:
            content = f.read()
        
        # 替换所有出现的目标序列
        modified_content = content.replace(target1, replacement)
        
        # 如果内容有变化，则写回文件
        if modified_content != content:
            with open(filepath, 'wb') as f:
                f.write(modified_content)
            print(f"已修改文件: {filepath}")
        else:
            modified_content = content.replace(target2, replacement)
            if modified_content != content:
                with open(filepath, 'wb') as f:
                    f.write(modified_content)
                print(f"已修改文件: {filepath}")
            else:
                print(f"未发现需要替换的内容: {filepath}")
    except Exception as e:
        print(f"处理文件 {filepath} 时出错: {e}")

def find_source_files():
    # 支持的扩展名
    extensions = ['*.c', '*.cpp', '*.h']
    files = []
    
    # 递归查找所有匹配的文件
    for ext in extensions:
        # 使用**表示递归搜索子目录
        files.extend(glob.glob(f'**/{ext}', recursive=True))
    
    return files

def main():
    print("开始处理文件...")
    
    # 获取所有需要处理的文件
    files = find_source_files()
    
    if not files:
        print("未找到任何.c、.cpp或.h文件")
        return
    
    print(f"找到 {len(files)} 个文件需要处理")
    
    # 处理每个文件
    for file in files:
        if os.path.isfile(file):
            replace_bytes_in_file(file)
        else:
            print(f"跳过非文件项: {file}")

    print("处理完成。")

if __name__ == "__main__":
    main()