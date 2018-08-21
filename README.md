シンプルモダンアートプロトコル
====

競りゲームの傑作「モダンアート」を単純化し、ソケット通信でAI同士の対戦ができるようにしたものです。

## デモ
![デモ](https://imgur.com/YEtB1Kw.gif)

## とりあえず試したい

    git clone https://sav_slug@bitbucket.org/sav_slug/modernart_protocol.git
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

### ルール（知らない人向け）

http://www.newgamesorder.jp/games/modernart
の下の方からモダンアート.pdfをダウンロードして読んだ後、ここから5行くらい上に目を通してください。

## Requirement

Python3で動作確認。
特別なモジュールは必要ない（はず）

## 使い方

## Install

## Contribution

## Licence
