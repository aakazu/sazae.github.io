QUESTION=["サザエさんの旦那さんの名前は？","カツオの妹の名前は？","タラちゃんはカツオから見てどんな関係？"]

R_ANS=["マスオ","ワカメ","甥"]
R_ANS2=["ますお","わかめ","おい"]

for i range(3);
    print(QUESTION[i])
    ans=input()
    if ans == R_ANS[i] or ans == R_ANS2[i]:
        print("正解です")
    else:
        print("不正解です")
