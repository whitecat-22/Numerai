# Numerai


[Numeraiトーナメント](https://numer.ai/tournament) 提出用の株価予測は、Webhookから[AWS APIGwatway](https://aws.amazon.com/jp/api-gateway/?nc2=h_ql_prod_serv_apig)を通じて、  
[Lambda](https://aws.amazon.com/jp/lambda/?nc2=h_ql_prod_serv_lbd)経由で[EC2](https://aws.amazon.com/jp/ec2/?nc2=h_ql_prod_fs_ec2)(g4dn.xlearge)を起動する。  
EC2起動時に、インスタンス内： home/(user)/numerai/predict.py を起動する。

- predict.py が扱うデータは、traditional data のままです。　　　　　→順次対応中
　

　

- 参照元：  
[AWS EC2 で Numerai Compute](https://zenn.dev/kunigaku/articles/50c079b033e6051bc764)



<a href="https://numer.ai/tournament">
    <img src="https://github.com/whitecat-22/Numerai/blob/main/Numerai-Logo-Side-White.03e7575d.png">
</a>
