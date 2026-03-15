项目简介
本工具是一款基于Python的凯撒密码加密解密程序，支持智能暴力破解功能，通过文本可读性评分算法自动识别最可能的解密结果。

功能特性

1.加密功能：将明文按指定步长偏移加密 

2.解密功能：将密文按指定步长还原为明文 

3.智能破解：自动分析并输出最可能的解密结果 

4.全量破解：显示所有25种可能的解密结果

智能评分算法说明

评分函数通过五个维度评估解密文本的可读性，分数越高表示越可能是正确解密

1.完整单词匹配(权重最高):程序内置数百个常见英文单词，匹配成功根据单词长度加分，5字母以上单词加50分，3至5字母单词加30分，短单词加10分

2.三字母组合匹配:识别the、and、ing、hel、wor等常见三字母组合，每个匹配加8分

3.双字母组合匹配:识别th、he、in、er等高频双字母组合，每个匹配加2分

4.字母频率评分:基于英文字母出现频率统计，常见字母如e、t、a权重更高

5.额外加分:包括字母占比超过百分之八十加15分，有空格分隔的单词加10分，首字母大写加5分

使用示例
命令行交互
运行程序后显示欢迎界面和功能菜单，用户输入选项1即可进入加密功能，输入明文Hello World，输入步长为3，得到密文为Khoor Zruog。
![功能1](https://github.com/Python-Programming-2026/project1-caesar-cipher-syy/blob/main/01631b2043e4ad55c4ad59924c5c2012.png?raw=true)

同理功能2可将密文破解成明文

![2](https://github.com/Python-Programming-2026/project1-caesar-cipher-syy/blob/main/a248f4a90c453d168536e73b88471b02.png?raw=true)

功能3可直接得出得分最高的明文
![3](https://github.com/Python-Programming-2026/project1-caesar-cipher-syy/blob/main/38ef54f37c8b5b826e7a1a4f134056e7.png?raw=true)

功能4可得出所有25种解密结果
![4](https://github.com/Python-Programming-2026/project1-caesar-cipher-syy/blob/main/3e75a3582cedce4600553c1052528116.png?raw=true)


注意事项
语言支持：仅支持英文字母，中文、数字、符号不加密。 文本长度：短文本少于10字符时评分可能不准确。 步长范围：有效步长为1至25，26等于无偏移。 大小写：加密后保留原文大小写格式。

