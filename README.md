English | [简体中文](README_zh_CN.md)  

## yopo

You Only Play Once (YOPo) is a Minecraft data pack that allows players to play the game only once.

## How to Use

Use `yopo:encrypt_message` as the entry function. The rest will be handled automatically, and it will tell you whether you have obtained a license.
It is recommended to use in conjunction with https://github.com/winsrewu/yopo-web. It should be deployed at https://yopo.jawbts.org.
Note that this data pack is built using https://mcbuild.dev.

## Principle

The data pack contains a built-in public key. It generates a random ID each time it loads, encrypts the ID with the public key, and sends the encrypted ID to the server. The server decrypts the encrypted ID with a private key, checks if the ID is valid, and if it is, allows the player to enter the game by signing the ID + 1 and returning it to the client. Otherwise, it denies entry. The client verifies the signature.