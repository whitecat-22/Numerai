# Numerai


Numerai価格予想は、WebhookからAWS APIGwatwayを通じて、Lambda経由でEC2(g4dn.xlearge)を起動。  
EC2起動時に、インスタンス内： (ubuntu)/numerai/predict.py を起動する。

参照元：  
[AWS EC2 で Numerai Compute](https://zenn.dev/kunigaku/articles/50c079b033e6051bc764)
