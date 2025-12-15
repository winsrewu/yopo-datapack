[English](README.md) | 简体中文  

## yopo

yopo(You Only Play Once)是一个Minecraft数据包，它可以让玩家在游戏中只玩一次。

## 如何使用

yopo:encrypt_message 是入口函数. 执行它, 其余的它会自动处理, 最后告诉你你到底那没拿到许可.  
建议配合 https://github.com/winsrewu/yopo-web 使用. 它应该被我部署在 https://yopo.jawbts.org 上.
注意, 这个数据包使用 https://mcbuild.dev 构建.
请注意, Minecraft的命令限制是每tick特定次. 可以通过 ```/gamerule maxCommandChainLength <>``` 设置. 不够大的值可能会导致静默错误.

## 原理

首先数据包内置公钥, 通过每次加载随机生成id, 然后用公钥加密id, 并将加密后的id发送给服务器. 服务器收到加密后的id后, 先用私钥解密, 然后判断id是否有效, 如果有效, 则允许玩家进入游戏, 也就是使用私钥签名(id + 1) 返回给客户端, 否则拒绝进入. 客户端会验证签名有效性.