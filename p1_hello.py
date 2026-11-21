# p1_hello.py — print、變數、四則運算
# 按 F5 執行，看下方 Shell 印出什麼。

print("哈囉，守護瓶！")

# 變數：用一個名字記住一個值
group = 3
name = "守護瓶"
print("第", group, "組的", name)

# 四則運算：+  -  *  /  **（次方）
ax = 0
ay = 0
az = 1
print("ax 的平方 =", ax ** 2)

# 總加速度 = 根號(ax² + ay² + az²)；** 0.5 就是開根號
mag = (ax ** 2 + ay ** 2 + az ** 2) ** 0.5
print("總加速度 =", mag, "g")

#group 9

# 小挑戰：把 ax、ay、az 改成 0、0、1，總加速度是多少？
# 再改成 2、0、0 呢？哪一組比較像「撞到東西」？
