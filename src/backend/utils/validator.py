# Library
import re

def clean_and_validate_text(text):
    if text is None:
        return None, "Chuỗi đầu vào không được để trống."

    text = str(text).strip()

    if not text:
        return None, "Văn bản đầu vào rỗng."

    if len(text) > 2000:
        return None, "Văn bản vượt quá 2000 ký tự."

    if not re.search(r"[a-zA-Zà-ỹÀ-Ỹ0-9]", text):
        return None, "Văn bản không hợp lệ."

    return text, None