※ 機械翻訳で日本語にしたテンプレート付属READMEです。また、このサンプルプロジェクトは`/hello_world`から`/html_input_form`にフォルダ名が変更されています。

# sam-app

このプロジェクトには、SAM CLI でデプロイするサーバーレスアプリケーションのソースコードとサポートファイルが含まれています。以下のファイルおよびフォルダが含まれます。

- hello_world - アプリケーションのLambda関数のコード。
- events - 関数を呼び出すために使用する呼び出しイベント。
- tests - アプリケーションのコードに対するユニットテスト。
- template.yaml - アプリケーションのAWSリソースを定義するテンプレート。

このアプリケーションでは、Lambda関数やAPI Gateway APIなど、いくつかのAWSリソースを使用します。これらのリソースは、このプロジェクトの `template.yaml` ファイルで定義されています。アプリケーションコードを更新するのと同じデプロイメントプロセスを通じて、AWSリソースを追加するためにテンプレートを更新することができます。

アプリケーションの構築とテストに統合開発環境（IDE）を使用したい場合は、AWS Toolkitを使用することができます。 
AWS Toolkitは、一般的なIDE用のオープンソースプラグインで、SAM CLIを使用してAWS上のサーバーレスアプリケーションを構築し、デプロイすることができます。AWS Toolkitはまた、Lambda関数コードのための簡略化されたステップスルーデバッグエクスペリエンスを追加します。以下のリンクを参照してください。

* [CLion](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [GoLand](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [WebStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [Rider](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PhpStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [RubyMine](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [DataGrip](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## サンプルアプリケーションのデプロイ

Serverless Application Model Command Line Interface (SAM CLI) は、AWS CLI の拡張機能で、Lambda アプリケーションを構築・テストするための機能を追加したものです。Dockerを使用して、LambdaにマッチしたAmazon Linux環境で機能を実行します。また、アプリケーションのビルド環境とAPIをエミュレートすることもできます。

SAM CLI を使用するには、以下のツールが必要です。

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

アプリケーションを初めてビルドしてデプロイするには、シェルで次のように実行します。

```bash
sam build --use-container
sam deploy --guided
```

最初のコマンドは、あなたのアプリケーションのソースを構築します。2番目のコマンドは、一連のプロンプトを表示しながら、アプリケーションをパッケージ化してAWSにデプロイします。

* **Stack Name**: CloudFormationにデプロイするスタックの名前です。これはアカウントとリージョンに固有のものであるべきで、プロジェクト名と一致するものが良い出発点でしょう。
* **AWS Region**: アプリをデプロイするAWSリージョンです。
* **Confirm changes before deploy**: デプロイ前に変更を確認する。* **Confirm changes before deploy**: yesに設定すると、手動レビューのために実行前にすべての変更セットが表示されます。Noに設定すると、AWS SAM CLIはアプリケーションの変更を自動的にデプロイします。
* **Allow SAM CLI IAM role creation**: この例を含む多くのAWS SAMテンプレートは、AWSサービスにアクセスするために含まれるAWS Lambda関数（複数可）に必要なAWS IAMロールを作成します。デフォルトでは、これらは必要最小限の権限にスコープダウンされています。IAM ロールを作成または変更する AWS CloudFormation スタックをデプロイするには、`capabilities` に `CAPABILITY_IAM` 値を指定する必要があります。このプロンプトで権限が提供されない場合、このサンプルをデプロイするには、`--capabilities CAPABILITY_IAM` を `sam deploy` コマンドに明示的に渡す必要があります。
* **Save arguments to samconfig.toml**: Yesに設定すると、選択した内容がプロジェクト内の設定ファイルに保存され、将来的にパラメータなしで `sam deploy` を再実行することで、アプリケーションに変更を加えることができるようになります。

API Gateway Endpoint の URL は、デプロイ後に表示される出力値で確認することができます。

## SAM CLI を使用して、ローカルでビルドおよびテストを行います

アプリケーションを `sam build --use-container` コマンドでビルドします。

```bash
sam-app$ sam build --use-container
```

SAM CLI は `hello_world/requirements.txt` で定義された依存関係をインストールし、配置パッケージを作成し、 `.aws-sam/build` フォルダに保存します。

テストイベントを使って直接関数を呼び出して、一つの関数をテストします。イベントは、関数がイベントソースから受け取る入力を表す JSON ドキュメントです。テストイベントは、このプロジェクトの `events` フォルダに含まれています。

関数をローカルで実行し、`sam local invoke` コマンドで呼び出すことができます。

```bash
sam-app$ sam local invoke HelloWorldFunction --event events/event.json
```

SAM CLI は、アプリケーションの API をエミュレートすることもできます。Sam local start-api` を使用すると、ポート 3000 で API をローカルに実行することができます。

```bash
sam-app$ sam local start-api
sam-app$ curl http://localhost:3000/
```

SAM CLI はアプリケーションのテンプレートを読み込んで、API のルートと呼び出される関数を決定します。各関数の定義にある `Events` プロパティには、各パスのルートとメソッドが含まれています。

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

## アプリケーションにリソースを追加する

アプリケーションテンプレートは、AWS Serverless Application Model (AWS SAM) を使用してアプリケーションリソースを定義します。AWS SAMはAWS CloudFormationの拡張機能で、関数、トリガー、APIなどの一般的なサーバーレスアプリケーションのリソースを構成するためのシンプルな構文を持っています。[SAM仕様](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md)に含まれないリソースについては、標準の[AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)リソースタイプを使用することが可能です。

## Lambda関数のログをフェッチ、テール、フィルターする

トラブルシューティングを簡単にするために、SAM CLI には `sam logs` というコマンドがあります。`sam logs` を使うと、デプロイした Lambda 関数で生成されたログをコマンドラインから取得することができます。ターミナルにログを出力するだけでなく、このコマンドにはバグを素早く発見するための気の利いた機能がいくつか用意されています。

`NOTE`: このコマンドは、SAMを使用してデプロイしたものだけでなく、すべてのAWS Lambda関数に対して機能します。

```bash
sam-app$ sam logs -n HelloWorldFunction --stack-name sam-app --tail
```

Lambda関数のログをフィルタリングする方法については、[SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html)に詳細な情報と例が記載されています。

## テスト

テストはこのプロジェクトの `tests` フォルダに定義されています。PIP を使用して、テストの依存関係をインストールし、テストを実行します。

```bash
sam-app$ pip install -r tests/requirements.txt --user
# ユニットテスト
sam-app$ python -m pytest tests/unit -v
# 統合テスト、最初にスタックをデプロイする必要があります。
# 環境変数 AWS_SAM_STACK_NAME にテストするスタックの名前を作成します。
sam-app$ AWS_SAM_STACK_NAME=<スタック名> python -m pytest tests/integration -v
```

## クリーンアップ

作成したサンプルアプリケーションを削除するには、AWS CLIを使用します。スタック名に自分のプロジェクト名を使ったと仮定して、以下を実行します。

```bash
aws cloudformation delete-stack --stack-name sam-app
```

## リソース

SAMの仕様、SAM CLI、サーバーレスアプリケーションの概念については、[AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)を参照してください。

次に、AWS Serverless Application Repositoryを利用して、Hello Worldのサンプルを超えるすぐに使えるAppをデプロイし、作者がどのようにアプリケーションを開発したかを学ぶことができます。[AWS Serverless Application Repositoryのメインページ](https://aws.amazon.com/serverless/serverlessrepo/)

無料版の[DeepL翻訳](www.DeepL.com/Translator)で翻訳しました。
