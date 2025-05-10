import sys

def string_to_binary_8bit(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_string_8bit(binary_str):
    # Chia chuỗi nhị phân thành từng nhóm 8 bit, rồi chuyển từng nhóm thành ký tự
    chars = [chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)]
    return ''.join(chars)

def read_file_and_convert_to_binary(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        binary_output = string_to_binary_8bit(content)
        with open("binary.txt", "w", encoding='utf-8') as binary_file:
            binary_file.write(binary_output)
        print("Đã xuất chuỗi nhị phân vào file 'binary.txt'")
    except FileNotFoundError:
        return "File không tồn tại."
    except Exception as e:
        return f"Lỗi xảy ra: {e}"

def convert_binary_file_to_text(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            binary_content = infile.read().strip()
        
        original_text = binary_to_string_8bit(binary_content)
        
        with open("extract-message.txt", 'w', encoding='utf-8') as outfile:
            outfile.write(original_text)
        
        print(f"Đã ghi chuỗi gốc vào file: 'convert-message.txt'")
    
    except FileNotFoundError:
        print("File đầu vào không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    file_path = sys.argv[1]  # Đường dẫn file được truyền từ dòng lệnh
    option = sys.argv[2]  # Lựa chọn giữa 'convert' và 'extract'
    if option == 'encode':
        read_file_and_convert_to_binary(file_path)
    elif option == 'decode':
        convert_binary_file_to_text(file_path)
    else:
        print("Lựa chọn không hợp lệ. Vui lòng sử dụng 'encode' hoặc 'decode'.")
        sys.exit(1)
