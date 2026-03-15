def caesar_cipher(text, shift, mode='encrypt'):
    """
    凯撒密码核心逻辑
    :param text: 输入字符串
    :param shift: 偏移步长
    :param mode: 'encrypt' 或 'decrypt'
    :return: 处理后的字符串
    """
    result = ""
    # 如果是解密，反向偏移
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # 确定 ASCII 基准 (大写 65, 小写 97)
            base = ord('A') if char.isupper() else ord('a')
            # 计算偏移后的字符
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            # 非字母字符保持不变
            result += char
    return result


def score_text(text):
    """
    评估文本的可读性得分（分数越高越可能是正确解密）
    :param text: 待评估的文本
    :return: 得分
    """
    # 英文常见字母频率（从高到低）
    common_letters = 'etaoinshrdlcumwfgypbvkjxqz'
    
    # 常见英文单词（用于匹配）
    common_words = {'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
                    'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at'}
    
    score = 0
    text_lower = text.lower()
    
    # 1. 字母频率评分
    for i, char in enumerate(common_letters):
        if char in text_lower:
            score += (26 - i) * text_lower.count(char)
    
    # 2. 常见单词匹配评分
    words = text_lower.split()
    for word in words:
        # 去除标点
        clean_word = ''.join(c for c in word if c.isalpha())
        if clean_word in common_words:
            score += 10
    
    # 3. 字母比例评分（字母占比越高越可能是正常文本）
    alpha_count = sum(1 for c in text if c.isalpha())
    if len(text) > 0:
        score += (alpha_count / len(text)) * 20
    
    return score


def brute_force_best(text):
    """
    暴力破解并返回最可能的结果
    :param text: 密文
    :return: (最佳步长，解密结果，得分)
    """
    best_shift = 0
    best_result = ""
    best_score = -1
    
    for i in range(1, 26):
        decoded = caesar_cipher(text, i, 'decrypt')
        score = score_text(decoded)
        
        if score > best_score:
            best_score = score
            best_shift = i
            best_result = decoded
    
    return best_shift, best_result, best_score


def main():
    print("=" * 40)
    print("欢迎使用 syy 凯撒密码工具")
    print("=" * 40)
    
    while True:
        print("\n请选择功能：")
        print("1. 加密 (Encrypt)")
        print("2. 解密 (Decrypt)")
        print("3. 智能暴力破解 (Smart Brute Force)")
        print("4. 显示所有破解结果 (Show All)")
        print("0. 退出 (Exit)")
        
        choice = input("请输入选项 (0-4): ").strip()
        
        if choice == '0':
            print("感谢使用，再见！")
            break
        
        elif choice == '1':
            text = input("请输入明文：")
            try:
                shift = int(input("请输入偏移步长 (整数): "))
                cipher_text = caesar_cipher(text, shift, 'encrypt')
                print(f"\n[加密结果]: {cipher_text}")
                print(f"[使用步长]: {shift}")
            except ValueError:
                print("错误：步长必须是整数！")
        
        elif choice == '2':
            text = input("请输入密文：")
            try:
                shift = int(input("请输入偏移步长 (整数): "))
                plain_text = caesar_cipher(text, shift, 'decrypt')
                print(f"\n[解密结果]: {plain_text}")
                print(f"[加密步长]: {shift}")
            except ValueError:
                print("错误：步长必须是整数！")
        
        elif choice == '3':
            text = input("请输入密文以智能破解：")
            print("\n[智能破解结果]:")
            print("-" * 40)
            shift, result, score = brute_force_best(text)
            print(f"最可能步长：{shift}")
            print(f"可信度得分：{score:.2f}")
            print(f"解密结果：{result}")
            print("-" * 40)
            print("提示：如结果不准确，可尝试选项 4 查看所有可能。")
        
        elif choice == '4':
            text = input("请输入密文以推导步长：")
            print("\n[暴力破解结果]:")
            print("-" * 30)
            for i in range(1, 26):
                decoded = caesar_cipher(text, i, 'decrypt')
                print(f"步长 {i:2d}: {decoded}")
            print("-" * 30)
        
        else:
            print("无效选项，请重新输入。")


if __name__ == "__main__":
    main()