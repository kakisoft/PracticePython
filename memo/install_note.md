# choco（Windows）
```
choco install python
```
パスが通されてない。

## インストーラ
インストール時に、パスを設定するチェックボックスがある。



# apt（ubuntu）
Javaがインストールされていない場合、インストールしておきます。
```
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
```
Pycharmインストール手順
```
sudo sh -c 'echo "deb http://archive.getdeb.net/ubuntu $(lsb_release -sc)-getdeb apps" >> /etc/apt/sources.list.d/getdeb.list'
wget -q -O - http://archive.getdeb.net/getdeb-archive.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install pycharm
```
起動コマンド
```
pycharm
```
