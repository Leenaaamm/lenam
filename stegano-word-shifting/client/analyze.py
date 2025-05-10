from docx import Document
from docx.shared import Pt
import sys

def analyze_doc(doc_path):
    # Mở tài liệu
    doc = Document(doc_path)

# Giả sử bạn muốn lấy font size của ký tự đầu tiên trong đoạn đầu tiên
    paragraph = doc.paragraphs[0]  # lấy đoạn đầu tiên

# Lặp qua từng Run (vì mỗi Run có thể có định dạng khác nhau)
    for run in paragraph.runs:
        if run.text:  # kiểm tra run không rỗng
            first_char = run.text[0]
            font_size = run.font.size  # trả về một đối tượng Pt hoặc None nếu không được thiết lập rõ ràng
            if font_size:
                print(f"base_size: {font_size.pt}pt")
            break  # chỉ lấy ký tự đầu tiên thôi

if __name__ == "__main__":
    file_directory = sys.argv[1]
    if file_directory.endswith(".docx") is False:
        print("Lỗi: Đường dẫn không phải là file .docx")
        sys.exit(1)
    analyze_doc(file_directory)