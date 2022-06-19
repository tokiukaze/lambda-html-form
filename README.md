# サンプルプロジェクト

lambdaでhtmlフォームを実装するサンプルプロジェクトです。

```text
.
├── README.md
├── docs                # sam initで生成されたREADME
├── html_input_form     # pythonプログラム
├── pyproject.toml      # python プロジェクト設定ファイル
├── template.yaml       # aws sam設定ファイル（aws api gatewayやlambdaの設定）
├── .flake8             # flake8設定ファイル（flake8とはlintツールのこと）
├── tests               # python testプログラム
└── venv                # venv仮想環境ファイル
```

## 環境の構築

環境を構築するための方法です。
下記がインストール済みであることが前提条件です。

* python
* vscode (python拡張機能)
* aws sam cli　(アカウント設定済み)

### 仮想環境の構築

venvを使用して開発環境を構築します。

$`python3 -m venv venv`

仮想環境"./vnev"が作成された後は、仮想化環境有効化コマンドでターミナルを仮想化します。

__venv 仮想環境の有効化コマンド__

$`. ./venv/bin/activate`

### パッケージのインストール

ローカルで開発を行うためのパッケージをインストールします。

$`cd html_input_form`

$`pip install -r requirements.txt`

$`cd ../tests`

$`pip install -r requirements.txt`

## 開発

ローカルでlambdaサーバーを構築しブラウザやcurlからテストできます。

```
> sam build && sam local start-api
...
2021-11-26 17:43:08  * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
```

[Tutorial - Lambda Powertools Python](https://awslabs.github.io/aws-lambda-powertools-python/latest/tutorial/#local-test)

詳しいドキュメントは[/docs](/docs/)にあります。

### デプロイ

開発したソースコードをawsにデプロイします。  
こちらも詳しくは[/docs](/docs)を見てください。

1. __sam buildコマンド__

プロジェクトをビルドします。

[sam build - AWS Serverless Application Model](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-build.html)

$`sam build --use-container`

2. __sam deployコマンド__

AWSにプロジェクトをアップロードします。

[sam deploy - AWS Serverless Application Model](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-deploy.html)

$`sam deploy --guided`
