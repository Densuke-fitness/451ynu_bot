# 451ynu_bot
 Automatic tweet by using twitter API

**[10万分の1の確率で横浜市立大学もしくは横浜国立大学になるbot](https://twitter.com/451ynu_bot)**

[![Image from Gyazo](https://i.gyazo.com/2536c22cb2a53a43afdc71bea01f509b.png)](https://gyazo.com/2536c22cb2a53a43afdc71bea01f509b)


## Description of contents
### 1.約1/2の確率でヨコイチか横国の文字リストの一方を選択する
選択元の文字リスト
[![Image from Gyazo](https://i.gyazo.com/f96634135fbf197d08e5d6617ef9c70c.png)](https://gyazo.com/f96634135fbf197d08e5d6617ef9c70c)

ランダムで取得した値が451(ヨコイチ)以下なら横市, より大きい値なら横国を選択

[![Image from Gyazo](https://i.gyazo.com/12b389bd6dfbec87d2503424dc96c51f.png)](https://gyazo.com/12b389bd6dfbec87d2503424dc96c51f)

### 2.ランダムで6文字を作成しツイート
選択した大学の文字リストから、重複を許してランダムで6文字を作成
[![Image from Gyazo](https://i.gyazo.com/611762d0641bafb20d6d3b7fc8e115e4.png)](https://gyazo.com/611762d0641bafb20d6d3b7fc8e115e4)

作成した6文字に学部名を加えながら自動ツイートを行う
[![Image from Gyazo](https://i.gyazo.com/68f809385a5764457809e79d22c2a1a3.png)](https://gyazo.com/68f809385a5764457809e79d22c2a1a3)

## Infrastructure
AWS LambdaとCloudWatchEventを用いて30分毎に実行。

[![Image from Gyazo](https://i.gyazo.com/fd4e33031bdf3822246c68322c66c8b0.png)](https://gyazo.com/fd4e33031bdf3822246c68322c66c8b0)

## Reference
- [TwitterのAPIライブラリtweepyを用いて定期ツイート等を実装してみる](https://qiita.com/macaroni10y/items/373f5451c93b824b30fe)

- [AWS LambdaにPythonをモジュール毎zipでアップロードする方法](https://www.suzu6.net/posts/83-lambda-zip/)

- [0.000850%の確率で東京都立大学になるbot](https://twitter.com/bot_tmu_850)