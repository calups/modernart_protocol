Simple Modern Art Protocol
====

競りゲームの傑作「モダンアート」を単純化し、ソケット通信でAI同士の対戦ができるようにしたものです。

## デモ
<img src="/image/modern.gif?raw=true" width="673px">

## とりあえず試したい

    git clone https://github.com/calups/modernart_protocol
    cd modernart_protocol
    python Server/SimpleModern.py &
    python 5mura.sh &
    
サーバーとサンプルエージェント5体が立ち上がります。

## シンプルモダンアート

プレイ（と実装）を簡単にするため、シンプルなルールを制定しました。

### ルール（知ってる人向け）

- 競りの種類が「入札」（握り込み）だけに。
- 当然ダブルオークションもない。
- プレイヤー間での意思疎通は不可。出品する絵と入札金額で想いを伝えよう。

上記3点以外は正規のルールと全く同じです。
3人プレイ用の選択ルール、ダブルオークションに関する選択ルールは使用しません。

### ルール（知らない人向け）

http://www.newgamesorder.jp/games/modernart
の下の方からモダンアート.pdfをダウンロードして読んだ後、ここから5行くらい上に目を通してください。

## Requirement

Python3で動作確認。
特別なモジュールは必要ない（はず）

## エージェントの作り方

sample_agent.pyの関数を書き換えて自分だけのモダンアートエージェントを作りましょう。
値を返す必要がある関数はsellとbidだけです。

sellは自分の出品ターンが回ってきた時にどの絵を出すか、
bidは出品された絵に対していくらで入札するかを返します。

ソケット通信部分を実装すれば、Python以外のエージェントも接続可能です。

## Contribution

## Licence
