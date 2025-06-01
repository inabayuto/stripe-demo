# Stripe デモプロジェクト

このプロジェクトは、Pythonを使用した基本的なStripe API操作（顧客の作成、支払い方法の紐付け、決済インテントの作成・確定など）を示すデモです。

## セットアップ

1.  **Dockerのインストール**: お使いのシステムにDockerがインストールされていることを確認してください。
2.  **`.env` ファイルの作成**: プロジェクトのルートディレクトリに、Stripeシークレットキーを記述した `.env` ファイルを作成してください。
    ```dotenv
    STRIPE_SECRET_KEY=sk_test_********************************
    STRIPE_PUBLISHABLE_KEY=sk_test_********************************
    ```
    `sk_test_...` の部分は、実際のStripeテストシークレットキーに置き換えてください。

## Dockerでの実行

1.  **Dockerイメージのビルド**: ターミナルでプロジェクトのルートディレクトリに移動し、以下のコマンドを実行します。
    ```bin/bash
    docker run -it stripe-dev:latest /bin/bash 
    ```

## ファイル構成と役割

-   `main.py`: Stripe操作を実行するメインスクリプトです。他のモジュールへの呼び出しを調整します。
-   `customer.py`: Stripe顧客を管理するための関数を含みます。
-   `payment_method.py`: Stripe支払い方法を処理するための関数を含みます。
-   `payment_intent.py`: Stripe決済インテントを作成・確定するための関数を含みます。
-   `utils/`: Stripeクライアントの初期化など、共通のユーティリティ関数を含むディレクトリです（例: `setup.py`）。
-   `requirements.txt`: プロジェクトに必要なPythonライブラリをリストアップしています。
-   `Dockerfile`: アプリケーション用のDockerイメージを作成するための定義ファイルです。