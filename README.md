# Numerai


[Numeraiトーナメント](https://numer.ai/tournament#) 提出用の株価予測は、WebhookからAWS APIGwatwayを通じて、Lambda経由でEC2(g4dn.xlearge)を起動。  
EC2起動時に、インスタンス内： home/(user)/numerai/predict.py を起動する。

参照元：  
[AWS EC2 で Numerai Compute](https://zenn.dev/kunigaku/articles/50c079b033e6051bc764)



![https://github.com/whitecat-22/Numerai/blob/main/Numerai-Logo-Side-White.03e7575d.png](https://github.com/whitecat-22/Numerai/blob/main/Numerai-Logo-Side-White.03e7575d.png)
