# robotframework

***Settings***

Library     Selenium2Library

***Test Cases***
百度搜索
    [Setup]
        打开百度
        Maximize Browser Window
    输入关键字
    [Teardown]
        Close Browser

***Keywords***
打开百度
    Open Browser     http://www.baidu.com    chrome

输入关键字
    Input Text      id:kw   helloworld