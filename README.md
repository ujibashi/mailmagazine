# mailmagazine

メールマガジン利用者リストのCSVファイルをまとめます。

### 使い方

1. フォルダに、メールマガジン名.csv のファイル名でファイルを作成します。
  - 0列目：名字
  - 1列目：名前
  - 2列目；メールアドレス
2. 以下の実行方法に従って実行すると、ファイルをまとめて、フォルダにmain.csvファイルが作成されます。

### 実行方法

```
$ cd ~
$ python3 mailmagazine/run.py <フォルダ>
```

### ソースコードの(run.py)更新方法

```
$ cd ~
$ cd mailmagazine
$ git pull
```
