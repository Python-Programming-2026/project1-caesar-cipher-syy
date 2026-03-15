def caesar_cipher(text, shift, mode='encrypt'):
    """
    凯撒密码核心逻辑
    :param text: 输入字符串
    :param shift: 偏移步长
    :param mode: 'encrypt' 或 'decrypt'
    :return: 处理后的字符串
    """
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result


def score_text(text):
    """
    评估文本的可读性得分（分数越高越可能是正确解密）
    """
    common_letters = 'etaoinshrdlcumwfgypbvkjxqz'
    
    common_words = {'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
                    'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
                    'hello', 'world', 'is', 'are', 'was', 'were', 'this', 'from',
                    'has', 'had', 'will', 'would', 'could', 'should', 'my', 'your',
                    'his', 'her', 'our', 'their', 'what', 'which', 'who', 'when',
                    'where', 'why', 'how', 'all', 'each', 'every', 'both', 'few',
                    'more', 'most', 'other', 'some', 'such', 'no', 'yes', 'if',
                    'then', 'else', 'so', 'but', 'or', 'an', 'been', 'being',
                    'am', 'can', 'may', 'must', 'shall', 'about', 'after', 'before',
                    'just', 'know', 'take', 'come', 'see', 'want', 'look', 'use',
                    'find', 'give', 'tell', 'work', 'call', 'try', 'ask', 'need',
                    'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let', 'begin',
                    'seem', 'help', 'talk', 'turn', 'start', 'show', 'hear', 'play',
                    'run', 'move', 'like', 'live', 'believe', 'hold', 'bring', 'happen',
                    'write', 'provide', 'sit', 'stand', 'lose', 'pay', 'meet', 'include',
                    'continue', 'set', 'learn', 'change', 'lead', 'understand', 'watch',
                    'follow', 'stop', 'create', 'speak', 'read', 'allow', 'add', 'spend',
                    'grow', 'open', 'walk', 'win', 'offer', 'remember', 'love', 'consider',
                    'appear', 'buy', 'wait', 'serve', 'die', 'send', 'expect', 'build',
                    'stay', 'fall', 'cut', 'reach', 'kill', 'remain', 'suggest', 'raise',
                    'pass', 'sell', 'require', 'report', 'decide', 'pull', 'people',
                    'history', 'way', 'art', 'world', 'information', 'map', 'family',
                    'government', 'health', 'system', 'computer', 'meat', 'year', 'thanks',
                    'music', 'person', 'reading', 'method', 'data', 'food', 'understanding',
                    'theory', 'law', 'bird', 'literature', 'problem', 'software', 'control',
                    'knowledge', 'power', 'ability', 'economics', 'love', 'internet',
                    'television', 'science', 'library', 'nature', 'fact', 'product',
                    'idea', 'temperature', 'investment', 'area', 'society', 'activity',
                    'story', 'industry', 'media', 'thing', 'oven', 'community', 'definition',
                    'safety', 'quality', 'development', 'language', 'management', 'player',
                    'variety', 'video', 'week', 'security', 'country', 'exam', 'movie',
                    'organization', 'equipment', 'physics', 'analysis', 'policy', 'series',
                    'thought', 'basis', 'boyfriend', 'direction', 'strategy', 'technology',
                    'army', 'camera', 'freedom', 'paper', 'environment', 'child', 'instance',
                    'month', 'truth', 'marketing', 'university', 'writing', 'article',
                    'department', 'difference', 'goal', 'news', 'audience', 'fishing',
                    'growth', 'income', 'marriage', 'user', 'combination', 'failure',
                    'meaning', 'medicine', 'philosophy', 'teacher', 'communication',
                    'night', 'chemistry', 'disease', 'disk', 'energy', 'nation', 'road',
                    'role', 'soup', 'advertising', 'location', 'success', 'addition',
                    'apartment', 'education', 'math', 'moment', 'painting', 'politics',
                    'attention', 'decision', 'event', 'property', 'shopping', 'student',
                    'wood', 'competition', 'distribution', 'entertainment', 'office',
                    'population', 'president', 'unit', 'category', 'cigarette', 'context',
                    'introduction', 'opportunity', 'performance', 'driver', 'flight',
                    'length', 'magazine', 'newspaper', 'relationship', 'teaching', 'cell',
                    'dealer', 'debate', 'finding', 'lake', 'member', 'message', 'phone',
                    'scene', 'appearance', 'association', 'concept', 'customer', 'death',
                    'discussion', 'housing', 'inflation', 'insurance', 'mood', 'woman',
                    'agreement', 'brain', 'career', 'clothing', 'company', 'conclusion',
                    'condition', 'conference', 'congress', 'consideration', 'credit',
                    'earth', 'girl', 'hall', 'historian', 'hospital', 'injury', 'instruction',
                    'maintenance', 'manufacturer', 'meal', 'perception', 'pie', 'poem',
                    'presence', 'proposal', 'reception', 'replacement', 'revolution',
                    'river', 'son', 'speech', 'tea', 'village', 'warning', 'winner',
                    'worker', 'writer', 'assistance', 'breath', 'buyer', 'chest', 'chocolate',
                    'conclusion', 'contribution', 'cookie', 'courage', 'dad', 'desk',
                    'drawer', 'establishment', 'examination', 'garbage', 'grocery', 'honey',
                    'impression', 'improvement', 'independence', 'insect', 'inspection',
                    'inspector', 'king', 'ladder', 'menu', 'penalty', 'piano', 'potato',
                    'profession', 'professor', 'quantity', 'reaction', 'request', 'salary',
                    'shame', 'shelter', 'shoe', 'silver', 'tapping', 'tissue', 'tonight',
                    'tourist', 'toy', 'trade', 'transportation', 'tunnel', 'weekend',
                    'welcome', 'yard'}
    
    common_bigrams = {'th', 'he', 'in', 'er', 'an', 're', 'on', 'at', 'en', 'nd',
                      'ti', 'es', 'or', 'te', 'of', 'ed', 'is', 'it', 'al', 'ar',
                      'st', 'nt', 'ng', 'se', 'ha', 'as', 'ou', 'io', 'le', 'co',
                      'me', 'de', 'hi', 've', 'ta', 'ec', 'si', 'll', 'so', 'na',
                      'li', 'la', 'el', 'ma', 'di', 'ye', 'fo', 'ld', 'um', 'ri',
                      'ra', 'ru', 'ic', 'ne', 'ea', 'ro', 'ly', 'be', 'pe', 'pr',
                      'ou', 'ow', 'un', 'ch', 'sh', 'wh', 'ph', 'gh', 'ck'}
    
    common_trigrams = {'the', 'and', 'tha', 'ent', 'ing', 'ion', 'tio', 'for', 'nde',
                       'has', 'nce', 'edt', 'tis', 'oft', 'sth', 'men', 'whi', 'hel',
                       'wor', 'ld ', 'ell', 'llo', 'rld', 'yo ', 'ou ', 'are', 'was',
                       'wer', 'her', 'his', 'tha', 'thi', 'tho', 'you', 'wit', 'ith'}
    
    score = 0
    text_lower = text.lower()
    words = text_lower.split()
    
    # 1. 完整单词匹配（权重最高）
    for word in words:
        clean_word = ''.join(c for c in word if c.isalpha())
        if clean_word in common_words:
            if len(clean_word) >= 5:
                score += 50
            elif len(clean_word) >= 3:
                score += 30
            else:
                score += 10
    
    # 2. 三字母组合匹配
    for i in range(len(text_lower) - 2):
        trigram = text_lower[i:i+3]
        if trigram.isalpha() and trigram in common_trigrams:
            score += 8
    
    # 3. 双字母组合匹配
    for i in range(len(text_lower) - 1):
        bigram = text_lower[i:i+2]
        if bigram.isalpha() and bigram in common_bigrams:
            score += 2
    
    # 4. 字母频率评分
    for i, char in enumerate(common_letters):
        count = text_lower.count(char)
        if count > 0:
            score += (26 - i) * count * 0.1
    
    # 5. 额外加分
    alpha_count = sum(1 for c in text if c.isalpha())
    if len(text) > 0 and alpha_count / len(text) > 0.8:
        score += 15
    
    if ' ' in text and len(words) > 1:
        score += 10
    
    if len(text) > 0 and text[0].isupper():
        score += 5
    
    return score


def brute_force_best(text):
    """
    暴力破解并返回最可能的结果
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
