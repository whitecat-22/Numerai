import os
import time
import pytz
import requests
import traceback
import numpy as np
import numerapi
import pandas as pd
from datetime import datetime, timezone

# line notify APIのトークン
line_notify_token = os.environ.get("LINE_NOTIFY_TOKEN")
# line notify APIのエンドポイントの設定
line_notify_api = 'https://notify-api.line.me/api/notify'

jst_nowtime= ""
def line_post(notification_message):
    # 現在時刻
    now = datetime.now(tz=timezone.utc)
    tokyo = pytz.timezone('Asia/Tokyo')
    # 東京のローカル時間に変換
    jst_now = tokyo.normalize(now.astimezone(tokyo))
    jst_nowtime = jst_now.strftime("%m/%d %H:%M")
    # ヘッダーの指定
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    # 送信するデータの指定
    data = {'message': f'{notification_message}'}

    # line notify apiにpostリクエストを送る
    requests.post(line_notify_api, headers=headers, data=data)

# notification_message = content0 +'\n' + '\n\n'.join(content_text)
notification_message = jst_nowtime +'\n' + "Numerai:価格予測開始"
line_post(notification_message)


try:
    """
    Catboostを呼び出しnumeraiに予測を提出する
    """
    # 必要なライブラリのinstall
    #!pip install numerapi
    #!pip install catboost

    import numerapi
    # 回帰を使うので、CatBoostRegressorを呼び出す
    from catboost import CatBoostRegressor

    # numerapiを使えばデータセットのダウンロードが簡単にできる
    #インスタンス化（numerapiを使うための準備）
    napi = numerapi.NumerAPI(verbosity="info")

    # 現在のラウンドのデータセットをダウンロードして解凍する。
    napi.download_current_dataset(unzip=True)

    """
    準備：トーナメントの現在のラウンド数を取得
    """
    # numerai_dataset_321/numerai_training_data.csv でトレーニングデータのファイル名
    # numerai_dataset_321/numerai_tournament_data.csv でトーナメントデータのファイル名

    # まずは現在のトーナメントのラウンド数を取得(int型)
    current_ds = napi.get_current_round()
    print(current_ds)

    # ここはnumerai_dataset_321のようなパスを得るため
    latest_round = os.path.join('numerai_dataset_'+str(current_ds))
    print(latest_round)

    """
    トレーニングデータとトーナメントデータの読み込み
    """
    print("# データの読み込み中...")
    # トレーニングデータをCSVから読み込む。　set_indexでどの列をindexにするか？を決める
    training_data = pd.read_csv(os.path.join(latest_round, "numerai_training_data.csv")).set_index("id")

    # トーナメントデータをCSVから読み込む。
    tournament_data = pd.read_csv(os.path.join(latest_round, "numerai_tournament_data.csv")).set_index("id")

    feature_names = [f for f in training_data.columns if "feature" in f]

    """
    データの確認
    """
    training_data.head()
    training_data.shape

    tournament_data.tail()
    tournament_data

    feature_names
    len(feature_names)

    """
    モデルのトレーニング
    """
    # GPUの指定
    params = {
        'task_type': 'GPU'
        }
    # モデルのインスタンス化（準備）
    model = CatBoostRegressor(**params)

    # モデルのトレーニング　model.fit(X, Y)  ⇨Xは特徴量、Yが予測したい値（列）
    model.fit(training_data[feature_names], training_data["target"])

    """
    予測をする
    """
    predictions = model.predict(tournament_data[feature_names])

    # 予測結果をデータフレームの予測列とした。
    tournament_data['prediction'] = predictions

    # トーナメント名
    TOURNAMENT_NAME = "nomi"

    tournament_data['prediction'].to_csv(f"{TOURNAMENT_NAME}_{current_ds}_submission.csv")

    """
    予測をAPIキーを使って提出する
    """
    # APIキーの設定
    public_id = os.environ.get('PUBLIC_ID')
    secret_key = os.environ.get('SECRET_KEY')
    model_id = os.environ.get('MODEL_ID')

    napi = numerapi.NumerAPI(public_id=public_id, secret_key=secret_key)

    # 予測の提出
    submission_id = napi.upload_predictions(f"{TOURNAMENT_NAME}_{current_ds}_submission.csv", model_id=model_id)

    # LINE通知（終了：成功）
    notification_message = jst_nowtime +'\n' + "Numerai:価格予測 提出完了"
    line_post(notification_message)

except:
    # LINE通知（終了：失敗）
    notification_message = jst_nowtime +'\n' + "Numerai:価格予測失敗" +'\n\n' + traceback.format_exc()
    line_post(notification_message)
