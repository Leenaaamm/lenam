from docx import Document
from docx.shared import Pt
import sys

def extract_binary_string(doc_path, base_size):
    document = Document(doc_path)
    res = ""
    for paragraph in document.paragraphs:
        index = 0
        for run in paragraph.runs:
            if run.text:  # kiểm tra run không rỗng
                for char in run.text:
                    if char == " " and run.font.size is not None:
                        if run.font.size.pt < float(base_size):
                            res += "0"
                        else:
                            res += "1"
    with open("binary_result.txt", "w") as f:
        f.write(res)
    print("Đã xuất chuỗi nhị phân vào file 'binary_result.txt'")
if __name__ == "__main__":
    file_directory = sys.argv[1]
    base_size = sys.argv[2]
    if file_directory.endswith(".docx") is False:
        print("Lỗi: Đường dẫn không phải là file .docx")
        sys.exit(1)

    extract_binary_string(file_directory,base_size)
