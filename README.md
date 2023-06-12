# LangChain Cloud Functions Source

LangChainを使ってChatGPTプラグインを試す関数
pluginはconfig.ymlにlang-chain.api-pluginsに追加していく。

## Cloud Functions

### 関数
https://console.cloud.google.com/functions/details/us-central1/lang-chain?env=gen1&hl=ja&project=xproject&tab=source

### 関数実行

```
$ curl -X POST https://us-central1-xproject.cloudfunctions.net/lang-chain -H "Authorization: bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" -d '{"message": "What t shirts are available in klarna?"}'
```

## ローカル開発

ローカル環境で関数を実行する場合はfunctions-frameworkを利用する。
Running on http...に記載されているURLに対してリクエストを実行するだけ。

```
$ functions-framework --target=run --debug
 * Serving Flask app 'run'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://192.168.2.174:8080
Press CTRL+C to quit
 * Restarting with watchdog (fsevents)
 * Debugger is active!
```