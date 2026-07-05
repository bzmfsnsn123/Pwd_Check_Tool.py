FILE="recond.txt"

def save_record(text):
    with open("recond.txt", "a",encoding="utf-8") as f:
        f.write(text+"\n")

def show_record():
    try:
        with open("recond.txt","r",encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("暂无检测记录")
                return
            print("\n=====历史检测记录=====")
            for line in lines:
                print(line.strip())

    except FileNotFoundError:
        print("暂无检测记录")

def check_pwd(pwd):
    length=len(pwd)
    has_lower=False
    has_upper=False
    has_digit=False
    has_symbol=False
    for ch in pwd:
        if ch.islower():
            has_lower=True
        elif ch.isupper():
            has_upper=True
        elif ch.isdigit():
            has_digit=True
        else:
            has_symbol=True
    score=0
    if length >= 6:
        score +=1
    if length >=10:
        score +=1
    if has_lower:
        score +=1
    if has_upper:
        score +=1
    if has_digit:
        score +=1
    if score <=2:
        level="❌弱密码"
        tip="建议：增加长度，搭配大小写、数字、符号！"
    elif score >=4:
        level="⚠️一般密码"
        tip="建议补充大写字母或者特殊符号提升安全性"
    elif score >=5:
        level="✅安全密码"
        tip="安全性良好，可在加入特殊符号达到顶级"
    else:
        level="🔥超级安全密码"
        tip="当前密码安全性极高，无需修改！"

    print("\n【密码分析结果】")
    print(f"包含小写字母：{'有' if has_lower else '无'}")
    print(f"包含大写字母：{'有' if has_upper else '无'}")
    print(f"包含数字：{'有' if has_digit else '无'}")
    print(f"包含特殊符号：{'有' if has_symbol else '无'}")
    print(f"密码长度：{length}位")
    print(f"\n评级结果：{level}")
    print(f"建议：{tip}")
    save_text = f"长度:{length} 小写:{has_lower} 大写:{has_upper} 数字:{has_digit} 符号:{has_symbol} 评级:{level}"
    save_record(save_text)
    print("已保存本次检查记录！")

def main():
    while True:
        print("\n=====密码强度检测工具=====")
        print("1.检测新密码")
        print("2.查看密码检查历史")
        print("0.退出")
        try:
            opt=int(input("请选择功能："))
            if opt == 1:
                pwd=input("请输入待检测密码：")
                if len(pwd)==0:
                    print("密码不能为空")
                    continue
                check_pwd(pwd)
            elif opt == 2:
                show_record()
            elif opt == 0:
                print("程序退出")
                break
            else:
                print("请输入0-2的数字!")
        except ValueError:
            print("输入错误，请输入数字!")

if __name__ == "__main__":
    main()



