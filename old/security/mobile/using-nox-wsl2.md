# Using Nox and WSL2

나는 원래 WSL2 사용자다. WSL이 정말 넘사로 너무 좋다고 생각하고, 너무도 잘 쓰고 있었으나 모바일 분석을 위해 Nox를 설치하면서 불편함이란걸 느꼈다.  

WSL2 구동을 위해 설정한 Hyper-V 때문에 다른 프로그램에서 인텔 VT를 사용하지 못한다. 인텔 VT가 Hyper-V 전용으로 완전히 고정되어버리기 때문이다.

혹여나 WSL2를 Hyper-V 없이 사용할 수 있는 방법이 있는지 알아봤으나 현재로써는 못하는 것 같다. [참고](https://github.com/MicrosoftDocs/WSL/issues/899)

## 다시 WSL 전환방법
```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```