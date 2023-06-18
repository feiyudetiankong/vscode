"""
Game_Name:TenHalf
Developer:Chen
Version:1.0
Date:2023/6/16
"""

#创建一个玩家player1
#玩家信息应包括玩家姓名、筹码、要牌标识符、一张扑克牌、牌点数、下注数

player1_Name = input("请输入玩家姓名：")    #从键盘输入玩家姓名，属于字符串型。
print("欢迎你，",player1_Name)  #打印欢迎信息
player1_card = input("请输入一张扑克牌：")  #从键盘输入一张扑克牌，属于字符串型。
player1_moner = 120
player1_flag = True
player1_pointsum = 0
player1_bet = 0

#打印玩家信息
print("玩家姓名：",player1_Name)
print("筹码：",player1_moner)
print("要牌标识符",player1_flag)
print("一张扑克牌",player1_card)
print("牌点数",player1_pointsum)
print("下注数",player1_bet)
